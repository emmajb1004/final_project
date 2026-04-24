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
    scene grey1 with pixellate
    "Would you like to query the machine?"

    menu:
        "Yes":
            jump day_1

label paint_menu:
    scene grey2 with pixellate
    "Would you like A.I.MEE to try and paint you a picture?"

    menu:
        "Yes":
            $ queried += 1
            $ paint_query = True
            jump day_2_v1
        "No":
            jump day_2_v2

label sing_menu:
    scene grey3 with pixellate
    "Would you like A.I.MEE to try and sing you a song?"

    menu:
        "Yes":
            $ queried += 1
            $ song_query = True
            if paint_query:
                jump day_3_v1
            else:
                jump day_3_v3
        "No":
            if paint_query:
                jump day_3_v2
            else:
                jump day_3_v4

label movie_menu:
    scene grey4 with pixellate
    "Would you like A.I.MEE to try and make you a movie?"

    menu:
        "Yes":
            $ queried += 1
            $ movie_query = True
            if paint_query and song_query:
                jump day_4_v1
            elif paint_query and not song_query:
                jump day_4_v3
            elif not paint_query and song_query:
                jump day_4_v5
            else:
                jump day_4_v7
        "No":
            if paint_query and song_query:
                jump day_4_v2
            elif paint_query and not song_query:
                jump day_4_v4
            elif not paint_query and song_query:
                jump day_4_v6
            else: 
                jump day_4_v8

label game_query_menu:
    scene grey5 with pixellate
    if queried < 2:
        $ play_game = False
    else:
        $ queried = True
    "Aimee wants to play a game"
    
    menu:
        "Okay":
            "You will play with Aimee"
            jump bad_end
        "I don't want to play." if play_game == False:
            "You won't play with Aimee."
            jump good_end

label end_queried:
    """
    {i}Show scene of Amy sitting against the back wall, emotionless, waiting for a query.
    It is like she has swapped with A.I.MEE. A door has opened in A.I.MEE's
    world and she is about to head out. The scene outside the door is the
    same landscape scene that Amy was painting{/i}
    """
    return