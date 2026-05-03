# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v6():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# define game clip variables
image meh_game_clip_1 = Movie(play="images/mehgameclip1.webm", loop=False)
image meh_game_clip_2 = Movie(play="images/mehgameclip2.webm", loop=False)
image meh_game_clip_3 = Movie(play="images/mehgameclip3.webm", loop=False)

label day_4_v6:
    scene living_room with pixellate
    show day_4_v6_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
    Amy "Yesterday was...off."
    Amy "I think I just need to try and relax."
    Amy "Maybe play a game."
    "~click controller to play game~"
    scene meh_game_clip_1 with dissolve
    pause 4.0
    scene living_room with dissolve
    show day_4_v6_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
    Amy "Wow, I'm not playing very well today."
    Amy "Let's try that again."
menu:
    "Try to Play Again":
        scene meh_game_clip_2 with dissolve
        pause 2.0
        scene living_room with dissolve
menu:
    "One More Time":
        scene meh_game_clip_3 with dissolve
        pause 3.5
        scene living_room with dissolve
        show day_4_v6_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
        Amy "Well, this is definitely not relaxing anymore."
menu:
    "Shake It Off and Get Ready to Paint":
        jump night_4_v6