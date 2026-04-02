label tv_day_yes_query:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ action_one = False
    $ action_two = False
    $ action_three = False

    label introduction_tv:
        scene living_room
        Amy "I don't know what's wrong with me. It's just static. Everything is static."
    
    label tv_menu:
        if action_one and action_two and action_three:
            jump tv_night_yes_query       

        menu:
            "go to kitchen" if not action_one:
                scene master_bedroom with pixellate
                Amy "What.. Why am I in the bedroom? I thought... I was going to the kitchen."
                $ action_one = True
                jump tv_menu
        menu:
            "go get a glass of water" if not action_two:
                scene kitchen with pixellate
                Amy "I .. I don't understand. What's wrong with my hand? What's going on?"
                $ action_two = True
                jump tv_menu
        menu:
            "try to lay down" if not action_three:
                scene living_room with pixellate
                Amy "I think I just need to lay down and..."
                $ action_three = True
                jump tv_menu

label tv_night_yes_query:
    """
    {i}Show scene of Amy in a dull room, trying to paint but it is hard.
    A.I.MEE is laying on the floor (with paintbrush, music, tv)
    trying to image what feeling emotions is like{/i}
    """
    jump movie_menu