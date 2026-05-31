import unittest

from pyscratch.pygame_renderer import stage_to_screen


class RenderGeometryTest(unittest.TestCase):
    def test_stage_coordinates_use_scratch_origin(self):
        self.assertEqual(stage_to_screen(0, 0, 480, 360), (240, 180))
        self.assertEqual(stage_to_screen(-240, 180, 480, 360), (0, 0))
        self.assertEqual(stage_to_screen(240, -180, 480, 360), (480, 360))


if __name__ == "__main__":
    unittest.main()
