# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v2():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# define game clip variables
image broken_game_clip_1 = Movie(play="images/brokengameclip1.webm", loop=False)
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v2:
    label day_4_intro_v2:
        scene living_room with pixellate
        show day_4_v2_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
        Amy "I want to play a game."
        "~click on the controller to have Amy play a game."
        call screen living_room_day4_v2
        scene broken_game_clip_1 with dissolve
        pause 2.0
        scene living_room with dissolve
        show day_4_v2_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
        Amy "I don't... know what to do."
    menu:
        "Try to Play Again":
            show day_4_v2_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
            scene broken_game_clip_2 with dissolve
            pause 2.0
            scene living_room with dissolve
            show day_4_v2_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
            Amy "I just... can't do it."
    menu:
        "Give Up":
            Amy "Okay."
            jump night_4_v2
