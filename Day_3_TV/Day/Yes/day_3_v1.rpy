define flash = Fade(0.1, 0.0, 0.5, color="#fff")
image bad_movie = Movie(play="images/zombiebad.webm", channel="movie", loop=False)

screen remote_screen():
    imagebutton:
        idle "remote"
        at item_hover, Transform(zoom=0.2) 
        xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
        action Return()

screen kitchen_day3():
    imagebutton:
        idle "water"
        at item_hover, Transform(zoom=0.3)
        xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
        action Jump("clicked_glass_day3")

label day_3_v1:
    $ action_one = False
    $ action_two = False
    $ action_three = False

    label day_3_intro_v1:
        scene living_room
        show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
        Amy "I feel so out of it today. I think I just need to relax and watch something."
        "~Click the black remote to turn on the TV~"
        call screen remote_screen
        scene bad_movie with dissolve
        pause 14.0
        scene living_room with dissolve
        show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
        Amy "I don't understand what's going on. What was that?"
        Amy "Why does my head hurt so much?"
        Amy "I think maybe I need some water."
    
    label day_3_menu_v1:
        if action_one and action_two and action_three:
            jump night_3_v1      

        menu:
            "go to kitchen" if not action_one:
                scene master_bedroom with pixellate
                show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
                Amy "What.. Why am I in the bedroom? I thought... I was going to the kitchen."
                $ action_one = True
                jump day_3_menu_v1
        menu:
            "go get a glass of water" if not action_two:
                jump day_3_kitchen_loop
        menu:
            "try to lay down" if not action_three:
                scene living_room with pixellate
                show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
                Amy "I think I just need to lay down and..."
                $ action_three = True
                jump day_3_menu_v1

# kitchen loop
    label day_3_kitchen_loop:
        scene kitchen with pixellate
        call screen kitchen_day3

    label clicked_glass_day3:
        # Show the messed up AI hand asset
        show ai_hand at center with flash
        with hpunch
        pause 2.0
        Amy "I .. I don't understand. What's wrong with my hand? What's going on?"
        hide ai_hand with dissolve
        $ action_two = True
        jump day_3_menu_v1