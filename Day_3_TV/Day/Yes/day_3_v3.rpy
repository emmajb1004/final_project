image movie_clip1 = Movie(play="images/zombiebad.webm", channel="movie", loop=False)
image movie_clip2 = Movie(play="images/zombiebad.webm", channel="movie", loop=False)
image movie_clip3 = Movie(play="images/zombiebad.webm", channel="movie", loop=False)

screen remote_day_3_v3():
    # Remote
        imagebutton:
            idle "remote"
            at item_hover, Transform(zoom=0.2) 
            xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
            action Return()

screen laptop_day_3_v3:
    # Laptop
        imagebutton:
            idle "laptop"
            at item_hover, Transform(zoom=0.6)
            xpos 0.3 ypos 0.6 anchor (0.5, 0.5)
            action Jump("clicked_laptop")

screen phone_day_3_v3:
    # Phone
        imagebutton:
            idle "phone"
            at item_hover, Transform(zoom=0.3)
            xpos 0.45 ypos 0.75 anchor (0.5, 0.5)
            action Jump("clicked_phone")

label day_3_v3:
    $ laptop = False
    $ phone = False

    label day_3_intro_v3:
        scene living_room
        Amy "My head hurts. I just want to laydown and watch something."
        "~click black remote to watch something~"
        call screen remote_day_3_v3
        scene movie_clip1 with dissolve
        pause 14.0
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
        call screen laptop_day_3_v3
        Amy "Here it is"

    label clicked_laptop:
        scene movie_clip2 with dissolve
        pause 14.0
        Amy "What's going on?"
        Amy "I... I'll check my phone."
        $ laptop = True
        jump day_3_menu_v3

    label loop_phone:
        scene living_room with pixellate
        Amy "Maybe my phone still works..."
        call screen phone_day_3_v3

    label clicked_phone:
        scene movie_clip1 with dissolve
        pause 14.0
        Amy "It's not working. I don't understand what is happening?" 
        Amy "My head... is killing me."
        $ phone = True
        jump day_3_menu_v3