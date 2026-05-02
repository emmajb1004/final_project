# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Amy = Character("Amy", color="FFC72C")
define AI = Character("A.I.MEE", color="6A6767")
default queried = 0 # variable to keep track of how many queries, determines good or bad ending
# variables to keep track of when the user chooses to query A.I.MEE, determines version of day
default paint_query = False
default song_query = False
default movie_query = False
default play_game = True

# The game starts here.
label start:
    call screen start_instructions
    scene grey1 with pixellate
    "Would you like to query the machine?"

    menu:
        "Yes":
            jump day_1 # jump to first day in script

label paint_menu:
    scene grey2 with pixellate
    "Would you like A.I.MEE to try and paint you a picture?"

    menu:
        "Yes":
            $ queried += 1
            $ paint_query = True
            jump day_2_v1 # jump to day 2, version 1 in script
        "No":
            jump day_2_v2 # jump to day 2, version 2 in script

label sing_menu:
    scene grey3 with pixellate
    "Would you like A.I.MEE to try and sing you a song?"

    menu:
        "Yes":
            $ queried += 1
            $ song_query = True
            if paint_query:
                jump day_3_v1 # jump to day 3, version 1 in script
            else:
                jump day_3_v3 # jump to day 3, version 3 in script
        "No":
            if paint_query:
                jump day_3_v2 # jump to day 3, version 2 in script
            else:
                jump day_3_v4 # jump to day 3, version 4 in script

label movie_menu:
    scene grey4 with pixellate
    "Would you like A.I.MEE to try and make you a movie?"

    menu:
        "Yes":
            $ queried += 1
            $ movie_query = True
            if paint_query and song_query:
                jump day_4_v1 # jump to day 4, version 1 in script
            elif paint_query and not song_query:
                jump day_4_v3 # jump to day 4, version 3 in script
            elif not paint_query and song_query:
                jump day_4_v5 # jump to day 4, version 5 in script
            else:
                jump day_4_v7 # jump to day 4, version 7 in script
        "No":
            if paint_query and song_query:
                jump day_4_v2 # jump to day 4, version 2 in script
            elif paint_query and not song_query:
                jump day_4_v4 # jump to day 4, version 4 in script
            elif not paint_query and song_query:
                jump day_4_v6 # jump to day 4, version 6 in script
            else: 
                jump day_4_v8 # jump to day 4, version 6 in script

label game_query_menu:
    scene grey5 with pixellate
    if queried == 0:
        jump good_end
    elif queried < 2:
        $ play_game = False
    else:
        $ queried = True
    "Aimee wants to play a game."
    
    menu:
        "Okay":
            "You will play with Aimee."
            jump bad_end
        "I don't want to play." if play_game == False:
            "You won't play with Aimee."
            jump good_end