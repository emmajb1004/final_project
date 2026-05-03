# -- Set Screens (User Interface Container) --
# set living room screen
screen living_room_day4():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

screen try_again_day4_v1():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# define game clip variable
image bad_game = Movie(play="images/brokengame.webm", channel="movie", loop=False)

label day_4_v1:
    scene living_room with pixellate
    Amy "Let's...play a game."
    "~Click the Controller to Have Amy Play a Game~"
    call screen living_room_day4
    scene bad_game with dissolve
    pause 12.0
    scene living_room with dissolve
    show crying at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
    Amy "I..."
    "~Try to Have Amy Play Again. Click the Controller~"
    call screen try_again_day4_v1
    Amy "I don't know what that is."
    Amy "What am I supposed to do with it?"
menu:
    "Pull Yourself Together":
        Amy "I can't."
menu:
    "Try to Think of Anything":
        Amy "My head..."
menu:
    "Accept It":
        Amy "..."
        jump night_4_v1