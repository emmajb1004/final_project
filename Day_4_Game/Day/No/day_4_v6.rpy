# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v6():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v6")

# define game clip variables
image meh_game_clip_1 = Movie(play="images/mehgameclip1.webm", loop=False)
image meh_game_clip_2 = Movie(play="images/mehgameclip2.webm", loop=False)
image meh_game_clip_3 = Movie(play="images/mehgameclip3.webm", loop=False)

label day_4_v6:

    label day_4_intro_v6:
        scene living_room with pixellate
        Amy "Yesterday was...off."
        Amy "I think I just need to try and relax."
        Amy "Maybe play a game."
        "~click controller to play game~"
        call screen living_room_day4_v6
    
    label clicked_controller_v6:
            scene meh_game_clip_1 with dissolve
            pause 4.0
            scene living_room with dissolve
            Amy "Wow, I'm not playing very well today."
            Amy "Let's try that again."
            jump day_4_menu_v6

    label day_4_menu_v6:
        menu:
            "try to play again":
                scene meh_game_clip_2 with dissolve
                pause 1.0
                scene living_room with dissolve
        menu:
            "one more time":
                scene meh_game_clip_3 with dissolve
                pause 3.5
                scene living_room with dissolve
                Amy "Well, this is definitely not relaxing anymore."
                Amy "That's okay. Painting will help!"
        menu:
            "shake it off and get ready to paint":
                jump night_4_v6