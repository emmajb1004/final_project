# -- Set Screens (User Interface Container) --
# set screen for remote control
screen remote_day_3_v3():
    imagebutton:
        idle "remote"
        at item_hover, Transform(zoom=0.2) 
        xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
        action Return()
# set screen for laptop
screen laptop_day_3_v3:
    imagebutton:
        idle "laptop"
        at item_hover, Transform(zoom=0.1)
        xpos 0.55 ypos 0.75 anchor (0.5, 1.0)
        action Jump("clicked_laptop")
# set screen for phone
screen phone_day_3_v3:
    imagebutton:
        idle "phone"
        at item_hover, Transform(zoom=0.2)
        xpos 0.36 ypos 0.61 anchor (0.5, 0.5)
        action Jump("clicked_phone")

# define movie clip variables
image movie_clip1 = Movie(play="images/zombieinsert1.webm", loop=False)
image movie_clip2 = Movie(play="images/zombieinsert2.webm", loop=False)
image movie_clip3 = Movie(play="images/zombieinsert3.webm", channel="movie", loop=False)

label day_3_v3:
    $ laptop = False
    $ phone = False

    label day_3_intro_v3:
        scene living_room
        Amy "My head hurts. I think I just want to lay down and watch something."
        "~click black remote to watch something~"
        call screen remote_day_3_v3
        scene movie_clip1 with dissolve
        pause 5.5
        scene living_room with dissolve
        Amy "Why... why is it like that?"
        Amy "Let me... try my laptop."

    label day_3_menu_v3:
        if laptop and phone:
            jump night_3_v3
        
        menu:
            "get laptop" if not laptop:
                jump loop_laptop
        menu:
            "check phone" if not phone:
                jump loop_phone

    label loop_laptop:
        scene master_bedroom with pixellate
        show laptop:
            xpos 0.55 ypos 0.75 anchor (0.5, 1.0) zoom 0.1
        Amy "Here it is. Hopefully this is better."
        call screen laptop_day_3_v3

    label clicked_laptop:
        show movie_clip2 with dissolve
        pause 5.0
        scene master_bedroom with dissolve
        Amy "What's going on?"
        Amy "I... I'll check my phone."
        $ laptop = True
        jump day_3_menu_v3

    label loop_phone:
        scene living_room with pixellate
        Amy "Maybe this will be fine..."
        call screen phone_day_3_v3

    label clicked_phone:
        scene movie_clip3 with dissolve
        pause 4.0
        scene living_room with dissolve
        Amy "What is that? I don't understand what's happening." 
        Amy "And my head... is killing me."
        $ phone = True
        jump day_3_menu_v3