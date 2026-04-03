label tv_day_version_3:
    """
    {i}Amy is trying to watch a movie but the tv won’t work.
    She tries to watch something on her phone but that doesn't work either.
    She tries to go and check the wifi but it is working fine.
    She then gives up and gets a glass of water and goes to bed. {/i}
    """

    $ laptop = False
    $ phone = False
    $ wifi = False

    label introduction_tv_version_3:
        scene living_room
        Amy "The TV isn't working. I don't know. I guess I'll just try and watch on my laptop."
    
    label tv_menu_version_3:
        if laptop and phone and wifi:
            jump tv_night_yes_query       

        menu:
            "get laptop" if not laptop:
                scene master_bedroom with dissolve
                Amy "My laptop isn't working either. The screen is just static. I have to check my phone."
                $ laptop = True
                jump tv_menu_version_3
        menu:
            "check phone" if not phone:
                scene hallway with dissolve
                Amy "It's not working. Why is everything static? What's going on?"
                $ phone = True
                jump tv_menu_version_3
        menu:
            "check wifi" if not wifi:
                scene dining_kitchen with dissolve
                Amy "The wifi is fine. I don't get it. I think I just need a minute. My head hurts."
                $ wifi = True
                jump tv_menu_version_3

label query_AIMEE_tv_version_3:
    scene background
    """
    Show AIMEE watching show on tv that is against back wall.
    """