label tv_day_yes_query:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ thought_one = False
    $ thought_two = False
    $ thought_three = False
    
    label tv_menu:
        if action_one and action_two and action_three:
            jump tv_night_yes_query       

        menu:
            "go to kitchen" if not action_one:
                "{i}Show Amy trying to think{/i}"
                $ action_one = True
                jump tv_menu
        menu:
            "try to get glass"
            "try to think 2" if not thought_two:
                "{i}Show Amy trying to think{/i}"
                $ thought_two = True
                jump tv_menu
        menu:
            "try to lay down"
            "try to think 3" if not thought_three:
                "{i}Show Amy trying to think{/i}"
                $ action_three = True
                jump tv_menu

label tv_night_yes_query:
    """
    {i}Show scene of Amy in a dull room, trying to paint but it is hard.
    A.I.MEE is laying on the floor (with paintbrush, music, tv)
    trying to image what feeling emotions is like{/i}
    """
    jump movie_menu