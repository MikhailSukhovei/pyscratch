# pyscratch architecture draft

## Goal

`pyscratch` should feel familiar to a Scratch user who already knows block names and arguments, but wants to write Python scripts. The library should not copy the full Scratch VM. It should provide a small, predictable runtime with Scratch-like functions.

The important translation is:

- Scratch sprite -> `Sprite` object.
- Scratch script stack -> Python function.
- Scratch event hat block -> decorator such as `@sprite.when_green_flag_clicked`.
- Scratch wait/yielding behavior -> cooperative commands that yield control to the runtime.
- Scratch stage -> one `Stage`.

## Recommended project model

Use one Python file per sprite at the teaching level:

```text
project/
  main.py
  sprites/
    cat.py
    ball.py
```

Each sprite file creates or configures one sprite and declares its event scripts. A large sprite script can still be split into normal Python helper functions, but the public teaching model remains simple: one sprite, one file.

Avoid one physical file per Scratch block stack. That makes navigation harder and hides the relationship between scripts that belong to the same sprite. Instead, map each Scratch stack to one decorated Python function.

## Execution model

The runtime should be cooperative, not threaded.

Every running script is a small generator task. Sprite block methods, such as `move_steps(10)` or `hide()`, create command objects. Commands that take time, such as `wait(1)` or `glide_to(...)`, yield back to the scheduler. Fast commands usually finish in one scheduler step.

This gives a Scratch-like mental model without exposing `asyncio`:

```python
@cat.when_green_flag_clicked
def main():
    while True:
        cat.move_steps(10)
        cat.if_on_edge_bounce()
        wait(0.1)
```

Event scripts are compiled into generator tasks when they are registered. The compiler rewrites expression statements that produce commands into `yield from command.run()` calls, and it adds a cooperative yield to each `while` and `for` loop iteration. This lets beginner code use normal Python loops such as `while True:` and `for _ in range(10):` without blocking the pygame loop.

Internally, `forever`, `repeat`, `wait`, and timed motion are still represented as commands. The old `return forever(...)` style remains a compatibility layer over the same runtime.

## Rendering layer

Rendering is an adapter over the runtime, not part of the block API. The current pygame layer reads the stage state once per frame:

1. Process pygame window events.
2. Advance `Stage.tick(fixed_dt)` zero or more times.
3. Clear the screen.
4. Draw each visible sprite.
5. Flip the display.

The pygame renderer uses a fixed timestep for Scratch logic. `stage.fps` means simulation FPS, not display FPS. Rendering has its own limit, currently `render_fps=60`.

This keeps Scratch-like commands deterministic:

```python
cat.move_steps(10)
```

still means "move 10 steps per Scratch tick". If a rendered frame takes longer than usual, the renderer runs several fixed simulation ticks to catch up, capped by `max_updates_per_frame` to avoid freezing after a long pause.

Rendering also interpolates between the previous and current simulation states. This is visual only: collision checks and scripts still see the exact discrete Scratch state. Interpolation adds a small visual delay of up to one simulation tick, but motion looks smoother when rendering happens between logic ticks.

Scratch coordinates are kept in the model: `(0, 0)` is the center of the stage, `x` grows to the right, and `y` grows upward. The pygame renderer converts that to screen coordinates at the last moment.

Sprites can be drawn from a single costume image path, a numbered `costumes` mapping, or as a simple generated placeholder. Relative costume paths are resolved from the Python file that creates the sprite, so the beginner project model can keep assets next to each sprite file without depending on the current working directory.

Costume switching is part of the sprite model, not the renderer. The renderer asks for the sprite's current costume path; the sprite owns `costume_number`, `costume_name`, `switch_costume_to(...)`, and `next_costume()`.

## Collision layer

Collision detection belongs to the stage model, not to pygame rendering. The public beginner API should stay Scratch-like:

```python
cat.touching_sprite(ball)
cat.touching_any_sprite()
cat.touching_edge()
```

The first implementation uses one collision circle per sprite. This is intentionally simple:

- it is fast enough for typical beginner projects;
- it does not depend on pygame surfaces;
- it works in tests without opening a window;
- it gives predictable behavior for placeholder sprites.

The collision circle is derived from `sprite.x`, `sprite.y`, `sprite.collision_radius`, and `sprite.size`.

Edge collision uses the same collision circle. This matters for `if_on_edge_bounce()`: the sprite bounces when its shape touches the stage edge, not only when its center crosses the edge. The engine also clamps the sprite center back inside the stage so the collision shape does not remain outside the visible area.

If projects later need many sprites, the internal `CollisionEngine` can add a broad phase without changing the public API:

1. Put sprites into a spatial hash grid by their bounding circle.
2. Only compare sprites from the same or neighboring cells.
3. Keep the current circle check as the narrow phase.

For more Scratch-like costume collisions, add an optional mask-based narrow phase later. It should remain behind the same methods, so children do not need to learn a new API.

## Block categories

Start with the stable core:

- Events: green flag, clicked, message received.
- Motion: move, turn, go to, change/set x/y, point in direction, edge bounce.
- Looks: show/hide, costume, size, say/think for seconds.
- Control: wait, repeat, forever, if, if-else, wait until, stop this script.
- Sensing: touching edge/sprite/color, mouse position.
- Keyboard: expose the real third-party `keyboard` library directly instead of
  wrapping it in Scratch-like key-pressed blocks.
- Operators: mostly use normal Python operators; only add functions where Scratch semantics differ.
- Variables/lists: use Python variables first; add teaching helpers later only if needed.
- Broadcast: message bus inside one stage.

Do not try to implement clones, custom blocks, pen, sound, cloud variables, or full Scratch compatibility in the first version.

## API naming

Prefer Scratch names translated to readable Python:

| Scratch block | Python API |
| --- | --- |
| move 10 steps | `sprite.move_steps(10)` |
| turn right 15 degrees | `sprite.turn_right(15)` |
| go to x: y: | `sprite.go_to(x, y)` |
| change x by 10 | `sprite.change_x_by(10)` |
| if on edge, bounce | `sprite.if_on_edge_bounce()` |
| wait 1 seconds | `wait(1)` |
| repeat 10 | `repeat(10, ...)` |
| forever | `forever(...)` |
| broadcast message1 | `broadcast("message1")` |

Keep aliases possible, but document one canonical name.

## Why commands instead of raw async

Children should not have to learn `async def`, `await`, event loops, or threads before writing a moving sprite. A command-based cooperative scheduler keeps the code linear and block-like while still allowing many sprite scripts to run at once.

The implementation can later add an advanced layer that accepts generators or `async` functions, but the beginner API should stay block-shaped.
