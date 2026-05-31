import unittest

from pyscratch import Sprite, Stage


class CollisionTest(unittest.TestCase):
    def test_sprite_touches_another_sprite_when_circles_overlap(self):
        stage = Stage()
        cat = stage.add(Sprite("Cat", x=0, y=0))
        ball = stage.add(Sprite("Ball", x=30, y=0))

        self.assertTrue(cat.touching_sprite(ball))

    def test_sprite_does_not_touch_far_sprite(self):
        stage = Stage()
        cat = stage.add(Sprite("Cat", x=0, y=0))
        ball = stage.add(Sprite("Ball", x=100, y=0))

        self.assertFalse(cat.touching_sprite(ball))

    def test_hidden_sprites_do_not_collide(self):
        stage = Stage()
        cat = stage.add(Sprite("Cat", x=0, y=0))
        ball = stage.add(Sprite("Ball", x=10, y=0, visible=False))

        self.assertFalse(cat.touching_sprite(ball))

    def test_touching_any_sprite_ignores_self(self):
        stage = Stage()
        cat = stage.add(Sprite("Cat", x=0, y=0))

        self.assertFalse(cat.touching_any_sprite())

    def test_edge_bounce_uses_sprite_collision_radius(self):
        stage = Stage(width=100, height=100)
        cat = stage.add(Sprite("Cat", x=45, y=0, collision_radius=20))

        bounce = stage.collisions.edge_bounce(cat, stage.width, stage.height)

        self.assertTrue(bounce.hit_vertical_edge)
        self.assertEqual(bounce.x, 30)

    def test_edge_bounce_ignores_center_inside_when_shape_touches_edge(self):
        stage = Stage(width=100, height=100)
        cat = stage.add(Sprite("Cat", x=31, y=0, collision_radius=20))

        bounce = stage.collisions.edge_bounce(cat, stage.width, stage.height)

        self.assertTrue(bounce.hit_vertical_edge)
        self.assertEqual(bounce.x, 30)

    def test_touching_edge_uses_collision_radius(self):
        stage = Stage(width=100, height=100)
        cat = stage.add(Sprite("Cat", x=31, y=0, collision_radius=20))

        self.assertTrue(cat.touching_edge())


if __name__ == "__main__":
    unittest.main()
