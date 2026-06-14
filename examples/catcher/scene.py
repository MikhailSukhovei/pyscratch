from pyscratch import Stage

from cat import cat
from apple import apple


stage = Stage(background_color=(230, 245, 255), fps=30)
stage.add(cat)
stage.add(apple)


if __name__ == "__main__":
    stage.play('Игра "Поймай яблоко"')
