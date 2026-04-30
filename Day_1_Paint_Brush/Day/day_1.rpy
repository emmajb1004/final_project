# define hover effect for clickable objects
transform item_hover:
    on hover:
        matrixcolor BrightnessMatrix(0.2)
    on idle:
        matrixcolor BrightnessMatrix(0.0)

# -- Set Screens (User Interface Container) --
# art studio screens
# Only show the asset if it hasn't been searched yet
screen studio_screen():
    # Ball of Yarn
    if not searched_yarn:
        imagebutton:
            idle "yarn"
            at item_hover, Transform(zoom=0.4)
            xpos 0.4 ypos 0.95 anchor (0.5, 1.0)
            action Jump("clicked_yarn")

    # Picture of Amy's Work
    if not searched_work:
        imagebutton:
            idle "art"
            at item_hover, Transform(zoom=0.35) 
            xpos 0.19 ypos 0.27 anchor (0.5, 0.5)
            action Jump("clicked_work")

    # Picture of child's art
    if not searched_dad:
        imagebutton:
            idle "childart"
            at item_hover, Transform(zoom=0.3)
            xpos 0.75 ypos 0.165 anchor (0.5, 0.5) 
            action Jump("clicked_dad")
    
    # option to leave room early
    textbutton "Leave Room":
        align (0.01, 0.05) 
        text_color "#ffffff"
        text_outlines [ (2, "#000", 0, 0) ] 
        text_hover_color "#ff0"
        text_bold True
        action Jump("leave_studio")

# art bathroom screens
# Only show the asset if it hasn't been searched yet
screen bathroom_screen():
    if not searched_towel:
        imagebutton:
            idle "towel" 
            at item_hover, Transform(zoom=0.6)
            xpos 0.65 ypos 0.93 anchor (0.5, 0.1) 
            action Jump("clicked_towel")

    if not searched_hand_soap:
        imagebutton:
            idle "handsoap"
            at item_hover, Transform(zoom=0.3)
            xpos 0.23 ypos 0.62 anchor (0.5, 1.0)
            action Jump("clicked_hand_soap")

    if not searched_body_wash:
        imagebutton:
            idle "bodywash"
            at item_hover, Transform(zoom=0.2)
            xpos 0.6 ypos 0.78 anchor (0.5, 1.0)
            action Jump("clicked_body_wash")

    # option to leave room early
    textbutton "Leave Room":
        align (0.01, 0.05) 
        text_color "#ffffff"
        text_outlines [ (2, "#000", 0, 0) ] 
        text_hover_color "#ff0"
        text_bold True
        action Jump("leave_bathroom")

# screen for kitchen
screen kitchen_screen():
    # Magnet of Friends
    if not searched_magnet:
        imagebutton:
            idle "magnet"
            at item_hover, Transform(zoom=0.2)
            xpos 0.35 ypos 0.4 anchor (0.5, 0.5) 
            action Jump("clicked_magnet")

    # Springform pan
    if not searched_pan:
        imagebutton:
            idle "pan"
            at item_hover, Transform(zoom=0.4)
            xpos 0.73 ypos 0.6 anchor (0.5, 1.0)
            action Jump("clicked_pan")

    # Mug
    if not searched_mug:
        imagebutton:
            idle "mug"
            at item_hover, Transform(zoom=0.4)
            xpos 0.42 ypos 0.58 anchor (0.5, 1.0)
            action Jump("clicked_mug")

    # option to leave room early
    textbutton "Leave Room":
        align (0.01, 0.05) 
        text_color "#ffffff"
        text_outlines [ (2, "#000", 0, 0) ] 
        text_hover_color "#ff0"
        text_bold True
        action Jump("leave_kitchen")

label day_1:
    # bedroom variables
    $ items_searched_studio = 0
    $ searched_yarn = False
    $ searched_work = False
    $ searched_dad = False

    # living room variables
    $ items_searched_bathroom = 0
    $ searched_towel = False
    $ searched_hand_soap = False
    $ searched_body_wash = False

    # kitchen variables
    $ items_searched_kitchen = 0
    $ searched_magnet = False
    $ searched_pan = False
    $ searched_mug = False

    # menu variables
    $ searched_studio = False
    $ searched_bathroom = False
    $ searched_kitchen = False

    label day_1_intro:
        scene hallway
        Amy "I can't find one of my paint brushes anywhere. I've had it since I was a kid."

    label day_1_search:
        # check if all rooms have been searched before moving to next scene
        if searched_studio and searched_bathroom and searched_kitchen:
            Amy "Hmm. I don't know. I've searched everywhere. Maybe it'll turn up later."
            jump night_1
            
        scene hallway
        Amy "Where should I look?"

    menu: # user choice for which room to search first
        "art studio" if not searched_studio: # remove option when searched
            Amy "Let me try searching my art studio."
            scene studio with dissolve
            show happy at Transform (xpos=0.95, ypos=.55, anchor=(0.5,0.5),zoom=0.9) # show Amy
            "~find and click on the three interactable objects in the room~"
            jump day_1_studio_search_loop
        "bathroom" if not searched_bathroom: # remove option when searched
            Amy "Let me check the bathroom."
            scene bathroom with dissolve
            show happy at Transform (xpos=0.9, ypos=.7, anchor=(0.5,0.5),zoom=1.5) # show Amy
            "~find and click on the three interactable objects in the room~"
            jump day_1_bathroom_search_loop
        "kitchen" if not searched_kitchen: # remove option when searched
            Amy "Might have left it in the kitchen."
            scene kitchen with dissolve
            show happy at Transform (xpos=0.95, ypos=.55, anchor=(0.5,0.5),zoom=0.9) # show Amy
            "~find and click on the three interactable objects in the room~"
            jump day_1_kitchen_search_loop

    label day_1_studio_search_loop:
        if items_searched_studio == 3: # check if room has been searched
            Amy "Can't find it here."
            $ searched_studio = True
            jump day_1_search  
        call screen studio_screen # activate clickable studio images

    label clicked_yarn:
        Amy "I have tried over many years to get into knitting and I just can’t do it. Not because I don’t like it or anything, I'm just so awful at it."
        $ searched_yarn = True
        $ items_searched_studio += 1
        jump day_1_studio_search_loop

    label clicked_work:
        Amy "This is the first piece I made where I genuinely felt proud. It's hard to fully feel great about your own work all the time, but this one I really like."
        $ searched_work = True
        $ items_searched_studio += 1
        jump day_1_studio_search_loop

    label clicked_dad:
        Amy "One of my first from when I was a kid. Painted it with my dad. I love painting with him."
        $ searched_dad = True
        $ items_searched_studio += 1
        jump day_1_studio_search_loop

    label leave_studio:
        Amy "Maybe I'll look somewhere else."
        jump day_1_search

    label day_1_bathroom_search_loop:
        # check if room has been searched
        if items_searched_bathroom == 3:
            Amy "I guess it's not here."
            $ searched_bathroom = True
            jump day_1_search
        call screen bathroom_screen # activate clickable studio images

    label clicked_towel:
        Amy "Unintended tie-dye. I have a hard time not staining towels with paint."
        $ searched_towel = True
        $ items_searched_bathroom += 1
        jump day_1_bathroom_search_loop

    label clicked_hand_soap:
        Amy "I like getting the fun hand soaps. This one is called 'Carnival'."
        $ searched_hand_soap = True
        $ items_searched_bathroom += 1
        jump day_1_bathroom_search_loop

    label clicked_body_wash:
        Amy "This is my splurge body wash. The absolute best smell but it costs $8 a bottle."
        $ searched_body_wash = True
        $ items_searched_bathroom += 1
        jump day_1_bathroom_search_loop

    label leave_bathroom:
        Amy "Maybe I'll look somewhere else."
        jump day_1_search

    label day_1_kitchen_search_loop:
        # check if room has been searched
        if items_searched_kitchen == 3:
            Amy "I don't think it is here."
            $ searched_kitchen = True
            jump day_1_search
        call screen kitchen_screen # activate clickable kitchen images

    label clicked_magnet:
        Amy "A magnet from the annual secret santa from my childhood friend group. It’s a collage of photos of us throughout the years."
        $ searched_magnet = True
        $ items_searched_kitchen += 1
        jump day_1_kitchen_search_loop

    label clicked_pan:
        Amy "I bought this pan specifically to make cheesecake because I love it so much. "
        $ searched_pan = True
        $ items_searched_kitchen += 1
        jump day_1_kitchen_search_loop

    label clicked_mug:
        Amy "I got this mug from volunteering at the New York Film Festival when I was a teenager."
        $ searched_mug = True
        $ items_searched_kitchen += 1
        jump day_1_kitchen_search_loop

    label leave_kitchen:
        Amy "Maybe I'll look somewhere else."
        jump day_1_search
