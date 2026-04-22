# Day 2 screens
screen bedroom_day2():
    if not searched_mask:
        imagebutton:
            idle "sleepmask"
            at item_hover, Transform(zoom=0.2) 
            xpos 0.35 ypos 0.65 anchor (0.5, 0.5)
            action Jump("clicked_mask")
            
    if not searched_alarm:
        imagebutton:
            idle "alarm"
            at item_hover, Transform(zoom=0.4)
            xpos 0.08 ypos 0.74 anchor (0.5, 1.0)
            action Jump("clicked_alarm")

    if not searched_fan:
        imagebutton:
            idle "fan"
            at item_hover, Transform(zoom=0.3)
            xpos 0.8 ypos 0.62 anchor (0.5, 1.0)
            action Jump("clicked_fan")

    textbutton "Leave Room":
        align (0.05, 0.05)
        text_color "#ffffff"
        text_hover_color "#ccff00"
        text_outlines [(3, "#000", 0, 0)]
        action Jump("leave_bedroom_day_2")

screen living_room_day2():
    if not searched_record:
        imagebutton:
            idle "record"
            at item_hover, Transform(zoom=0.5)
            xpos 0.75 ypos 0.9 anchor (0.5, 1.0)
            action Jump("clicked_record")

    if not searched_mitten:
        imagebutton:
            idle "mitten"
            at item_hover, Transform(zoom=0.4)
            xpos 0.55 ypos 0.68 anchor (0.5, 0.5)
            action Jump("clicked_mitten")

    if not searched_console:
        imagebutton:
            idle "console"
            at item_hover, Transform(zoom=0.7)
            xpos 0.12 ypos 0.6 anchor (0.5, 0.5)
            action Jump("clicked_console")

    textbutton "Leave Room":
        align (0.05, 0.05)
        text_color "#ffffff"
        text_outlines [(3, "#000", 0, 0)]
        action Jump("leave_living_room_day_2")

screen kitchen_day2():
    if not searched_magnet:
        imagebutton:
            idle "bad_magnet"
            at item_hover, Transform(zoom=0.14)
            xpos 0.355 ypos 0.4 anchor (0.5, 0.5)
            action Jump("clicked_bad_magnet")

    if not searched_mug:
        imagebutton:
            idle "bad_mug"
            at item_hover, Transform(zoom=0.15)
            xpos 0.42 ypos 0.58 anchor (0.5, 1.0)
            action Jump("clicked_bad_mug")

    if not searched_bad_pan:
        imagebutton:
            idle "bad_pan"
            at item_hover, Transform(zoom=0.35)
            xpos 0.715 ypos 0.57 anchor (0.5, 1.0)
            action Jump("clicked_bad_pan")

    textbutton "Leave Room":
        align (0.05, 0.05)
        text_color "#ffffff"
        text_outlines [(3, "#000", 0, 0)]
        action Jump("leave_kitchen_day_2")

label day_2_v1:

    # bedroom variables
    $ items_searched_bedroom = 0
    $ searched_mask = False
    $ searched_alarm = False
    $ searched_fan = False

    # living room variables
    $ items_searched_living_room = 0
    $ searched_record = False
    $ searched_mitten = False
    $ searched_console = False

    # kitchen variables
    $ items_searched_kitchen = 0
    $ searched_magnet = False
    $ searched_mug = False
    $ searched_bad_pan = False

    # menu variables
    $ searched_bedroom = False
    $ searched_living_room = False
    $ searched_kitchen = False

    label day_2_intro_v1:
        scene hallway
        #play music "audio/sweetheart_suno.mp3" fadein 2.0
        "Play song snippet"
        Amy "What is that? It sounds like this old song my mom used to sing to me. Where is it coming from?"
    
    label day_2_search_v1:
        if searched_bedroom and searched_living_room and searched_kitchen:
            Amy "I've searched anywhere. I don't understand. My head hurts. I just need to call it a day. And paint."
            jump night_2_v1
        
        scene hallway with dissolve
        Amy "Where should I search?"
        
        menu:
            "bedroom" if not searched_bedroom:
                Amy "Let me try searching my room."
                jump day_2_bedroom_loop
            "living room" if not searched_living_room:
                Amy "Let me see if they are in the living room."
                jump day_2_living_room_loop
            "kitchen" if not searched_kitchen:
                Amy "Maybe they are in the kitchen"
                jump day_2_kitchen_loop

    label day_2_bedroom_loop:
        if items_searched_bedroom == 3:
            Amy "Hmm I guess they aren't in here."
            $ searched_bedroom = True
            jump day_2_search_v1

        scene master_bedroom with dissolve
        show concerned2 at Transform (xpos=0.95, ypos=.55, anchor=(0.5,0.5),zoom=0.8)
        call screen bedroom_day2

    label clicked_mask:
        Amy "I haven’t been sleeping well the past couple days…"
        $ searched_mask = True
        $ items_searched_bedroom += 1
        jump day_2_bedroom_loop

    label clicked_alarm:
        Amy "I like to test my abilities to read an analog clock from time to time... for some reason. But it isn't making any sound."
        $ searched_alarm = True
        $ items_searched_bedroom += 1
        jump day_2_bedroom_loop

    label clicked_fan:
        Amy "I like to be cold when I sleep. But it isn't turned on or making any sound now."
        $ searched_fan = True
        $ items_searched_bedroom += 1
        jump day_2_bedroom_loop

    label leave_bedroom_day_2:
        Amy "Maybe I'll look somewhere else."
        jump day_2_search_v1

    # living room loop
    label day_2_living_room_loop:
        if items_searched_living_room == 3:
            Amy "Can't find them anywhere here."
            $ searched_living_room = True
            jump day_2_search_v1
        
        scene living_room with dissolve
        show concerned2 at Transform (xpos=0.9, ypos=.55, anchor=(0.5,0.5),zoom=0.8)
        call screen living_room_day2

    label clicked_record:
        Amy "My creative writing teacher in high school played Another Brick in The Wall to teach us about lyricism. He also made us regularly read his poetry in class and talk about how much we loved it. But that's not where the song is coming from."
        $ searched_record = True
        $ items_searched_living_room += 1
        jump day_2_living_room_loop

    label clicked_mitten:
        Amy "It’s a little mitten my friend made me. A placeholder for a full sized pair. It was... hmm... I can’t remember my friend..."
        $ searched_mitten = True
        $ items_searched_living_room += 1
        jump day_2_living_room_loop

    label clicked_console:
        Amy "Probably my favorite hobby. But the sound isn't coming from there."
        $ searched_console = True
        $ items_searched_living_room += 1
        jump day_2_living_room_loop

    label leave_living_room_day_2:
        Amy "Maybe I should try another room."
        jump day_2_search_v1

    # kitchen loop
    label day_2_kitchen_loop:
        if items_searched_kitchen == 3:
            Amy "I feel really uncomfortable in this room. I need to leave."
            $ searched_kitchen = True
            jump day_2_search_v1
        
        scene kitchen with dissolve
        show concerned2 at Transform (xpos=0.92, ypos=.63, anchor=(0.5,0.5),zoom=0.7)
        call screen kitchen_day2

    label clicked_bad_magnet:
        Amy "Wait, this doesn’t look right… I don’t think these are the right pictures."
        $ searched_magnet = True
        $ items_searched_kitchen += 1
        jump day_2_kitchen_loop

    label clicked_bad_mug:
        Amy "I don’t understand. I can’t read the writing anymore."
        $ searched_mug = True
        $ items_searched_kitchen += 1
        jump day_2_kitchen_loop

    label clicked_bad_pan:
        Amy "Wait. This isn't the right pan... what's going on?"
        $ searched_bad_pan = True
        $ items_searched_kitchen += 1
        jump day_2_kitchen_loop

    label leave_kitchen_day_2:
        Amy "Let me try somewhere else."
        jump day_2_search_v1