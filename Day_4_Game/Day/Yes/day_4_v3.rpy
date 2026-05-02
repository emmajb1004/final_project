# -- Set Screens (User Interface Container) --
# set living room screen
screen living_room_day4_controller_v3():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_controller_day4_v3")

# set kitchen screen
screen kitchen_day4_water():
    imagebutton:
        idle "water"
        at item_hover, Transform(zoom=0.3)
        xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
        action Jump("clicked_water_day4")

# define visual effect variable
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
# define game clip variables
image broken_game_clip_1 = Movie(play="images/brokengameclip1.webm", loop=False)
image broken_game_clip_2 = Movie(play="images/brokengameclip2.webm", loop=False)

label day_4_v3:
    $ game = False
    $ kitchen = False
    $ water = False
    $ clicked_controller = False
    $ clicked_water = False

    label day_4_intro_v3:
        scene living_room with pixellate
        Amy "I feel so...uneasy."
        Amy "Maybe I should try playing a game."
        "~click the controller to play the game~"
        call screen living_room_day4_controller_v3

    label clicked_controller_day4_v3:
        scene broken_game_clip_1 with pixellate
        pause 6.0
        scene living_room with pixellate
        Amy "What was that? I don't understand what's going on."
        Amy "Everything on the screen just feels like noise..."
        jump day_4_menu_v3
    
    label day_4_menu_v3:
        if game and kitchen and water:
            jump night_4_v3     

        menu:
            "keeping trying to play" if not game:
                scene broken_game_clip_2 with dissolve
                pause 6.0
                scene living_room with dissolve
                Amy "What's happening to me? Nothing makes sense." 
                Amy "Please make it stop. My head... is burning."
                Amy "Maybe I should get some water."
                $ game = True
                jump day_4_menu_v3
        menu:
            "go to kitchen" if not kitchen:
                scene bathroom with pixellate
                Amy "Why am I here? I just... I just want some water."
                $ kitchen = True
                jump day_4_menu_v3
        menu:
            "get water" if not water:
                jump day_4_water_loop

    label day_4_water_loop:
        scene kitchen with pixellate
        call screen kitchen_day4_water
    
    label clicked_water_day4:
        show water_ai at Transform(xpos=0.5, ypos=0.5, anchor=(0.5,0.5), zoom=0.3) with flash
        with hpunch
        pause 0.5
        hide water_ai
        Amy "AH!"
        Amy "Make it stop. Just make it stop."
        $ water = True
        jump day_4_menu_v3