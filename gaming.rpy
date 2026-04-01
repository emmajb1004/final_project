label game_day_yes_query:
    """
    {i}Show scene of Amy curled up on the floor crying,
    controller in front of her, because she forgot how to play games.
    A.I.MEE has a controller in her hand and is pressed against 
    the wall, as if she can sense Amy.{/i}
    """
    $ cried_one = False
    $ cried_two = False
    $ cried_three = False

    label game_menu:
        if cried_one and cried_two and cried_three:
            jump game_night_yes_query   
        menu:
            "cry 1" if not cried_one:
                "{i}Show Amy crying{/i}"
                $ cried_one = True
                jump game_menu
            "cry 2" if not cried_two:
                "{i}Show Amy crying{/i}"
                $ cried_two = True
                jump game_menu
            "cry 3" if not cried_three:
                "{i}Show Amy crying{/i}"
                $ cried_three = True
                jump game_menu

label game_day_no_query:
    """
    {i}Show Amy happily playing a game in her living room.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """
    jump game_night_no_query


label game_night_yes_query:
    """
    {i}Show scene of Amy standing, looking at her finished landscape picture,
    it has a hallow of light around it. You get the sense it has taken
    everything from her. A.I.MEE is standing at the front looking out,
    like she is breaking the fourth wall and can see us, with her hand raised{/i}
    """
    jump game_query_menu

label game_night_no_query:
    """
    {i}Show scene of Amy sitting and happily looking at her finished painting.
    A.I.MEE is sitting against the wall, waiting for a query{/i}
    """
    return