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

label query_AIMEE_gaming:
    scene background
    """
    Show AIMEE with controller in hand, pressed against the wall.
    """