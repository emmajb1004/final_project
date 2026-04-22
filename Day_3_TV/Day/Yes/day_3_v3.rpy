screen living_room_day3():
    # Remote
    if not searched_remote:
        imagebutton:
            idle "remote"
            at item_hover, Transform(zoom=0.4)
            xpos 0.7 ypos 0.8 anchor (0.5, 0.5)
            action Jump("clicked_remote")

    # Laptop
    if not searched_laptop:
        imagebutton:
            idle "laptop"
            at item_hover, Transform(zoom=0.6)
            xpos 0.3 ypos 0.6 anchor (0.5, 0.5)
            action Jump("clicked_laptop")

    # Phone
    if not searched_phone:
        imagebutton:
            idle "phone"
            at item_hover, Transform(zoom=0.3)
            xpos 0.45 ypos 0.75 anchor (0.5, 0.5)
            action Jump("clicked_phone")

label day_3_v3:
    $ tv = False
    $ laptop = False
    $ phone = False

    $ searched_remote = False
    $ searched_laptop = False
    $ searched_phone = False

    label day_3_intro_v3:
        scene living_room
        Amy "My head hurts. I just want to laydown and watch something."
    
    label day_3_menu_v3:
        if tv and laptop and phone:
            jump night_3_v3    
        
        scene living_room with dissolve
        
        menu:
            "watch movie" if not tv:
                jump loop_tv
            
            "get laptop" if not laptop:
                jump loop_laptop
                
            "check phone" if not phone:
                jump loop_phone

    label loop_tv:
        scene living_room
        "I should find the remote."
        call screen living_room_day3
        
    label clicked_remote:
        #$ renpy.movie_cutscene("glitch_clip.webm")
        Amy "Why... why is it like that?"
        $ tv = True
        $ searched_remote = True
        jump day_3_menu_v3

    label loop_laptop:
        scene master_bedroom with pixellate
        Amy "I'll try my laptop instead."
        call screen living_room_day3

    label clicked_laptop:
        #$ renpy.movie_cutscene("glitch_clip.webm")
        Amy "What's going on?"
        $ laptop = True
        $ searched_laptop = True
        jump day_3_menu_v3

    label loop_phone:
        scene hallway with pixellate
        Amy "Maybe my phone still works..."
        call screen living_room_day3

    label clicked_phone:
        #$ renpy.movie_cutscene("glitch_clip.webm")
        Amy "It's not working. I don't understand what is happening? My head... is killing me."
        $ phone = True
        $ searched_phone = True
        jump day_3_menu_v3