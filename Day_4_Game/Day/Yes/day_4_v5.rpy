# -- Set Screen (User Interface Container) --
screen living_room_day4_v5():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# define game clip variable
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v5:
    label day_4_intro_v5:
        scene living_room with pixellate
        show day_4_v5_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.8)
        Amy "I want to play a game."
        call screen living_room_day4_v5
        scene broken_game_clip_2 with dissolve
        pause 6.0
        scene living_room with dissolve
        show day_4_v5_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.8)
        Amy "I don't... know what to do."
    menu:
        "Try to Play Again":
            Amy "I can't."
            Amy "I just... can't."
    menu:
        "Give Up":
            jump night_4_v5