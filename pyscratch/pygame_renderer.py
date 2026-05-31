from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .runtime import Stage
    from .sprite import Sprite


def stage_to_screen(
    x: float,
    y: float,
    stage_width: int,
    stage_height: int,
) -> tuple[int, int]:
    return round(stage_width / 2 + x), round(stage_height / 2 - y)


@dataclass(frozen=True)
class RenderState:
    x: float
    y: float
    direction: float
    size: float


class PygameRenderer:
    def __init__(
        self,
        stage: "Stage",
        title: str = "pyscratch",
        render_fps: int = 60,
        max_updates_per_frame: int = 5,
    ) -> None:
        try:
            import pygame
        except ImportError as exc:
            raise RuntimeError(
                "pygame is required for rendering. Install it with: pip install pygame"
            ) from exc

        self.pygame = pygame
        self.stage = stage
        self.title = title
        self.render_fps = render_fps
        self.max_updates_per_frame = max_updates_per_frame
        self._accumulator = 0.0
        self._previous_states: dict[int, RenderState] = {}
        self._costumes: dict[str, Any] = {}

    def run(self, max_frames: int | None = None) -> None:
        pygame = self.pygame
        pygame.display.init()
        pygame.font.init()

        screen = pygame.display.set_mode((self.stage.width, self.stage.height))
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()
        self.stage.green_flag()
        self.sync_interpolation_state()

        running = True
        frame_count = 0
        while running:
            real_dt = clock.tick(self.render_fps) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.advance_simulation(real_dt)
            self.draw(screen)
            pygame.display.flip()
            frame_count += 1
            if max_frames is not None and frame_count >= max_frames:
                running = False

        pygame.font.quit()
        pygame.display.quit()

    def advance_simulation(self, real_dt: float) -> int:
        fixed_dt = 1 / self.stage.fps
        if not self._previous_states:
            self.sync_interpolation_state()

        self._accumulator += real_dt
        updates = 0

        while (
            self._accumulator >= fixed_dt
            and updates < self.max_updates_per_frame
        ):
            self._previous_states = self._snapshot_states()
            self.stage.tick(fixed_dt)
            self._accumulator -= fixed_dt
            updates += 1

        if updates == self.max_updates_per_frame:
            self._accumulator = 0.0

        return updates

    def sync_interpolation_state(self) -> None:
        self._previous_states = self._snapshot_states()

    def interpolation_alpha(self) -> float:
        fixed_dt = 1 / self.stage.fps
        return max(0.0, min(1.0, self._accumulator / fixed_dt))

    def render_state(self, sprite: "Sprite") -> RenderState:
        current = self._state_for(sprite)
        previous = self._previous_states.get(id(sprite), current)
        alpha = self.interpolation_alpha()
        return RenderState(
            x=_lerp(previous.x, current.x, alpha),
            y=_lerp(previous.y, current.y, alpha),
            direction=_lerp_angle(previous.direction, current.direction, alpha),
            size=_lerp(previous.size, current.size, alpha),
        )

    def draw(self, screen: Any) -> None:
        pygame = self.pygame
        screen.fill(self.stage.background_color)
        for sprite in self.stage.sprites:
            if sprite.visible:
                self._draw_sprite(screen, sprite, self.render_state(sprite))

    def _draw_sprite(self, screen: Any, sprite: "Sprite", state: RenderState) -> None:
        surface = self._sprite_surface(sprite)
        scaled = self._scale(surface, state.size)
        rotated = self.pygame.transform.rotate(scaled, 90 - state.direction)
        center = stage_to_screen(state.x, state.y, self.stage.width, self.stage.height)
        rect = rotated.get_rect(center=center)
        screen.blit(rotated, rect)

    def _snapshot_states(self) -> dict[int, RenderState]:
        return {id(sprite): self._state_for(sprite) for sprite in self.stage.sprites}

    def _state_for(self, sprite: "Sprite") -> RenderState:
        return RenderState(sprite.x, sprite.y, sprite.direction, sprite.size)

    def _sprite_surface(self, sprite: "Sprite") -> Any:
        if sprite.costume:
            return self._load_costume(sprite.costume)
        return self._default_surface(sprite)

    def _load_costume(self, path: str) -> Any:
        if path not in self._costumes:
            image = self.pygame.image.load(Path(path)).convert_alpha()
            self._costumes[path] = image
        return self._costumes[path]

    def _default_surface(self, sprite: "Sprite") -> Any:
        pygame = self.pygame
        surface = pygame.Surface((48, 48), pygame.SRCALPHA)
        pygame.draw.circle(surface, sprite.color, (24, 24), 20)
        pygame.draw.circle(surface, (40, 40, 40), (24, 24), 20, 2)
        pygame.draw.polygon(surface, (40, 40, 40), [(38, 24), (28, 18), (28, 30)])
        return surface

    def _scale(self, surface: Any, size: float) -> Any:
        if size == 100:
            return surface
        width = max(1, round(surface.get_width() * size / 100))
        height = max(1, round(surface.get_height() * size / 100))
        return self.pygame.transform.smoothscale(surface, (width, height))


def _lerp(start: float, end: float, alpha: float) -> float:
    return start + (end - start) * alpha


def _lerp_angle(start: float, end: float, alpha: float) -> float:
    delta = (end - start + 180) % 360 - 180
    return (start + delta * alpha) % 360
