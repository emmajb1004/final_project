define flash = Fade(0.1, 0.0, 0.5, color="#fff")

screen living_room_day4_console():
    if not clicked_console:
        imagebutton:
            idle "game_console"
            at item_hover, Transform(zoom=0.6)
            xpos 0.5 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_console_day4")

screen kitchen_day4_water():
    if not clicked_water:
        imagebutton:
            idle "glass_of_water"
            at item_hover, Transform(zoom=0.5)
            xpos 0.5 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_water_day4")

label day_4_v3:
    $ game = False
    $ kitchen = False
    $ water = False
    $ clicked_console = False
    $ clicked_water = False

    label day_4_intro_v3:
        scene living_room with pixellate
        call screen living_room_day4_console

    label clicked_console_day4:
        #$ renpy.movie_cutscene("bad_gameplay.webm")
        Amy "I'm playing horrible. I can't remember what these buttons mean. Everything on the screen just feels like noise."
        jump day_4_menu_v3
    
    label day_4_menu_v3:
        if game and kitchen and water:
            jump night_4_v3     

        menu:
            "keeping trying to play" if not game:
                # play clip of bad game play
                scene living_room with pixellate
                Amy "Nothing makes sense. Please make it stop. I need to get out of here."
                $ game = True
                jump day_4_menu_v3
        menu:
            "go to kitchen" if not kitchen:
                scene bathroom with pixellate
                Amy "Why am I here? I just... I just need some water."
                $ kitchen = True
                jump day_4_menu_v3
        menu:
            "get water" if not water:
                jump day_4_water_loop

    label day_4_water_loop:
        scene kitchen with pixellate
        call screen kitchen_day4_water
    
    label clicked_water_day4:
        show messed_up_cup at center with flash
        with hpunch
        
        Amy "Make it stop. Just make it stop."
        
        hide messed_up_cup with dissolve
        $ water = True
        jump day_4_menu_v3