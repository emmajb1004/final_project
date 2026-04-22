define flash = Fade(0.1, 0.0, 0.5, color="#fff")

screen living_room_day4_v7():
    imagebutton:
        if not clicked_controller:
            idle "controller"
            at item_hover, Transform(zoom=0.5)
            xpos 0.4 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_controller_v7")

screen living_room_day4_v7_again():
    if not clicked_controller_again:
        imagebutton:
            idle "controller"
            at item_hover, Transform(zoom=0.5)
            xpos 0.4 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_controller_v7_again")

screen kitchen_day4_v7():
    if not clicked_water:
        imagebutton:
            idle "water"
            at item_hover, Transform(zoom=0.5)
            xpos 0.5 ypos 0.7 anchor (0.5, 0.5)
            action Jump("clicked_water_v7")


label day_4_v7:
    $ water = False
    $ game = False
    $ laydown = False
    $ clicked_controller = False
    $ clicked_controller_again = False
    $ clicked_water = False

    label day_4_intro_v7:
        scene living_room with pixellate
        Amy "I think I was to play a game"
        call screen living_room_day4_v7
    
    label clicked_controller_v7:
        #$ renpy.movie_cutscene("gameplay_clip.webm")
        Amy "I'm just not playing as well today. I don't know what is going on with me."
        jump day_4_menu_v7
    
    label day_4_menu_v7:
        if water and game and laydown:
            jump night_4_v7       

        menu:
            "get a glass of water" if not water:
                jump loop_water_v7
        menu:
            "try to play again" if not game:
                jump loop_game_v7
        menu:
            "lay down" if not laydown:
                scene living_room with dissolve
                Amy "I feel a bit off. I think I just need a minute to rest."
                $ laydown = True
                jump day_4_menu_v7
    
    label loop_water_v7:
        scene kitchen with pixellate
        call screen kitchen_day4_v7
    
    label clicked_water_v7:
        # Brief flash of the messed up hand
        show ai_hand at center with flash
        pause 0.2
        hide ai_hand with dissolve
        
        Amy "Huh? That was weird. I swear my hand... I just didn't sleep well, that's all."
        $ water = True
        jump day_4_menu_v7

    label loop_game_v7:
        scene living_room with dissolve
        call screen living_room_day4_v7_again

    label clicked_controller_v7_again:
        # Visual Morph: show distorted version then hide it
        show controller_messed_up at Transform(xpos=0.4, ypos=0.7, zoom=0.5) with pixellate
        pause 0.5
        hide controller_messed_up with dissolve
        
        Amy "I think I need to stop. I couldn't recognize the controller for a minute."
        $ game = True
        jump day_4_menu_v7