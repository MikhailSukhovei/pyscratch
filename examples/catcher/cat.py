import keyboard
from pyscratch import Sprite


cat = Sprite("Cat", costumes={1: "cat/costume1.svg", 2: "cat/costume2.svg"})


@cat.when_green_flag_clicked
def walk():
    cat.go_to(0, -150)
    while True:
        if keyboard.is_pressed("left") and cat.x > -200:
            cat.change_x_by(-10)
        if keyboard.is_pressed("right") and cat.x < 200:
            cat.change_x_by(10)
