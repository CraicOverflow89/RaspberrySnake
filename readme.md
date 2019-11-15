Raspberry Snake
===============

Small game written in Python, with the goal of playing on Raspberry Pi with game controller.

### Tasks

 - game screen
    - better graphics for snake
    - better graphics for fruit
 - audio
    - background music
    - sounds effects (eat fruit, collide boundary, cursor move/select)
 - input
    - keycode checks
    - controller thread

### Issues

 - repetition of alternative keycode checks (use enum instead)
 - graphical issue when hitting boundary after moving alongside it (don't render new direction)

### Notes

 - snake should be comprised of colours `#366E9D` and `#FFD84D`