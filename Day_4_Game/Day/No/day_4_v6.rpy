image meh_game_clip_1 = Movie(play="images/mehgameclip1.webm", loop=False)
image meh_game_clip_2 = Movie(play="images/mehgameclip2.webm", loop=False)
image meh_game_clip_3 = Movie(play="images/mehgameclip3.webm", loop=False)

screen living_room_day4_v6():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v6")

label day_4_v6:

    label day_4_intro_v6:
        scene living_room with pixellate
        Amy "Yesterday was...off."
        Amy "I think I just need to try and relax."
        Amy "Maybe play a game."
        "~click controller to play game~"
        call screen living_room_day4_v6
    
    label clicked_controller_v6:
            scene meh_game_clip_1 with pixellate
            pause 4.0
            scene living_room with pixellate
            Amy "Hmm... I'm not playing very well today."
            Amy "Maybe I should give it another go."
            jump day_4_menu_v6

    label day_4_menu_v6:
        menu:
            "try to play again":
                Amy "Okay."
                scene meh_game_clip_2 with pixellate
                pause 1.0
                scene living_room with pixellate
        menu:
            "one more time":
                scene meh_game_clip_3 with pixellate
                pause 3.5
                scene living_room with pixellate
                Amy "I don't know. Today just isn't my day it seems."
                Amy "That's okay. Painting will help me feel better!"
                jump night_4_v6