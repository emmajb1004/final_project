
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
                $ searched_studio = True
                jump paint_brush_search
            "search bathroom" if not searched_bathroom:
                "{i}Show Amy searching bathroom{/i}"
                $ searched_bathroom = True
                jump paint_brush_search
            "search kitchen" if not searched_kitchen:
                "{i}Show Amy searching kitchen{/i}"
                $ searched_kitchen = True
                jump paint_brush_search


label paint_brush_night:
    """
    {i}Show scene of Amy painting and A.I.MEE sitting against
    the wall with the paint brush in the room{/i}
    """
    jump paint_menu
