label day_4_v5:
    """
    {i}Show scene of Amy curled up on the floor crying,
    controller in front of her, because she forgot how to play games.
    A.I.MEE has a controller in her hand and is pressed against 
    the wall, as if she can sense Amy.{/i}
    """
    $ cried_one = False
    $ cried_two = False
    $ cried_three = False


    label day_4_intro_v5:
        scene living_room with pixellate
        Amy "I want to play a game."

    label day_4_menu_v5:
        if cried_one and cried_two and cried_three:
            jump day_4_AI_v5   
        menu:
            "try to play" if not cried_one:
                Amy "I don't... know what this is."
                $ cried_one = True
                jump day_4_menu_v5
            "try to play again" if not cried_two:
                Amy "I can't."
                $ cried_two = True
                jump day_4_menu_v5
            "give up" if not cried_three:
                Amy "Okay."
                $ cried_three = True
                jump day_4_menu_v5

label day_4_AI_v5:
    scene background
    """
    Show AIMEE with controller in hand, pressed against the wall.
    """
    jump night_4_v5