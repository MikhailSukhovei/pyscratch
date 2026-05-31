from __future__ import annotations

from dataclasses import dataclass
from math import hypot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sprite import Sprite


@dataclass(frozen=True)
class Circle:
    x: float
    y: float
    radius: float


@dataclass(frozen=True)
class EdgeBounce:
    x: float
    y: float
    hit_vertical_edge: bool = False
    hit_horizontal_edge: bool = False


class CollisionEngine:
    def touching(self, first: "Sprite", second: "Sprite") -> bool:
        if first is second:
            return False
        if not first.visible or not second.visible:
            return False

        first_circle = first.collision_circle()
        second_circle = second.collision_circle()
        distance = hypot(first_circle.x - second_circle.x, first_circle.y - second_circle.y)
        return distance <= first_circle.radius + second_circle.radius

    def touching_any(self, sprite: "Sprite", sprites: list["Sprite"]) -> bool:
        return any(self.touching(sprite, other) for other in sprites)

    def touching_edge(self, sprite: "Sprite", stage_width: int, stage_height: int) -> bool:
        bounce = self.edge_bounce(sprite, stage_width, stage_height)
        return bounce.hit_vertical_edge or bounce.hit_horizontal_edge

    def edge_bounce(self, sprite: "Sprite", stage_width: int, stage_height: int) -> EdgeBounce:
        circle = sprite.collision_circle()
        half_width = stage_width / 2
        half_height = stage_height / 2
        x = circle.x
        y = circle.y
        hit_vertical_edge = False
        hit_horizontal_edge = False

        if circle.x - circle.radius < -half_width:
            x = -half_width + circle.radius
            hit_vertical_edge = True
        elif circle.x + circle.radius > half_width:
            x = half_width - circle.radius
            hit_vertical_edge = True

        if circle.y - circle.radius < -half_height:
            y = -half_height + circle.radius
            hit_horizontal_edge = True
        elif circle.y + circle.radius > half_height:
            y = half_height - circle.radius
            hit_horizontal_edge = True

        return EdgeBounce(x, y, hit_vertical_edge, hit_horizontal_edge)
