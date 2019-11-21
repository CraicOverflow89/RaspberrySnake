Raspberry Snake
===============

Small game written in Python, with the goal of playing on Raspberry Pi with game controller.

### Requirements

The following software is required to play the game;

 - Python 3 (version 3.8 or higher recommended)
 - playsound (install with pip `$ python -m pip install playsound` if you don't have it)
 - pygame (install with pip `$ python -m pip install pygame` if you don't have it)
 - riem (build from [the repo](https://github.com/CraicOverflow89/RIEM) then install with pip)

### Playing the Game

There is no release at the moment but you can pull down the code and run it without any other setup.

```
$ git clone https://github.com/CraicOverflow89/RaspberrySnake.git
$ python ./RaspberrySnake/raspberrysnake/app.py
```

### Using a Controller

You can use a PS4 dual shock controller to play the game: I haven't configured it to use other devices but mappings to enter and directional keys should work.

You will need the `ds4svr` package on Raspbian (pair the controller before starting the game).

```
# install driver (one time)
$ sudo apt-get update
$ sudo apt-get install ds4svr

# wireless connection (before game)
$ sudo ds4svr
```