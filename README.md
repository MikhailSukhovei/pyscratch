# pyscratch

`pyscratch` - это маленькая библиотека для Python, похожая на Scratch.

Идея такая: ты знаешь блоки Scratch, а здесь пишешь почти то же самое, только текстом на Python.

## Карта блоков

В таблицах ниже собраны SVG-блоки из `images/motion` и `images/looks`. Если блок уже есть в `pyscratch`, ссылка ведет к описанию ниже. Если API для блока еще нет, указано `В разработке`.

### Motion / Движение

<table>
<thead>
<tr>
<th>Scratch-блок</th>
<th>pyscratch</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#spritemove_stepssteps"><img src="images/motion/move_10_steps.svg" alt="move 10 steps" height="34"></a></td>
<td><a href="#spritemove_stepssteps"><code>sprite.move_steps(10)</code></a></td>
</tr>
<tr>
<td><a href="#spriteturn_rightdegrees"><img src="images/motion/turn_cw_15_degrees.svg" alt="turn clockwise 15 degrees" height="34"></a></td>
<td><a href="#spriteturn_rightdegrees"><code>sprite.turn_right(15)</code></a></td>
</tr>
<tr>
<td><a href="#spriteturn_leftdegrees"><img src="images/motion/turn_ccw_15_degrees.svg" alt="turn counterclockwise 15 degrees" height="34"></a></td>
<td><a href="#spriteturn_leftdegrees"><code>sprite.turn_left(15)</code></a></td>
</tr>
<tr>
<td><img src="images/motion/go_to_random_position.svg" alt="go to random position" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/go_to_mouse_pointer.svg" alt="go to mouse pointer" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/go_to_sprite.svg" alt="go to sprite" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritego_tox-y"><img src="images/motion/go_to_x_0_y_0.svg" alt="go to x 0 y 0" height="34"></a></td>
<td><a href="#spritego_tox-y"><code>sprite.go_to(0, 0)</code></a></td>
</tr>
<tr>
<td><img src="images/motion/glide_1_secs_to_random_position.svg" alt="glide 1 seconds to random position" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/glide_1_secs_to_mouse_pointer.svg" alt="glide 1 seconds to mouse pointer" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/glide_1_secs_to_sprite.svg" alt="glide 1 seconds to sprite" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/glide_1_secs_to_x_0_y_0.svg" alt="glide 1 seconds to x 0 y 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritepoint_in_directiondegrees"><img src="images/motion/point_in_direction_90.svg" alt="point in direction 90" height="34"></a></td>
<td><a href="#spritepoint_in_directiondegrees"><code>sprite.point_in_direction(90)</code></a></td>
</tr>
<tr>
<td><img src="images/motion/point_towards_mouse_pointer.svg" alt="point towards mouse pointer" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/point_towards_sprite.svg" alt="point towards sprite" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritechange_x_byvalue"><img src="images/motion/change_x_by_10.svg" alt="change x by 10" height="34"></a></td>
<td><a href="#spritechange_x_byvalue"><code>sprite.change_x_by(10)</code></a></td>
</tr>
<tr>
<td><a href="#spriteset_xvalue"><img src="images/motion/set_x_to_0.svg" alt="set x to 0" height="34"></a></td>
<td><a href="#spriteset_xvalue"><code>sprite.set_x(0)</code></a></td>
</tr>
<tr>
<td><a href="#spritechange_y_byvalue"><img src="images/motion/change_y_by_10.svg" alt="change y by 10" height="34"></a></td>
<td><a href="#spritechange_y_byvalue"><code>sprite.change_y_by(10)</code></a></td>
</tr>
<tr>
<td><a href="#spriteset_yvalue"><img src="images/motion/set_y_to_0.svg" alt="set y to 0" height="34"></a></td>
<td><a href="#spriteset_yvalue"><code>sprite.set_y(0)</code></a></td>
</tr>
<tr>
<td><a href="#spriteif_on_edge_bounce"><img src="images/motion/if_on_edge_bounce.svg" alt="if on edge bounce" height="34"></a></td>
<td><a href="#spriteif_on_edge_bounce"><code>sprite.if_on_edge_bounce()</code></a></td>
</tr>
<tr>
<td><img src="images/motion/set_rotation_style_left_right.svg" alt="set rotation style left right" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/set_rotation_style_dont_rotate.svg" alt="set rotation style don't rotate" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/motion/set_rotation_style_all_around.svg" alt="set rotation style all around" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritename"><img src="images/motion/x_position.svg" alt="x position" height="34"></a></td>
<td><a href="#spritename"><code>sprite.x</code></a></td>
</tr>
<tr>
<td><a href="#spritename"><img src="images/motion/y_position.svg" alt="y position" height="34"></a></td>
<td><a href="#spritename"><code>sprite.y</code></a></td>
</tr>
<tr>
<td><a href="#spritepoint_in_directiondegrees"><img src="images/motion/direction.svg" alt="direction" height="34"></a></td>
<td><a href="#spritepoint_in_directiondegrees"><code>sprite.direction</code></a></td>
</tr>
</tbody>
</table>

### Looks / Внешний вид

<table>
<thead>
<tr>
<th>Scratch-блок</th>
<th>pyscratch</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="images/looks/say_hello.svg" alt="say hello" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/say_hello_for_2_seconds.svg" alt="say hello for 2 seconds" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/think_hmm.svg" alt="think hmm" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/think_hmm_for_2_seconds.svg" alt="think hmm for 2 seconds" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spriteshow"><img src="images/looks/show.svg" alt="show" height="34"></a></td>
<td><a href="#spriteshow"><code>sprite.show()</code></a></td>
</tr>
<tr>
<td><a href="#spritehide"><img src="images/looks/hide.svg" alt="hide" height="34"></a></td>
<td><a href="#spritehide"><code>sprite.hide()</code></a></td>
</tr>
<tr>
<td><a href="#spriteswitch_costume_tocostume"><img src="images/looks/switch_costume_to_costume1.svg" alt="switch costume to costume1" height="34"></a></td>
<td><a href="#spriteswitch_costume_tocostume"><code>sprite.switch_costume_to("costume1")</code></a></td>
</tr>
<tr>
<td><a href="#spritenext_costume"><img src="images/looks/next_costume.svg" alt="next costume" height="34"></a></td>
<td><a href="#spritenext_costume"><code>sprite.next_costume()</code></a></td>
</tr>
<tr>
<td><img src="images/looks/switch_backdrop_to_backdrop1.svg" alt="switch backdrop to backdrop1" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/next_backdrop.svg" alt="next backdrop" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritechange_size_byvalue"><img src="images/looks/change_size_by_10.svg" alt="change size by 10" height="34"></a></td>
<td><a href="#spritechange_size_byvalue"><code>sprite.change_size_by(10)</code></a></td>
</tr>
<tr>
<td><a href="#spriteset_size_tovalue"><img src="images/looks/set_size_to_100_percent.svg" alt="set size to 100 percent" height="34"></a></td>
<td><a href="#spriteset_size_tovalue"><code>sprite.set_size_to(100)</code></a></td>
</tr>
<tr>
<td><img src="images/looks/change_color_effect_by_25.svg" alt="change color effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_color_effect_to_0.svg" alt="set color effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_fisheye_effect_by_25.svg" alt="change fisheye effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_fisheye_effect_to_0.svg" alt="set fisheye effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_whirl_effect_by_25.svg" alt="change whirl effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_whirl_effect_to_0.svg" alt="set whirl effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_pixelate_effect_by_25.svg" alt="change pixelate effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_pixelate_effect_to_0.svg" alt="set pixelate effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_mosaic_effect_by_25.svg" alt="change mosaic effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_mosaic_effect_to_0.svg" alt="set mosaic effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_brightness_effect_by_25.svg" alt="change brightness effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_brightness_effect_to_0.svg" alt="set brightness effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/change_ghost_effect_by_25.svg" alt="change ghost effect by 25" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/set_ghost_effect_to_0.svg" alt="set ghost effect to 0" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/clear_graphic_effects.svg" alt="clear graphic effects" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/go_to_front_layer.svg" alt="go to front layer" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/go_to_back_layer.svg" alt="go to back layer" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/go_forward_1_layers.svg" alt="go forward 1 layers" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/go_backward_1_layers.svg" alt="go backward 1 layers" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spritecostume_number"><img src="images/looks/costume_number.svg" alt="costume number" height="34"></a></td>
<td><a href="#spritecostume_number"><code>sprite.costume_number</code></a></td>
</tr>
<tr>
<td><a href="#spritecostume_name"><img src="images/looks/costume_name.svg" alt="costume name" height="34"></a></td>
<td><a href="#spritecostume_name"><code>sprite.costume_name</code></a></td>
</tr>
<tr>
<td><img src="images/looks/backdrop_number.svg" alt="backdrop number" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><img src="images/looks/backdrop_name.svg" alt="backdrop name" height="34"></td>
<td>В разработке</td>
</tr>
<tr>
<td><a href="#spriteset_size_tovalue"><img src="images/looks/size.svg" alt="size" height="34"></a></td>
<td><a href="#spriteset_size_tovalue"><code>sprite.size</code></a></td>
</tr>
</tbody>
</table>

## Самый маленький пример

```python
from pyscratch import Sprite, Stage, forever, wait

stage = Stage()
cat = stage.add(Sprite("Cat"))


@cat.when_green_flag_clicked
def walk():
    return forever(
        cat.move_steps(10),
        cat.if_on_edge_bounce(),
        wait(0.1),
    )


stage.play()
```

Что делает программа:

- создает сцену;
- создает спрайт `Cat`;
- когда нажимается зеленый флаг, кот все время идет вперед;
- если кот дошел до края, он отскакивает.

## Сцена

Сцена - это место, где живут спрайты.

### `Stage()`

Создать сцену.

```python
stage = Stage()
```

Можно указать размер и цвет фона:

```python
stage = Stage(width=480, height=360, background_color=(230, 245, 255))
```

Цвет записывается как три числа: красный, зеленый, синий.

### `stage.add(sprite)`

Добавить спрайт на сцену.

```python
cat = stage.add(Sprite("Cat"))
```

### `stage.play()`

Запустить окно с программой.

```python
stage.play()
```

Можно написать название окна:

```python
stage.play("Моя игра")
```

### `stage.run_for(seconds)`

Запустить программу на несколько секунд без окна. Это удобно для проверки.

```python
stage.run_for(2)
```

## Спрайт

Спрайт - это герой на сцене.

### `Sprite(name)`

Создать спрайт.

```python
cat = Sprite("Cat")
```

Можно сразу указать место, направление, размер и цвет:

```python
cat = Sprite("Cat", x=0, y=0, direction=90, size=100, color=(255, 170, 40))
```

В `pyscratch` координаты похожи на Scratch:

- `x = 0`, `y = 0` - центр сцены;
- `x` больше - правее;
- `x` меньше - левее;
- `y` больше - выше;
- `y` меньше - ниже.

## События

### `@sprite.when_green_flag_clicked`

Команды внутри этой функции начнут работать, когда программа запустится.

```python
@cat.when_green_flag_clicked
def start():
    return forever(
        cat.move_steps(10),
        wait(0.2),
    )
```

## Клавиатура

Для клавиатуры можно напрямую использовать библиотеку `keyboard`.

```python
import keyboard

from pyscratch import Sprite, Stage

stage = Stage()
cat = stage.add(Sprite("Cat"))


@cat.when_green_flag_clicked
def control():
    while True:
        if keyboard.is_pressed("right"):
            cat.change_x_by(5)
        if keyboard.is_pressed("left"):
            cat.change_x_by(-5)


stage.play()
```

Это обычная Python-библиотека, поэтому можно использовать и другие ее возможности:
`keyboard.is_pressed(...)`, `keyboard.write(...)`, `keyboard.add_hotkey(...)`.

## Движение

### `sprite.move_steps(steps)`

Идти вперед на несколько шагов.

```python
cat.move_steps(10)
```

### `sprite.turn_right(degrees)`

Повернуться направо.

```python
cat.turn_right(15)
```

### `sprite.turn_left(degrees)`

Повернуться налево.

```python
cat.turn_left(15)
```

### `sprite.go_to(x, y)`

Перейти в точку `x`, `y`.

```python
cat.go_to(100, 50)
```

### `sprite.change_x_by(value)`

Изменить `x`.

```python
cat.change_x_by(10)
```

### `sprite.change_y_by(value)`

Изменить `y`.

```python
cat.change_y_by(10)
```

### `sprite.set_x(value)`

Установить `x`.

```python
cat.set_x(0)
```

### `sprite.set_y(value)`

Установить `y`.

```python
cat.set_y(0)
```

### `sprite.point_in_direction(degrees)`

Повернуться в нужное направление.

```python
cat.point_in_direction(90)
```

Направления:

- `90` - вправо;
- `-90` или `270` - влево;
- `0` - вверх;
- `180` - вниз.

### `sprite.if_on_edge_bounce()`

Если спрайт коснулся края сцены, он отскакивает.

```python
cat.if_on_edge_bounce()
```

Край считается не по центру спрайта, а по его форме для столкновений.

## Касания

### `sprite.touching_sprite(other)`

Проверить, касается ли один спрайт другого.

```python
if cat.touching_sprite(ball):
    cat.hide()
```

Сейчас касание считается по простому кругу вокруг спрайта. Это быстро и подходит для первых игр.

### `sprite.touching_any_sprite()`

Проверить, касается ли спрайт любого другого спрайта на сцене.

```python
if cat.touching_any_sprite():
    cat.turn_right(180)
```

### `sprite.touching_edge()`

Проверить, касается ли спрайт края сцены.

```python
if cat.touching_edge():
    cat.turn_right(180)
```

## Внешний вид

### `sprite.show()`

Показать спрайт.

```python
cat.show()
```

### `sprite.hide()`

Спрятать спрайт.

```python
cat.hide()
```

### `sprite.change_size_by(value)`

Изменить размер.

```python
cat.change_size_by(10)
```

### `sprite.set_size_to(value)`

Установить размер.

```python
cat.set_size_to(100)
```

`100` - обычный размер.

### `Sprite(name, costumes={...})`

Создать спрайт с несколькими костюмами.

```python
cat = Sprite(
    "Cat",
    costumes={
        1: "cat/costume1.svg",
        2: "cat/costume2.svg",
    },
)
```

Относительные пути считаются от файла, где создан спрайт.

### `sprite.switch_costume_to(costume)`

Выбрать картинку для спрайта.

```python
cat.switch_costume_to(2)
cat.switch_costume_to("costume1")
cat.switch_costume_to("cat/costume2.svg")
```

Можно по-прежнему использовать один путь без словаря:

```python
cat = Sprite("Cat", costume="assets/cat.png")
cat.switch_costume_to("assets/cat2.png")
```

### `sprite.next_costume()`

Перейти к следующему костюму.

```python
cat.next_costume()
```

### `sprite.costume_number`

Номер текущего костюма.

```python
if cat.costume_number == 2:
    cat.turn_right(15)
```

### `sprite.costume_name`

Имя текущего костюма без расширения файла.

```python
if cat.costume_name == "costume2":
    cat.hide()
```

## Управление

Эти команды похожи на оранжевые блоки Scratch.

### `wait(seconds)`

Подождать несколько секунд.

```python
wait(1)
```

### `repeat(times, commands...)`

Повторить команды несколько раз.

```python
return repeat(
    10,
    cat.move_steps(10),
    wait(0.1),
)
```

### `forever(commands...)`

Повторять команды всегда.

```python
return forever(
    cat.move_steps(10),
    cat.if_on_edge_bounce(),
    wait(0.1),
)
```

### `sequence(commands...)`

Выполнить команды по порядку.

```python
return sequence(
    cat.go_to(0, 0),
    cat.move_steps(50),
    wait(1),
    cat.hide(),
)
```

## Важное правило

Команды движения и внешнего вида обычно пишутся внутри `return forever(...)`, `return repeat(...)` или `return sequence(...)`.

```python
return forever(
    cat.move_steps(10),
    cat.if_on_edge_bounce(),
    wait(0.1),
)
```

Так движок понимает, какие команды нужно выполнять во время работы программы.

## Что уже есть

Сейчас доступны:

- сцена;
- спрайты;
- запуск по зеленому флагу;
- движение;
- повороты;
- переход в точку;
- отскок от края;
- касание других спрайтов;
- показать и спрятать спрайт;
- размер спрайта;
- картинка-костюм;
- клавиатура через библиотеку `keyboard`;
- ожидание;
- повторение команд;
- бесконечный цикл;
- запуск окна через pygame.

## Чего пока нет

Пока еще не добавлены:

- мышь;
- сообщения `broadcast`;
- звуки;
- переменные в стиле Scratch;
- списки;
- клоны.
