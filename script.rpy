# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Amy = Character("Amy", color="FFC72C")
define AI = Character("A.I.MEE", color="6A6767")
default queried = 0
default paint_query = False
default song_query = False
default movie_query = False
default play_game = True

# The game starts here.

label start:
    scene grey
    "Would you like to query the machine?"

    menu:
        "Yes":
            "{i}Show starting scene{/i}"
            jump paint_brush_day

label paint_menu:
    scene grey
    "Would you like A.I.MEE to try and paint you a picture?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            $ paint_query = True
            jump ear_buds_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump ear_buds_day_no_query


label sing_menu:
    scene grey
    "Would you like A.I.MEE to try and sing you a song?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            $ song_query = True
            jump tv_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump tv_day_no_query

label movie_menu:
    scene grey
    "Would you like A.I.MEE to try and make you a movie?"

    menu:
        "Yes":
            "{i}User has selected to query A.I.MEE{/i}"
            $ queried = queried + 1
            $ movie_query = True
            jump game_day_yes_query
        "No":
            "{i}User has selected not to query the machine{/i}"
            jump game_day_no_query

label game_query_menu:
    scene grey
    if queried > 2:
        $ play_game = False
    "Aimee wants to play a game"
    menu:
        "Okay":
            "You will play with Aimee"
        "I don't want to play." if not play_game:
            "You won't play with Aimee."

label end_queried:
    """
    {i}Show scene of Amy sitting against the back wall, emotionless, waiting for a query.
    It is like she has swapped with A.I.MEE. A door has opened in A.I.MEE's
    world and she is about to head out. The scene outside the door is the
    same landscape scene that Amy was painting{/i}
    """
    return