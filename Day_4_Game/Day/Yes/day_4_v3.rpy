label day_4_v3:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ game = False
    $ kitchen = False
    $ water = False

    label day_4_intro_v3:
        scene living_room with pixellate
        Amy "I'm playing horrible. I can't rememeber what these buttons mean. Everything on the screen just feels like noise.'"
    
    label day_4_menu_v3:
        if game and kitchen and water:
            jump night_4_v3      

        menu:
            "keeping trying to play" if not game:
                scene living_room with pixellate
                Amy "Nothing makes sense. Please make it stop. I need to get out of here."
                $ game = True
                jump day_4_menu_v3
        menu:
            "go to kitchen" if not kitchen:
                scene living_room with pixellate
                Amy "Why am I here? I just... I just need some water."
                $ kitchen = True
                jump day_4_menu_v3
        menu:
            "get water" if not water:
                scene kitchen with pixellate
                Amy "Make it stop. Just make it stop."
                $ water = True
                jump day_4_menu_v3

label query_AIMEE_game_version_3:
    scene background
    """
    Show AIMEE watching show on tv that is against back wall.
    """