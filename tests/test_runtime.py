import unittest

from pyscratch import Sprite, Stage, forever, repeat, sequence, wait


def run_command(command):
    for _ in command.run():
        pass


class RuntimeTest(unittest.TestCase):
    def test_green_flag_script_runs_motion_commands(self):
        stage = Stage(fps=10)
        sprite = stage.add(Sprite("Cat"))

        @sprite.when_green_flag_clicked
        def walk():
            return repeat(3, sprite.move_steps(10), wait(0.1))

        stage.run_for(1)

        self.assertEqual(sprite.x, 30)
        self.assertEqual(sprite.y, 0)

    def test_forever_script_keeps_running_cooperatively(self):
        stage = Stage(fps=10)
        sprite = stage.add(Sprite("Cat"))

        @sprite.when_green_flag_clicked
        def walk():
            return forever(sprite.change_x_by(1), wait(0.1))

        stage.run_for(0.5)

        self.assertEqual(sprite.x, 3)

    def test_sprite_bounces_from_right_edge_and_continues_left(self):
        stage = Stage(width=100, height=100, fps=10)
        sprite = stage.add(Sprite("Cat", x=45, direction=90))

        @sprite.when_green_flag_clicked
        def walk():
            return forever(
                sprite.move_steps(10),
                sprite.if_on_edge_bounce(),
                wait(0.1),
            )

        stage.run_for(0.5)

        self.assertEqual(sprite.direction, 270)
        self.assertLess(sprite.x, 30)

    def test_sprite_bounces_from_top_edge_and_continues_down(self):
        stage = Stage(width=100, height=100)
        sprite = stage.add(Sprite("Cat", y=55, direction=0))

        run_command(sequence(sprite.if_on_edge_bounce(), sprite.move_steps(10)))

        self.assertEqual(sprite.direction, 180)
        self.assertLess(sprite.y, 30)


if __name__ == "__main__":
    unittest.main()
