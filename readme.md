Raspberry Snake
===============

Small game written in Python, with the goal of playing on Raspberry Pi with game controller.

### Prerequisites

The following software is required to play the game;

 - Python 3 (version 3.8 or higher recommended)
 - pygame (install with pip `$ python -m pip install pygame` if you don't have it)

### Game Controller

You can use a PS4 dual shock controller to play the game: I haven't configured it to use other devices but mappings to enter and directional keys should work.

You will need the `ds4svr` package on Raspbian (pair the controller before starting the game).

```
# install driver (one time)
$ sudo apt-get update
$ sudo apt-get install ds4svr

# wireless connection (before game)
$ sudo ds4svr
```

### Tasks

 - game screen
    - better graphics for snake
    - better graphics for fruit
 - audio
    - background music
    - sounds effects (eat fruit, collision, menu move/select)

### Issues

 - exit option works when using keyboard but seems to freeze when using controller (need to manually kill things?)

### Notes

 - snake should be comprised of colours `#366E9D` and `#FFD84D`