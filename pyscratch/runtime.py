from __future__ import annotations

from collections.abc import Callable, Iterator
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .commands import Command, _as_command
from .collision import CollisionEngine

if TYPE_CHECKING:
    from .sprite import Sprite


_current_stage: ContextVar["Stage | None"] = ContextVar("current_stage", default=None)


def current_stage() -> "Stage":
    stage = _current_stage.get()
    if stage is None:
        raise RuntimeError("No running Stage is active.")
    return stage


@dataclass
class Task:
    script: Iterator[None]
    stopped: bool = False

    def step(self) -> None:
        if self.stopped:
            return
        try:
            next(self.script)
        except StopIteration:
            self.stopped = True


@dataclass
class Stage:
    width: int = 480
    height: int = 360
    fps: int = 30
    background_color: tuple[int, int, int] = (255, 255, 255)
    sprites: list["Sprite"] = field(default_factory=list)
    time: float = 0.0
    collisions: CollisionEngine = field(default_factory=CollisionEngine)
    _tasks: list[Task] = field(default_factory=list)

    def add(self, sprite: "Sprite") -> "Sprite":
        sprite.stage = self
        self.sprites.append(sprite)
        return sprite

    def green_flag(self) -> None:
        self._tasks.clear()
        for sprite in self.sprites:
            for script_factory in sprite.green_flag_scripts:
                self.start(script_factory)

    def start(self, script_factory: Callable[[], Command | object]) -> None:
        result = script_factory()
        if hasattr(result, "run"):
            script = _as_command(result).run()
        elif isinstance(result, Iterator):
            script = result
        else:
            script = iter(())
        self._tasks.append(Task(script))

    def tick(self, dt: float | None = None) -> None:
        token = _current_stage.set(self)
        try:
            self.time += dt if dt is not None else 1 / self.fps
            for task in list(self._tasks):
                task.step()
            self._tasks = [task for task in self._tasks if not task.stopped]
        finally:
            _current_stage.reset(token)

    def run_for(self, seconds: float) -> None:
        self.green_flag()
        frame_count = int(seconds * self.fps)
        for _ in range(frame_count):
            self.tick()

    def play(self, title: str = "pyscratch") -> None:
        from .pygame_renderer import PygameRenderer

        PygameRenderer(self, title=title).run()
