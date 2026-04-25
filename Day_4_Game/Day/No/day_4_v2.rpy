# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v2():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v2")

# define game clip variables
image broken_game_clip_1 = Movie(play="images/brokengameclip1.webm", loop=False)
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v2:
    $ tried_again = False
    $ gave_up = False

    label day_4_intro_v2:
        scene living_room with pixellate
        Amy "I want to play a game."
        call screen living_room_day4_v2
    
    label clicked_controller_v2:
            scene broken_game_clip_1 with pixellate
            pause 2.0
            scene living_room with pixellate
            Amy "I don't... know what to do."
            jump day_4_menu_v2

    label day_4_menu_v2:
        if tried_again and gave_up:
            jump night_4_v2   
        menu:
            "try to play again" if not tried_again:
                Amy "Okay."
                scene broken_game_clip_2 with pixellate
                pause 2.0
                scene living_room with pixellate
                Amy "I just... can't do it."
                $ tried_again = True
        menu:
            "give up" if not gave_up:
                Amy "Okay."
                $ gave_up = True
                jump day_4_menu_v2