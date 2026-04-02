
label ear_buds_day_yes_query:
    """
    {i}Show scene of Amy looking for her earbuds and forgetting music.
    A.I.MEE has earbuds and is listening to the music{/i}
    """
    $ searched_bedroom = False
    $ searched_living_room = False
    $ searched_kitchen = False
    
    label ear_buds_search:
        if searched_bedroom and searched_living_room and searched_kitchen:
            jump ear_buds_night_yes_query
        
        menu:
            "search bedroom" if not searched_bedroom:
                "{i}Show Amy searching bedroom{/i}"
                menu:
                    "discheveled bed":
                        Amy "I haven’t been sleeping well the past couple days…"
                    "bed frame with usb port":
                        Amy "We really are living in the future"
                    "Book tokens":
                        Amy "Each token is one dollar off a book. I always forget to bring them when I’m out. And I’m having trouble remembering any of the books I want…"
                $ searched_bedroom = True
                jump ear_buds_search
            "search living room" if not searched_living_room:
                "{i}Show Amy searching living room{/i}"
                menu:
                    "Vinyl record: The Wall Pink Floyd":
                        Amy "My creative writing teacher in high school played Another Brick in The Wall to teach us about lyricism. He also made us regularly read his poetry in class and talk about how much we loved it. Great album though."
                    "Coffee Table with tiny mitten on it":
                        Amy "My friend made me that. I think she meant to make me a full size one but realized it was too small and this was the placeholder. I’m having trouble remembering which friend though…"
                    "Video game console":
                        Amy "Probably my favorite hobby."
                $ searched_living_room = True
                jump ear_buds_search
            "search kitchen" if not searched_kitchen:
                "{i}Show Amy searching kitchen{/i}"
                menu:
                    "magnet of friends":
                        Amy "Wait, this doesn’t look right… I don’t think these are the right pictures"
                    "coffee mug":
                        Amy "I don’t understand. I can’t read the writing anymore."
                    "springform pan":
                        Amy "I bought this pan to make cheesecake because I love it so much."
                $ searched_kitchen = True
                jump ear_buds_search

label ear_buds_night_yes_query:
    """
    {i}Show scene of Amy trying to paint but having a harder time.
    A.I.MEE has paint brush and is listening to music and swirling 
    finger on floor like she is painting{/i}
    """
    jump sing_menu