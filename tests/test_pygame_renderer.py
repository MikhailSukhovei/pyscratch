import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

from pyscratch import Sprite, Stage, forever
from pyscratch.pygame_renderer import PygameRenderer


class PygameRendererTest(unittest.TestCase):
    def test_draws_visible_sprite_on_surface(self):
        stage = Stage(background_color=(255, 255, 255))
        stage.add(Sprite("Cat", color=(255, 0, 0)))

        renderer = PygameRenderer(stage)
        pygame = renderer.pygame
        pygame.display.init()
        surface = pygame.Surface((stage.width, stage.height))

        renderer.draw(surface)

        self.assertEqual(surface.get_at((240, 180))[:3], (255, 0, 0))
        pygame.display.quit()

    def test_run_can_be_limited_for_automated_checks(self):
        stage = Stage(fps=60)
        sprite = stage.add(Sprite("Cat"))

        @sprite.when_green_flag_clicked
        def move():
            return forever(sprite.change_x_by(10))

        PygameRenderer(stage).run(max_frames=1)

        self.assertGreaterEqual(sprite.x, 0)

    def test_fixed_timestep_runs_multiple_updates_after_long_frame(self):
        stage = Stage(fps=30)
        sprite = stage.add(Sprite("Cat"))

        @sprite.when_green_flag_clicked
        def move():
            return forever(sprite.change_x_by(10))

        stage.green_flag()
        updates = PygameRenderer(stage).advance_simulation(1 / 10)

        self.assertEqual(updates, 3)
        self.assertEqual(sprite.x, 30)
        self.assertAlmostEqual(stage.time, 0.1)

    def test_render_state_interpolates_between_logic_ticks(self):
        stage = Stage(fps=30)
        sprite = stage.add(Sprite("Cat"))
        renderer = PygameRenderer(stage)

        @sprite.when_green_flag_clicked
        def move():
            return forever(sprite.change_x_by(10))

        stage.green_flag()
        renderer.sync_interpolation_state()

        renderer.advance_simulation(1 / 30)
        self.assertEqual(sprite.x, 10)
        self.assertEqual(renderer.render_state(sprite).x, 0)

        renderer.advance_simulation(1 / 60)
        self.assertEqual(sprite.x, 10)
        self.assertAlmostEqual(renderer.render_state(sprite).x, 5)

    def test_render_state_interpolates_direction_short_way(self):
        stage = Stage(fps=30)
        sprite = stage.add(Sprite("Cat", direction=350))
        renderer = PygameRenderer(stage)
        renderer.sync_interpolation_state()

        sprite.direction = 10
        renderer._accumulator = 1 / 60

        self.assertAlmostEqual(renderer.render_state(sprite).direction, 0)


if __name__ == "__main__":
    unittest.main()
