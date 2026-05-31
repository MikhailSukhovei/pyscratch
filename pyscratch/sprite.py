from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from math import cos, radians, sin
from typing import TYPE_CHECKING

from .commands import Call, Command
from .collision import Circle

if TYPE_CHECKING:
    from .runtime import Stage


@dataclass
class Sprite:
    name: str
    x: float = 0
    y: float = 0
    direction: float = 90
    visible: bool = True
    size: float = 100
    color: tuple[int, int, int] = (255, 170, 40)
    costume: str | None = None
    collision_radius: float = 20
    stage: "Stage | None" = None
    green_flag_scripts: list[Callable[[], object]] = field(default_factory=list)

    def when_green_flag_clicked(self, script: Callable[[], object]) -> Callable[[], object]:
        self.green_flag_scripts.append(script)
        return script

    def move_steps(self, steps: float) -> Command:
        return Call(lambda: self._move_steps(steps))

    def _move_steps(self, steps: float) -> None:
        angle = radians(90 - self.direction)
        self.x += cos(angle) * steps
        self.y += sin(angle) * steps

    def turn_right(self, degrees: float) -> Command:
        return Call(lambda: self._turn_right(degrees))

    def _turn_right(self, degrees: float) -> None:
        self.direction = (self.direction + degrees) % 360

    def turn_left(self, degrees: float) -> Command:
        return Call(lambda: self._turn_left(degrees))

    def _turn_left(self, degrees: float) -> None:
        self.direction = (self.direction - degrees) % 360

    def go_to(self, x: float, y: float) -> Command:
        return Call(lambda: self._go_to(x, y))

    def _go_to(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def change_x_by(self, value: float) -> Command:
        return Call(lambda: self._change_x_by(value))

    def _change_x_by(self, value: float) -> None:
        self.x += value

    def change_y_by(self, value: float) -> Command:
        return Call(lambda: self._change_y_by(value))

    def _change_y_by(self, value: float) -> None:
        self.y += value

    def set_x(self, value: float) -> Command:
        return Call(lambda: self._set_x(value))

    def _set_x(self, value: float) -> None:
        self.x = value

    def set_y(self, value: float) -> Command:
        return Call(lambda: self._set_y(value))

    def _set_y(self, value: float) -> None:
        self.y = value

    def point_in_direction(self, degrees: float) -> Command:
        return Call(lambda: self._point_in_direction(degrees))

    def _point_in_direction(self, degrees: float) -> None:
        self.direction = degrees % 360

    def show(self) -> Command:
        return Call(self._show)

    def _show(self) -> None:
        self.visible = True

    def hide(self) -> Command:
        return Call(self._hide)

    def _hide(self) -> None:
        self.visible = False

    def change_size_by(self, value: float) -> Command:
        return Call(lambda: self._change_size_by(value))

    def _change_size_by(self, value: float) -> None:
        self.size += value

    def set_size_to(self, value: float) -> Command:
        return Call(lambda: self._set_size_to(value))

    def _set_size_to(self, value: float) -> None:
        self.size = value

    def switch_costume_to(self, path: str) -> Command:
        return Call(lambda: self._switch_costume_to(path))

    def _switch_costume_to(self, path: str) -> None:
        self.costume = path

    def collision_circle(self) -> "Circle":
        return Circle(self.x, self.y, self.collision_radius * self.size / 100)

    def touching_sprite(self, other: "Sprite") -> bool:
        if self.stage is None:
            return False
        return self.stage.collisions.touching(self, other)

    def touching_any_sprite(self) -> bool:
        if self.stage is None:
            return False
        return self.stage.collisions.touching_any(self, self.stage.sprites)

    def touching_edge(self) -> bool:
        if self.stage is None:
            return False
        return self.stage.collisions.touching_edge(self, self.stage.width, self.stage.height)

    def if_on_edge_bounce(self) -> Command:
        return Call(self._if_on_edge_bounce)

    def _if_on_edge_bounce(self) -> None:
        if self.stage is None:
            return

        bounce = self.stage.collisions.edge_bounce(
            self,
            self.stage.width,
            self.stage.height,
        )
        bounced = False

        if bounce.hit_vertical_edge:
            self.x = bounce.x
            self.direction = (360 - self.direction) % 360
            bounced = True

        if bounce.hit_horizontal_edge:
            self.y = bounce.y
            self.direction = (180 - self.direction) % 360
            bounced = True

        if bounced:
            self.direction %= 360
