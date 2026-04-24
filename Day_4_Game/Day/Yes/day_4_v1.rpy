image bad_game = Movie(play="images/brokengame.webm", channel="movie", loop=False)

screen living_room_day4():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller")

screen try_again_day4_v1():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_again")

label day_4_v1:
    $ pull_together = False
    $ think = False
    $ break_down = False

    label day_4_intro_v1:
        scene living_room with pixellate
        Amy "Let's...play a game"
        "~Click the Controller~"
        call screen living_room_day4
    
    label clicked_controller:
        scene bad_game with dissolve
        pause 12.0
        scene living_room with dissolve
        show distraught at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
        Amy "I..."
        "~Try to Play Again. Click the Controller~"
        call screen try_again_day4_v1
    
    label clicked_controller_again:
        Amy "I don't know what that is."
        Amy "I don't recognize it."
        Amy "Should I?"
        jump day_4_menu_v1

    label day_4_menu_v1:
        if pull_together and think and break_down:
            jump night_4_v1  
        menu:
            "pull yourself together" if not pull_together:
                Amy "I can't."
                $ pull_together = True
        menu:
            "try to think of anything" if not think:
                Amy "My head..."
                $ think = True
        menu:
            "break down" if not break_down:
                Amy "..."
                $ break_down = True
                jump day_4_menu_v1