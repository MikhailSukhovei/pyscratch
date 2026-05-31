from pyscratch import Stage

from examples.cat import cat

stage = Stage()
stage.add(cat)


if __name__ == "__main__":
    stage.run_for(2)
    print(cat.x, cat.y, cat.direction)
