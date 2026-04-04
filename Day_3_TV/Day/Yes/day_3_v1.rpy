label day_3_v1:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ action_one = False
    $ action_two = False
    $ action_three = False

    label day_3_intro_v1:
        scene living_room
        Amy "I don't know what's wrong with me. It's just static. Everything is static."
    
    label day_3_menu_v1:
        if action_one and action_two and action_three:
            jump night_3_v1       

        menu:
            "go to kitchen" if not action_one:
                scene master_bedroom with pixellate
                Amy "What.. Why am I in the bedroom? I thought... I was going to the kitchen."
                $ action_one = True
                jump day_3_menu_v1
        menu:
            "go get a glass of water" if not action_two:
                scene kitchen with pixellate
                Amy "I .. I don't understand. What's wrong with my hand? What's going on?"
                $ action_two = True
                jump day_3_menu_v1
        menu:
            "try to lay down" if not action_three:
                scene living_room with pixellate
                Amy "I think I just need to lay down and..."
                $ action_three = True
                jump day_3_menu_v1

label query_AIMEE_tv:
    scene background
    """
    Show AIMEE watching show on tv that is against back wall.
    """