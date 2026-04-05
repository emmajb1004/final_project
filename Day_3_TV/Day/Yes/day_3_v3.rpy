label day_3_v3:
    """
    {i}Amy is trying to watch a movie but the tv won’t work.
    She tries to watch something on her phone but that doesn't work either.
    She tries to go and check the wifi but it is working fine.
    She then gives up and gets a glass of water and goes to bed. {/i}
    """

    $ laptop = False
    $ phone = False
    $ wifi = False

    label day_3_intro_v3:
        scene living_room
        Amy "The TV isn't working. I don't know. I guess I'll just try and watch on my laptop."
    
    label day_3_menu_v3:
        if laptop and phone and wifi:
            jump night_3_AI_v3      

        menu:
            "get laptop" if not laptop:
                scene master_bedroom with pixellate
                Amy "My laptop isn't working either. The screen is just static. I have to check my phone."
                $ laptop = True
                jump day_3_menu_v3
        menu:
            "check phone" if not phone:
                scene hallway with pixellate
                Amy "It's not working. Why is everything static? What's going on?"
                $ phone = True
                jump day_3_menu_v3
        menu:
            "check wifi" if not wifi:
                scene dining_kitchen with pixellate
                Amy "The wifi is fine. I don't get it. I think I just need a minute. My head hurts."
                $ wifi = True
                jump day_3_menu_v3

label night_3_AI_v3:
    scene background
    """
    Show AIMEE watching show on tv that is against back wall.
    """
    jump night_3_v3