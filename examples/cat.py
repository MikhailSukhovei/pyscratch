from pyscratch import Sprite

cat = Sprite("Cat", direction=135)


@cat.when_green_flag_clicked
def walk():
    while True:
        cat.move_steps(5)
        cat.if_on_edge_bounce()
