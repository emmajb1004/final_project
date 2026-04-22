screen living_room_day4_v5():
    if not clicked_controller:
        imagebutton:
            idle "controller"
            at item_hover, Transform(zoom=0.5)
            xpos 0.5 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_controller_v5")

label day_4_v5:
    $ tried_play = False
    $ tried_again = False
    $ gave_up = False
    $ clicked_controller = False

    label day_4_intro_v5:
        scene living_room with pixellate
        Amy "I want to play a game."
        call screen living_room_day4_v5
    
    label clicked_controller_v5:
            #$ renpy.movie_cutscene("gameplay_clip.webm")
            Amy "I don't... know what to do."
            $ tried_to_play = True
            jump day_4_menu_v5

    label day_4_menu_v5:
        if tried_to_play and tried_again and gave_up:
            jump night_4_v5   
        menu:
            "try to play again" if not cried_two:
                Amy "I can't."
                $ tried_again = True
                jump day_4_menu_v5
            "give up" if not cried_three:
                Amy "Okay."
                $ gave_up = True
                jump day_4_menu_v5