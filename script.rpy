# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Amy = Character("Amy", color="FFC72C")
define AI = Character("A.I.MEE", color="6A6767")
default queried = 0

# The game starts here.

label start:

    "Would you like to query the machine?"

    menu:
        "Yes":
            "{i}Show starting scene{/i}"

label paint_brush_day:
    """
    {i}Show scene of Amy trying to find paint brush
    and A.I.MEE looking at paint brush{/i}
    """

    menu:
        "search studio":
            "{i}Show Amy searching studio{/i}"
            jump paint_brush_night
        "search bathroom":
            "{i}Show Amy searching bathroom{/i}"
            jump paint_brush_night
        "search kitchen":
            "{i}Show Amy searching kitchen{/i}"
            jump paint_brush_night

label paint_brush_night:
    """
    {i}Show scene of Amy painting and A.I.MEE sitting against
    the wall with the paint brush in the room{/i}
    """
label paint_menu:
    "Would you like A.I.MEE to try and paint you a picture?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            jump ear_buds_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump ear_buds_day_no_query

label ear_buds_day_yes_query:
    """
    {i}Show scene of Amy looking for her earbuds and forgetting music.
    A.I.MEE has earbuds and is listening to the music{/i}
    """
    menu:
        "search bedroom":
            "{i}Show Amy searching bedroom{/i}"
            jump ear_buds_night_yes_query
        "search living room":
            "{i}Show Amy searching living room{/i}"
            jump ear_buds_night_yes_query
        "search kitchen":
            "{i}Show Amy searching kitchen{/i}"
            jump ear_buds_night_yes_query

label ear_buds_day_no_query:
    """
    {i}Show scene of Amy singing and 
    A.I.MEE sitting and waiting for a query{/i}
    """
    jump ear_buds_night_no_query

label ear_buds_night_yes_query:
    """
    {i}Show scene of Amy trying to paint but having a harder time.
    A.I.MEE has paint brush and is listening to music and swirling 
    finger on floor like she is painting{/i}
    """
    jump sing_menu

label ear_buds_night_no_query:
    """
    {i}Show scene of Amy happily painting her picture.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """
    jump sing_menu

label sing_menu:
    "Would you like A.I.MEE to try and sing you a song?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            jump tv_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump tv_day_no_query

label tv_day_yes_query:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """
    menu:
        "try to think 1":
            "{i}Show Amy trying to think{/i}"
            jump tv_night_yes_query
        "try to think 2":
            "{i}Show Amy trying to think{/i}"
            jump tv_night_yes_query
        "try to think 3":
            "{i}Show Amy trying to think{/i}"
            jump tv_night_yes_query

label tv_day_no_query:
    """
    {i}Show scene of Amy laughing and happily watching something on TV.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """
    jump tv_night_no_query

label tv_night_yes_query:
    """
    {i}Show scene of Amy in a dull room, trying to paint but it is hard.
    A.I.MEE is laying on the floor (with paintbrush, music, tv)
    trying to image what feeling emotions is like{/i}
    """
    jump movie_menu

label tv_night_no_query:
    """
    {i}Show scene of Amy happily painting her picture. 
    A.I.MEE is sitting against the wall, waiting for a query{/i}
    """
    jump movie_menu

label movie_menu:
    "Would you like A.I.MEE to try and make you a movie?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            jump game_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump game_day_no_query

label game_day_yes_query:
    """
    {i}Show scene of Amy curled up on the floor crying,
    controller in front of her, because she forgot how to play games.
    A.I.MEE has a controller in her hand and is pressed against 
    the wall, as if she can sense Amy.{/i}
    """
    menu:
        "cry 1":
            "{i}Show Amy crying{/i}"
            jump game_night_yes_query
        "cry 2":
            "{i}Show Amy crying{/i}"
            jump game_night_yes_query
        "cry 3":
            "{i}Show Amy crying{/i}"
            jump game_night_yes_query

label game_day_no_query:
    """
    {i}Show Amy happily playing a game in her living room.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """
    jump game_night_no_query


label game_night_yes_query:
    """
    {i}Show scene of Amy standing, looking at her finished landscape picture,
    it has a hallow of light around it. You get the sense it has taken
    everything from her. A.I.MEE is standing at the front looking out,
    like she is breaking the fourth wall and can see us, with her hand raised{/i}
    """
    jump game_menu

label game_night_no_query:
    """
    {i}Show scene of Amy sitting and happily looking at her finished painting.
    A.I.MEE is sitting against the wall, waiting for a query{/i}
    """
    return

label game_menu:
    "Aimee wants to play a game."

    menu:
        "Okay":
            "{i}You will play a game with Aimee{/i}"

label end_queried:
    """
    {i}Show scene of Amy sitting against the back wall, emotionless, waiting for a query.
    It is like she has swapped with A.I.MEE. A door has opened in A.I.MEE's
    world and she is about to head out. The scene outside the door is the
    same landscape scene that Amy was painting{/i}
    """
    return