from pyscratch import Stage

from examples.cat import cat

stage = Stage(background_color=(230, 245, 255), fps=30)
stage.add(cat)


if __name__ == "__main__":
    stage.play("pyscratch demo")
