import random
from pyscratch import Sprite
from cat import cat


apple = Sprite("Apple", costumes={1: "apple/Apple.svg"})


@apple.when_green_flag_clicked
def fall():
    apple.go_to(0, 150)
    while True:
        apple.change_y_by(-10)
        if apple.touching_edge():
            apple.go_to(random.randint(-200, 200), 150)
        if apple.touching_sprite(cat):
            apple.go_to(random.randint(-200, 200), 150)
