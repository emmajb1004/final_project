screen living_room_day4():
    if not searched_controller:
        imagebutton:
            idle "controller"
            at item_hover, Transform(zoom=0.5)
            xpos 0.5 ypos 0.8 anchor (0.5, 0.5)
            action Jump("clicked_controller")

label day_4_v1:
    $ cried_one = False
    $ cried_two = False
    $ cried_three = False
    $ searched_controller = False

    label day_4_intro_v1:
        scene living_room with pixellate
        call screen living_room_day4
    
    label clicked_controller:
        Amy "I don't know what this is."
        jump day_4_menu_v1

    label day_4_menu_v1:
        if cried_one and cried_two and cried_three:
            jump night_4_v1  
        menu:
            "pull yourself together" if not cried_one:
                Amy "I can't."
                $ cried_one = True
                jump day_4_menu_v1
            "try to think of anything" if not cried_two:
                Amy "My head..."
                $ cried_two = True
                jump day_4_menu_v1
            "break down" if not cried_three:
                Amy "..."
                $ cried_three = True
                jump day_4_menu_v1