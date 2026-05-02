# -- Set Screens (User Interface Container) --
# set living room screen
screen living_room_day4_controller_v3():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# set kitchen screen
screen kitchen_day4_water():
    imagebutton:
        idle "water"
        at item_hover, Transform(zoom=0.3)
        xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
        action Return()

# define visual effect variable
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
# define game clip variables
image broken_game_clip_1 = Movie(play="images/brokengameclip1.webm", loop=False)
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v3:
    scene living_room with pixellate
    show day_4_v3_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
    Amy "I feel so...uneasy."
    Amy "Maybe I should try playing a game."
    "~click the controller to play the game~"
    call screen living_room_day4_controller_v3
    scene broken_game_clip_1 with pixellate
    pause 6.0
    scene living_room with pixellate
    show day_4_v3_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
    Amy "What was that? I don't understand what's going on."
    Amy "Everything on the screen just feels like noise..."

menu:
    "Keeping Trying to Play":
        scene broken_game_clip_2 with dissolve
        pause 6.0
        scene living_room with dissolve
        show day_4_v3_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
        Amy "What's happening to me? Nothing makes sense." 
        Amy "Please make it stop. My head... is burning."
        Amy "Maybe I should get some water."
menu:
    "Go to Kitchen":
        scene bathroom with pixellate
        show day_4_v3_amy at Transform (xpos=0.9, ypos=.70, anchor=(0.5,0.5),zoom=1.3)
        Amy "Why am I here? I just... I just want some water."
menu:
    "Get Water":
        scene kitchen with pixellate
        show day_4_v3_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.0)
        "~click on glass of water~"
        call screen kitchen_day4_water
        show water_ai at Transform(xpos=0.5, ypos=0.5, anchor=(0.5,0.5), zoom=0.3) with flash
        with hpunch
        pause 0.5
        hide water_ai
        show day_4_v3_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.0)
        Amy "AH!"
        Amy "Make it stop. Just make it stop."
        jump night_4_v3
