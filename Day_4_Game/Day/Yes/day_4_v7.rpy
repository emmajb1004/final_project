label day_4_v7:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

    $ water = False
    $ game = False
    $ laydown = False

    label day_4_intro_v7:
        scene living_room with pixellate
        Amy "I'm just not playing as well today. I don't know what is going on with me."
    
    label day_4_menu_v7:
        if water and game and laydown:
            jump night_4_v7      

        menu:
            "get a glass of water" if not water:
                scene kitchen with pixellate
                Amy "Huh? That was weird. I swear my hand... I just didn't sleep well, that's all."
                $ water = True
                jump day_4_menu_v7
        menu:
            "try to play again" if not game:
                scene living_room with dissolve
                Amy "I think I need to stop. I couldn't recognize the controller for a minute."
                $ game = True
                jump day_4_menu_v7
        menu:
            "lay down" if not laydown:
                scene living_room with dissolve
                Amy "I feel a bit off. I think I just need a minute to rest."
                $ laydown = True
                jump day_4_menu_v7

label query_AIMEE_game_version_7:
    scene background
    """
    Show AIMEE watching show on tv that is against back wall.
    """