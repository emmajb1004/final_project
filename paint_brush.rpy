
label paint_brush_day:
    """
    {i}Show scene of Amy trying to find paint brush
    and A.I.MEE looking at paint brush{/i}
    """

    $ searched_studio = False
    $ searched_bathroom = False
    $ searched_kitchen = False

    label paint_brush_search:
        if searched_studio and searched_bathroom and searched_kitchen:
            jump paint_brush_night
        menu:
            "search studio" if not searched_studio:
                "{i}Show Amy searching studio{/i}"
                menu:
                    "ball of yarn":
                        Amy "I have tried over many years to try and get into knitting and I just can’t do it. Not because I don’t like it or anything, I just am genuinely so awful at it."
                    "picture of Amy's work":
                        Amy "This is the first piece where I genuinely felt proud. It's hard to fully feel great about your own work all the time, but this one I really like."
                    "picture of her dad":
                        Amy "I learned to paint from my dad. Working with him on my assignments for art class was my favorite part of high school."
                $ searched_studio = True
                jump paint_brush_search
            
            "search bathroom" if not searched_bathroom:
                scene bathroom
                "{i}Show Amy searching bathroom{/i}"
                menu:
                    "paint stained towel":
                        Amy "Unintended tie dye. I have a hard time not staining towels with paint."   
                    "bottle of hand soap":
                        Amy "I like getting the fun hand soaps. This one is called carnival"
                    "Bottle of body wash":
                        Amy "This is my splurge body wash. The absolute best smell but it costs $8 a bottle."
                $ searched_bathroom = True
                jump paint_brush_search
            
            "search kitchen" if not searched_kitchen:
                scene kitchen
                "{i}Show Amy searching kitchen{/i}"
                menu:
                    "magnet of friends":
                        Amy "A magnet from the annual secret santa from my childhood friend group. It’s a collage of photos of us throughout the years."
                    "bag of popcorn kernels":
                        Amy "I had an old roommate that I would make elaborate popcorn flavors for. I haven’t made them for myself in a while but I am always prepared for when she visits."
                    "empty dish rack":
                        Amy "I used to be on dishes at an old ice cream shop job and it was instilled in me to never put wet dishes on top of dry ones. It’s the one part of my house that I am the most organized about."
                $ searched_kitchen = True
                jump paint_brush_search


label paint_brush_night:
    """
    {i}Show scene of Amy painting and A.I.MEE sitting against
    the wall with the paint brush in the room{/i}
    """
    jump paint_menu
