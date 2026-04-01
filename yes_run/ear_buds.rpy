
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
                $ searched_bedroom = True
                jump ear_buds_search
            "search living room" if not searched_living_room:
                "{i}Show Amy searching living room{/i}"
                $ searched_living_room = True
                jump ear_buds_search
            "search kitchen" if not searched_kitchen:
                "{i}Show Amy searching kitchen{/i}"
                $ searched_kitchen = True
                jump ear_buds_search

label ear_buds_night_yes_query:
    """
    {i}Show scene of Amy trying to paint but having a harder time.
    A.I.MEE has paint brush and is listening to music and swirling 
    finger on floor like she is painting{/i}
    """
    jump sing_menu