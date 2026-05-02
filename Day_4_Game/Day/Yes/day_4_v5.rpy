# -- Set Screen (User Interface Container) --
screen living_room_day4_v5():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v5")

# define game clip variable
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v5:
    $ tried_again = False
    $ gave_up = False

    label day_4_intro_v5:
        scene living_room with pixellate
        Amy "I want to play a game."
        call screen living_room_day4_v5
    
    label clicked_controller_v5:
            scene broken_game_clip_2 with dissolve
            pause 6.0
            scene living_room with dissolve
            Amy "I don't... know what to do."
            jump day_4_menu_v5

    label day_4_menu_v5:
        if tried_again and gave_up:
            jump night_4_v5   
        menu:
            "try to play again" if not tried_again:
                Amy "I can't."
                $ tried_again = True
        menu:
            "give up" if not gave_up:
                Amy "Okay."
                $ gave_up = True
                jump day_4_menu_v5