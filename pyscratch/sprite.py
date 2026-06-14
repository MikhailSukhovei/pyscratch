from __future__ import annotations

import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from math import cos, radians, sin
from pathlib import Path
from typing import TYPE_CHECKING

from .commands import Call, Command
from .collision import Circle
from .scripts import script as compile_script

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
    costumes: dict[int, str] = field(default_factory=dict)
    costume_number: int = 1
    collision_radius: float = 20
    stage: "Stage | None" = None
    green_flag_scripts: list[Callable[[], object]] = field(default_factory=list)
    _costume_base_path: Path = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._costume_base_path = _caller_directory()
        self.costumes = self._normalize_costumes(self.costumes)

        if self.costume is not None:
            self.costume = self._normalize_costume_path(self.costume)

        if self.costumes:
            if self.costume_number not in self.costumes:
                if self.costume_number == 1:
                    self.costume_number = sorted(self.costumes)[0]
                else:
                    raise ValueError(
                        f"Sprite {self.name!r} has no costume number "
                        f"{self.costume_number}."
                    )
            self.costume = self.costumes[self.costume_number]

    @property
    def costume_name(self) -> str | None:
        path = self.current_costume_path
        if path is None:
            return None
        return Path(path).stem

    @property
    def current_costume_path(self) -> str | None:
        if self.costumes:
            try:
                return self.costumes[self.costume_number]
            except KeyError as exc:
                raise ValueError(
                    f"Sprite {self.name!r} has no costume number "
                    f"{self.costume_number}."
                ) from exc
        return self.costume

    def when_green_flag_clicked(self, script: Callable[[], object]) -> Callable[[], object]:
        compiled_script = compile_script(script)
        self.green_flag_scripts.append(compiled_script)
        return compiled_script

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

    def switch_costume_to(self, costume: int | str) -> Command:
        return Call(lambda: self._switch_costume_to(costume))

    def _switch_costume_to(self, costume: int | str) -> None:
        if isinstance(costume, int):
            if not self.costumes:
                if costume == self.costume_number:
                    return
                raise ValueError(
                    f"Sprite {self.name!r} has no costume number {costume}."
                )
            self._switch_costume_number_to(costume)
            return

        if self.costumes:
            self._switch_costume_named(costume)
            return

        self.costume = self._normalize_costume_path(costume)

    def next_costume(self) -> Command:
        return Call(self._next_costume)

    def _next_costume(self) -> None:
        if not self.costumes:
            return

        numbers = sorted(self.costumes)
        try:
            index = numbers.index(self.costume_number)
        except ValueError:
            index = -1
        self._switch_costume_number_to(numbers[(index + 1) % len(numbers)])

    def _switch_costume_number_to(self, number: int) -> None:
        if number not in self.costumes:
            raise ValueError(f"Sprite {self.name!r} has no costume number {number}.")

        self.costume_number = number
        self.costume = self.costumes[number]

    def _switch_costume_named(self, name: str) -> None:
        normalized_name = self._normalize_costume_path(name)
        matches = [
            number
            for number, path in self.costumes.items()
            if name in {path, Path(path).name, Path(path).stem}
            or normalized_name == path
        ]
        if not matches:
            raise ValueError(f"Sprite {self.name!r} has no costume named {name!r}.")
        if len(matches) > 1:
            raise ValueError(f"Sprite {self.name!r} has several costumes named {name!r}.")

        self._switch_costume_number_to(matches[0])

    def _normalize_costumes(self, costumes: dict[int, str]) -> dict[int, str]:
        normalized: dict[int, str] = {}
        for number, path in costumes.items():
            if not isinstance(number, int):
                raise TypeError(
                    f"Costume number for sprite {self.name!r} must be an integer."
                )
            if number < 1:
                raise ValueError(
                    f"Costume number for sprite {self.name!r} must be 1 or greater."
                )
            normalized[number] = self._normalize_costume_path(path)

        return normalized

    def _normalize_costume_path(self, path: str) -> str:
        costume_path = Path(path)
        if not costume_path.is_absolute():
            costume_path = self._costume_base_path / costume_path
        return str(costume_path.resolve())

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


def _caller_directory() -> Path:
    pyscratch_file = Path(__file__).resolve()
    frame = inspect.currentframe()
    try:
        while frame is not None:
            filename = frame.f_code.co_filename
            if filename != "<string>":
                path = Path(filename)
                if path.exists() and path.resolve() != pyscratch_file:
                    return path.resolve().parent
            frame = frame.f_back
    finally:
        del frame

    return Path.cwd()
