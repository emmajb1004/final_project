# -- Set Screens (User Interface Container) --
# set living room screen for controller click
screen living_room_day4_v7():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_v7")

# set living room screen for controller clicked again
screen living_room_day4_v7_again():
        imagebutton:
            idle "controller"
            at item_hover, Transform(zoom=0.3)
            xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
            action Jump("clicked_controller_v7_again")

# set kitchen screen for water
screen kitchen_day4_v7():
        imagebutton:
            idle "water"
            at item_hover, Transform(zoom=0.3)
            xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
            action Jump("clicked_water_v7")

# define visual effect variable
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
# define game clip variable
image game_play_v7 = Movie(play="images/gameplayv7.webm", channel="movie", loop=False)

label day_4_v7:
    $ water = False
    $ game = False

    label day_4_intro_v7:
        scene living_room with pixellate
        Amy "I think I want to play a game."
        "~click controller to play game~"
        call screen living_room_day4_v7
    
    label clicked_controller_v7:
        scene game_play_v7 with dissolve
        pause 8.0
        scene living_room with dissolve
        Amy "I'm just not playing as well today. I don't know what is going on with me."
        Amy "Maybe I should drink some water."
        jump day_4_menu_v7
    
    label day_4_menu_v7:
        if water and game:
            Amy "I feel a bit off today." 
            Amy "I think I just need a minute to rest before painting."
            menu:
                "get some rest":
                    jump night_4_v7       

        menu:
            "get a glass of water" if not water:
                jump loop_water_v7
        menu:
            "try to play again" if not game:
                jump loop_game_v7
    
    label loop_water_v7:
        scene kitchen with pixellate
        call screen kitchen_day4_v7
    
    label clicked_water_v7:
        show ai_hand at center with flash
        hide ai_hand with dissolve
        pause 0.5
        Amy "Huh? That was weird. I swear my hand..." 
        Amy "I just didn't sleep well, that's all."
        Amy "I'm going to get back to my game."
        $ water = True
        jump day_4_menu_v7

    label loop_game_v7:
        scene living_room with dissolve
        call screen living_room_day4_v7_again

    label clicked_controller_v7_again:
        show bad_controller at Transform(xpos=0.76,ypos=0.85, anchor=(0.5, 1.0), zoom=1.1) with flash
        hide bad_controller with dissolve
        pause 0.5 
        Amy "Woah, I couldn't recognize the controller for a minute."
        $ game = True
        jump day_4_menu_v7