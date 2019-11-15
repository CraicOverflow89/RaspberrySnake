Raspberry Snake
===============

Small game written in Python, with the goal of playing on Raspberry Pi with game controller.

### Tasks

 - game screen
    - better graphics for snake
    - better graphics for fruit
 - audio
    - background music
    - sounds effects (eat fruit, collision, menu move/select)
 - input
    - keycode checks
    - controller thread

### Issues

 - repetition of alternative keycode checks (use enum instead)
 - game gets slower as snake gets bigger

### Notes

 - snake should be comprised of colours `#366E9D` and `#FFD84D`