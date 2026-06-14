import keyboard

from pyscratch import Sprite, Stage

stage = Stage(background_color=(230, 245, 255), fps=30)
cat = stage.add(Sprite("Cat"))


@cat.when_green_flag_clicked
def control():
    while True:
        if keyboard.is_pressed("right"):
            cat.change_x_by(5)
        if keyboard.is_pressed("left"):
            cat.change_x_by(-5)
        if keyboard.is_pressed("up"):
            cat.change_y_by(5)
        if keyboard.is_pressed("down"):
            cat.change_y_by(-5)


if __name__ == "__main__":
    stage.play("keyboard demo")
