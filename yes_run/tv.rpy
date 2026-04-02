label tv_day_yes_query:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ action_one = False
    $ action_two = False
    $ action_three = False
    
    label tv_menu:
        if action_one and action_two and action_three:
            jump tv_night_yes_query       

        menu:
            "go to kitchen" if not action_one:
                scene master_bedroom
                "{i}Show Amy ending up in bedroom instead of kitchen{/i}"
                $ action_one = True
                jump tv_menu
        menu:
            "try to get glass" if not action_two:
                scene kitchen
                "{i}Show Amy with weird hand when grabbing water{/i}"
                $ action_two = True
                jump tv_menu
        menu:
            "try to lay down" if not action_three:
                scene living_room
                "{i}Show Amy trying to lay down in living room but abrupt cut{/i}"
                $ action_three = True
                jump tv_menu

label tv_night_yes_query:
    """
    {i}Show scene of Amy in a dull room, trying to paint but it is hard.
    A.I.MEE is laying on the floor (with paintbrush, music, tv)
    trying to image what feeling emotions is like{/i}
    """
    jump movie_menu