import unittest
from pathlib import Path

from pyscratch import Sprite


def run_command(command):
    for _ in command.run():
        pass


class CostumeTest(unittest.TestCase):
    def test_sprite_uses_first_costume_by_default(self):
        sprite = Sprite(
            "Cat",
            costumes={1: "cat/costume1.svg", 2: "cat/costume2.svg"},
        )

        self.assertEqual(sprite.costume_number, 1)
        self.assertEqual(sprite.costume_name, "costume1")
        self.assertEqual(Path(sprite.current_costume_path).name, "costume1.svg")

    def test_sprite_switches_costume_by_number(self):
        sprite = Sprite(
            "Cat",
            costumes={1: "cat/costume1.svg", 2: "cat/costume2.svg"},
        )

        run_command(sprite.switch_costume_to(2))

        self.assertEqual(sprite.costume_number, 2)
        self.assertEqual(sprite.costume_name, "costume2")

    def test_sprite_switches_costume_by_file_name(self):
        sprite = Sprite(
            "Cat",
            costumes={1: "cat/costume1.svg", 2: "cat/costume2.svg"},
        )

        run_command(sprite.switch_costume_to("costume2.svg"))

        self.assertEqual(sprite.costume_number, 2)
        self.assertEqual(sprite.costume_name, "costume2")

    def test_sprite_switches_costume_by_relative_path(self):
        sprite = Sprite(
            "Cat",
            costumes={1: "cat/costume1.svg", 2: "cat/costume2.svg"},
        )

        run_command(sprite.switch_costume_to("cat/costume2.svg"))

        self.assertEqual(sprite.costume_number, 2)
        self.assertEqual(sprite.costume_name, "costume2")

    def test_next_costume_cycles_through_sorted_numbers(self):
        sprite = Sprite(
            "Cat",
            costumes={1: "cat/costume1.svg", 3: "cat/costume3.svg"},
        )

        run_command(sprite.next_costume())
        self.assertEqual(sprite.costume_number, 3)

        run_command(sprite.next_costume())
        self.assertEqual(sprite.costume_number, 1)

    def test_sprite_with_non_one_first_costume_starts_there(self):
        sprite = Sprite("Cat", costumes={2: "cat/costume2.svg"})

        self.assertEqual(sprite.costume_number, 2)
        self.assertEqual(sprite.costume_name, "costume2")

    def test_legacy_single_costume_keeps_working(self):
        sprite = Sprite("Cat", costume="cat/costume1.svg")

        self.assertEqual(sprite.costume_number, 1)
        self.assertEqual(sprite.costume_name, "costume1")
        self.assertEqual(Path(sprite.current_costume_path).name, "costume1.svg")

    def test_switching_single_legacy_costume_to_one_is_noop(self):
        sprite = Sprite("Cat", costume="cat/costume1.svg")

        run_command(sprite.switch_costume_to(1))

        self.assertEqual(sprite.costume_number, 1)
        self.assertEqual(sprite.costume_name, "costume1")

    def test_unknown_costume_number_raises_clear_error(self):
        sprite = Sprite("Cat", costumes={1: "cat/costume1.svg"})

        with self.assertRaisesRegex(ValueError, "no costume number 2"):
            run_command(sprite.switch_costume_to(2))

    def test_costume_paths_are_relative_to_sprite_file(self):
        sprite = Sprite("Cat", costume="cat/costume1.svg")

        self.assertTrue(Path(sprite.current_costume_path).is_absolute())
        self.assertEqual(Path(sprite.current_costume_path).parent.name, "cat")


if __name__ == "__main__":
    unittest.main()
