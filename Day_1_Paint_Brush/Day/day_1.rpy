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
    $ searched_popcorn = False
    $ searched_dish_rack = False

    # menu variables
    $ searched_studio = False
    $ searched_bathroom = False
    $ searched_kitchen = False

    label day_1_intro:
        scene hallway
        Amy "I can't find my paint brush anywhere. I know I have lots of paint brushes I could use but it annoys me I can't find this specific one."

    label day_1_search:
        if searched_studio and searched_bathroom and searched_kitchen:
            Amy "Hmm. I don't know. I've searched everywhere. Maybe it'll turn up later."
            jump day_1_AI
            scene hallway
        Amy "Where should I look?"
    
    menu:
        "art studio" if not searched_studio:
            Amy "Let me try searching my art studio."
            jump day_1_studio_search_loop
        "bathroom" if not searched_bathroom:
            Amy "Let me check the bathroom."
            jump day_1_bathroom_search_loop
        "kitchen" if not searched_kitchen:
            Amy "Might have left it in the kitchen."
            jump day_1_kitchen_search_loop

    label day_1_studio_search_loop:
        scene hallway with dissolve
        # check if room has been searched
        if items_searched_studio == 3:
            Amy "Can't find it here."
            $ searched_studio = True
            jump day_1_search  
        menu:
            "ball of yarn" if not searched_yarn:
                Amy "I have tried over many years to try and get into knitting and I just can’t do it. Not because I don’t like it or anything, I just am genuinely so awful at it."
                $ searched_yarn = True
                $ items_searched_studio += 1
                jump day_1_studio_search_loop # This keeps Amy in the room
            "picture of my work" if not searched_work:
                Amy "This is the first piece where I genuinely felt proud. It's hard to fully feel great about your own work all the time, but this one I really like."
                $ searched_work = True
                $ items_searched_studio += 1
                jump day_1_studio_search_loop # This keeps Amy in the room
            "picture of my dad" if not searched_dad:
                Amy "I learned to paint from my dad. Working with him on my assignments for art class was my favorite part of high school."
                $ searched_dad = True
                $ items_searched_studio += 1
                jump day_1_studio_search_loop # This keeps Amy in the room
            "Leave Room":
                Amy "Maybe I'll look somewhere else."
                jump day_1_search

    label day_1_bathroom_search_loop:
        scene bathroom with dissolve
        # check if room has been searched
        if items_searched_bathroom == 3:
            Amy "I guess it's not here."
            $ searched_bathroom = True
            jump day_1_search
        menu:  
            "paint stained towel" if not searched_towel:
                Amy "Unintended tie dye. I have a hard time not staining towels with paint."   
                $ searched_towel = True
                $ items_searched_bathroom += 1
                jump day_1_bathroom_search_loop # This keeps Amy in the room
            "bottle of hand soap" if not searched_hand_soap:
                Amy "I like getting the fun hand soaps. This one is called carnival"
                $ searched_hand_soap = True
                $ items_searched_bathroom += 1
                jump day_1_bathroom_search_loop # This keeps Amy in the room
            "Bottle of body wash" if not searched_body_wash:
                Amy "This is my splurge body wash. The absolute best smell but it costs $8 a bottle."
                $ searched_body_wash = True
                $ items_searched_bathroom += 1
                jump day_1_bathroom_search_loop # This keeps Amy in the room
            "Leave Room":
                Amy "Maybe I'll look somewhere else."
                jump day_1_search

    label day_1_kitchen_search_loop:
        scene kitchen with dissolve
        if items_searched_kitchen == 3:
            Amy "I don't think it is here."
            $ searched_kitchen = True
            jump day_1_search
        menu:
            "magnet of friends" if not searched_magnet:
                Amy "A magnet from the annual secret santa from my childhood friend group. It’s a collage of photos of us throughout the years."
                $ searched_magnet = True
                $ items_searched_kitchen += 1
                jump day_1_kitchen_search_loop # This keeps Amy in the room
            "bag of popcorn kernels" if not searched_popcorn:
                Amy "I had an old roommate that I would make elaborate popcorn flavors for. I haven’t made them for myself in a while but I am always prepared for when she visits."
                $ searched_popcorn = True
                $ items_searched_kitchen += 1
                jump day_1_kitchen_search_loop # This keeps Amy in the room
            "empty dish rack" if not searched_dish_rack:
                Amy "I used to be on dishes at an old ice cream shop job and it was instilled in me to never put wet dishes on top of dry ones. It’s the one part of my house that I am the most organized about."
                $ searched_dish_rack = True
                $ items_searched_kitchen += 1
                jump day_1_kitchen_search_loop # This keeps Amy in the room
            "Leave Room":
                Amy "Maybe I'll look somewhere else."
                jump day_1_search

label day_1_AI:
    scene background
    show paint_brush
    """
    Show AIMEE looking at paintbrush on the floor.
    """
    jump night_1
