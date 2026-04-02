label ear_buds_day_yes_query:

    # bedroom variables
    $ items_searched_bedroom = 0
    $ searched_bed = False
    $ searched_frame = False
    $ searched_tokens = False

    # living room variables
    $ items_searched_living_room = 0
    $ searched_record = False
    $ searched_mitten = False
    $ searched_console = False

    # kitchen variables
    $ items_searched_kitchen = 0
    $ searched_magnet = False
    $ searched_mug = False
    $ searched_pan = False

    # menu variables
    $ searched_bedroom = False
    $ searched_living_room = False
    $ searched_kitchen = False

    label introduction_ear_buds:
        scene hallway
        Amy "I can't rememeber how my favorite song goes. I don't get it. Where are my ear buds?"
    
    label ear_buds_search:
        if searched_bedroom and searched_living_room and searched_kitchen:
            Amy "I've searched anywhere. I don't understand. My head hurts. I just need to call it a day. And paint."
            jump ear_buds_night_yes_query
        scene hallway
        Amy "Where should I search?"
        
        menu:
            "bedroom" if not searched_bedroom:
                Amy "Let me try searching my room."
                jump bedroom_search_loop_earbuds
            "living room" if not searched_living_room:
                Amy "Let me see if they are in the living room."
                jump living_room_search_loop_earbuds
            "kitchen" if not searched_kitchen:
                Amy "Maybe they are in the kitchen"
                jump kitchen_search_loop_earbuds
    
        label bedroom_search_loop_earbuds:
            scene master_bedroom with dissolve
            # check if room has been searched
            if items_searched_bedroom == 3:
                Amy "Hmm I guess they aren't in here."
                $ searched_bedroom = True
                jump ear_buds_search   
            menu:
                "discheveled bed" if not searched_bed:
                    Amy "I haven’t been sleeping well the past couple days…"
                    $ searched_bed = True
                    $ items_searched_bedroom += 1
                    jump bedroom_search_loop_earbuds # This keeps Amy in the room
                "bed frame with usb port" if not searched_frame:
                    Amy "We really are living in the future"
                    $ searched_frame = True
                    $ items_searched_bedroom += 1
                    jump bedroom_search_loop_earbuds # This keeps Amy in the room
                "Book tokens" if not searched_tokens:
                    Amy "Each token is one dollar off a book. I always forget to bring them when I’m out. And I’m having trouble remembering any of the books I want…"
                    $ searched_tokens = True
                    $ items_searched_bedroom += 1
                    jump bedroom_search_loop_earbuds # This keeps Amy in the room
                "Leave Room":
                    Amy "Maybe I'll look somewhere else."
                    jump ear_buds_search

        label living_room_search_loop_earbuds:
            scene living_room with dissolve
            # check if room has already been searched
            if items_searched_living_room == 3:
                Amy "Can't find them anywhere here."
                $ searched_living_room = True
                jump ear_buds_search   
            menu:
                "Vinyl record: The Wall Pink Floyd" if not searched_record:
                    Amy "My creative writing teacher in high school played Another Brick in The Wall to teach us about lyricism. He also made us regularly read his poetry in class and talk about how much we loved it."
                    $ searched_record = True
                    $ items_searched_living_room += 1
                    jump living_room_search_loop_earbuds # This keeps Amy in the room
                "Coffee Table with tiny mitten on it" if not searched_mitten:
                    Amy "My friend made me that. I think she meant to make me a full size one but realized it was too small and this was the placeholder. I’m having trouble remembering which friend though…"
                    $ searched_mitten = True
                    $ items_searched_living_room += 1
                    jump living_room_search_loop_earbuds # This keeps Amy in the room
                "Video game console" if not searched_console:
                    Amy "Probably my favorite hobby."
                    $ searched_console = True
                    $ items_searched_living_room += 1
                    jump living_room_search_loop_earbuds # This keeps Amy in the room
                "Leave Room":
                    Amy "Maybe I'll look somewhere else."
                    jump ear_buds_search
            
        label kitchen_search_loop_earbuds:
            scene kitchen with dissolve
            # check if room has already been searched
            if items_searched_kitchen == 3:
                Amy "Nowhere to be found here"
                $ searched_kitchen = True
                jump ear_buds_search
            menu:
                "magnet of friends" if not searched_magnet:
                    Amy "Wait, this doesn’t look right… I don’t think these are the right pictures"
                    $ searched_magnet = True
                    $ items_searched_kitchen += 1
                    jump kitchen_search_loop_earbuds # This keeps Amy in the room
                "coffee mug" if not searched_mug:
                    Amy "I don’t understand. I can’t read the writing anymore."
                    $ searched_mug = True
                    $ items_searched_kitchen += 1
                    jump kitchen_search_loop_earbuds # This keeps Amy in the room
                "springform pan" if not searched_pan:
                    Amy "I bought this pan to make cheesecake because I love it so much."
                    $ searched_pan = True
                    $ items_searched_kitchen += 1
                    jump kitchen_search_loop_earbuds # This keeps Amy in the room
                "Leave Room":
                    Amy "Maybe I'll look somewhere else."
                    jump ear_buds_search

label query_AIMEE_earbuds:
    scene background
    """
    Show AIMEE trying to listen to music on the floor.
    """

label ear_buds_night_yes_query:
    """
    {i}Show scene of Amy trying to paint but having a harder time.
    A.I.MEE has paint brush and is listening to music and swirling 
    finger on floor like she is painting{/i}
    """
    jump sing_menu