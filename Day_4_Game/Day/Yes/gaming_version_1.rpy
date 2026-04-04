label game_day_query_version_1:
    """
    {i}Show scene of Amy curled up on the floor crying,
    controller in front of her, because she forgot how to play games.
    A.I.MEE has a controller in her hand and is pressed against 
    the wall, as if she can sense Amy.{/i}
    """
    $ cried_one = False
    $ cried_two = False
    $ cried_three = False


    label introduction_game_version_1:
        scene living_room with pixellate
        Amy "I don't know what this is."

    label game_menu_version_1:
        if cried_one and cried_two and cried_three:
            jump game_night_yes_query   
        menu:
            "pull yourself together" if not cried_one:
                Amy "I can't."
                $ cried_one = True
                jump game_menu_version_1
            "try to think of anything" if not cried_two:
                Amy "My head..."
                $ cried_two = True
                jump game_menu_version_1
            "break down" if not cried_three:
                Amy "..."
                $ cried_three = True
                jump game_menu_version_1

label query_AIMEE_gaming_version_1:
    scene background
    """
    Show AIMEE with controller in hand, pressed against the wall.
    """