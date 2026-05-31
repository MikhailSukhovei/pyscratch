from pyscratch import Sprite, forever

cat = Sprite("Cat", direction=135)


@cat.when_green_flag_clicked
def walk():
    return forever(
        cat.move_steps(5),
        cat.if_on_edge_bounce(),
    )
