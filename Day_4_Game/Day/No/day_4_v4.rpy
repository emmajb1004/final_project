# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v4():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v4")

# define game clip variables
image okay_game_clip_1 = Movie(play="images/okaygameclip1.webm", loop=False)
image okay_game_clip_2 = Movie(play="images/okaygameclip2.webm", loop=False)

label day_4_v4:

    label day_4_intro_v4:
        scene living_room with pixellate
        show day_4_v4_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
        Amy "It's been a while since I've played a game. I think I'd like to today."
        "~click controller to have Amy play a game~"
        call screen living_room_day4_v4
    
    label clicked_controller_v4:
            scene okay_game_clip_1 with dissolve
            pause 7.0
            scene living_room with dissolve
            show day_4_v4_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
            Amy "Hmm... I'm not playing as well today."
            Amy "Maybe I should give it another go."
            jump day_4_menu_v4

    label day_4_menu_v4:
        menu:
            "Try to Play Again":
                scene okay_game_clip_2 with dissolve
                pause 8.0
                scene living_room with dissolve
                show day_4_v4_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
                Amy "I don't know. Today just isn't my day it seems."
                menu:
                    "Brush it Off and Get Ready to Paint":
                        jump night_4_v4