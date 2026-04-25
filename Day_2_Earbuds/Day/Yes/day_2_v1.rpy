# -- Set Screens (User Interface Container) --
# bedroom screens
# Only show the asset if it hasn't been searched yet
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

# living room screens
# Only show the asset if it hasn't been searched yet
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

# kitchen screens
# Only show the asset if it hasn't been searched yet
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

# music variables
define audio.sweetheart_clip1 = "<from 11>sweetheartAI.mp3"
define audio.sweetheart_clip2 = "<from 21>sweetheartAI.mp3"
define audio.sweetheart_clip3 = "<from 31>sweetheartAI.mp3"
define audio.sweetheart_clip4 = "<from 41>sweetheartAI.mp3"

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
        scene hallway with pixellate
        play sound sweetheart_clip1
        pause 9.0
        stop sound
        Amy "What is that? It sounds like this old song my mom used to sing to me. But it sounds off..."
        Amy "Where is it coming from?"
        
    menu:
        "Search Bedroom":
            Amy "Let me see if it's coming from my room."
            scene master_bedroom with dissolve
            show concerned2 at Transform (xpos=0.95, ypos=.55, anchor=(0.5,0.5),zoom=0.8)
            jump day_2_bedroom_loop 
    # -- bedroom loop --
    label day_2_bedroom_loop:
        if items_searched_bedroom == 3: # check if room has been searched
            Amy "Hmm I guess it isn't coming from here."
            scene hallway with dissolve
            play sound sweetheart_clip2
            pause 9.0
            stop sound
            $ searched_bedroom = True
            jump day_2_living_room_loop_menu
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
    
    label day_2_living_room_loop_menu:
        Amy "What is that..."
        menu:
            "Search Living Room":
                Amy "Maybe it's coming from the living room."
                scene living_room with dissolve
                show concerned2 at Transform (xpos=0.9, ypos=.55, anchor=(0.5,0.5),zoom=0.8)
                jump day_2_living_room_loop 

    # --living room loop--
    label day_2_living_room_loop:
        if items_searched_living_room == 3: # check if room has been searched
            Amy "Not from here I guess."
            $ searched_living_room = True
            scene hallway with dissolve
            play sound sweetheart_clip3
            pause 10.0
            stop sound
            jump day_2_kitchen_loop_menu
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
    
    label day_2_kitchen_loop_menu:
        Amy "I have to find where it's coming from."
        menu:
            "Search Kitchen":
                Amy "I'll check the kitchen."
                scene kitchen with dissolve
                show concerned2 at Transform (xpos=0.92, ypos=.63, anchor=(0.5,0.5),zoom=0.7)
                jump day_2_kitchen_loop 

    # --kitchen loop--
    label day_2_kitchen_loop:
        if items_searched_kitchen == 3: # check if room has been searched
            Amy "I feel really uncomfortable in this room. I need to leave."
            $ searched_kitchen = True
            scene hallway with dissolve
            play sound sweetheart_clip4
            pause 11.5
            stop sound fadeout 1.0
            jump day_2_end
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
    
    label day_2_end:
        Amy "I've searched everywhere. I don't understand. My head hurts. I just need to call it a day. And paint."
        jump night_2_v1

