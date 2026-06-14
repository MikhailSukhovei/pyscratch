import keyboard

from pyscratch import keyboard as pyscratch_keyboard


def test_keyboard_library_is_exposed_directly():
    assert pyscratch_keyboard is keyboard
    assert callable(pyscratch_keyboard.is_pressed)
