# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Amy = Character("Amy", color="FFC72C")
define AI = Character("A.I.MEE", color="6A6767")
define queried = 0

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
    "No":
        "{i}User has selected not to query the machine{/i}"

label ear_buds_day_yes_query:
    """
    {i}Show scene of Amy looking for her earbuds and forgetting music.
    A.I.MEE has earbuds and is listening to the music{/i}
    """

label ear_buds_day_no_query:
    """
    {i}Show scene of Amy singing and 
    A.I.MEE sitting and waiting for a query{/i}
    """

label ear_buds_night_yes_query:
    """
    {i}Show scene of Amy trying to paint but having a harder time.
    A.I.MEE has paint brush and is listening to music and swirling 
    finger on floor like she is painting{/i}
    """

label ear_buds_night_no_query:
    """
    {i}Show scene of Amy happily painting her picture.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """

label sing_menu:
    "Would you like A.I.MEE to try and sing you a song?"

menu:
    "Yes":
        "{i}User has selected to query A.I.MEE{/i}"
    "No":
        "{i}User has selected not to query the machine{/i}"

label tv_day_yes_query:
    """
    {i}Show scene of Amy in living room, grey, wathcing static on TV.
    A.I.MEE is watching a scene from a movie and learning human behavior{/i}
    """

label tv_day_no_query:
    """
    {i}Show scene of Amy laughing and happily watching something on TV.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """

label tv_night_yes_query:
    """
    {i}Show scene of Amy in a dull room, trying to paint but it is hard.
    A.I.MEE is laying on the floor (with paintbrush, music, tv)
    trying to image what feeling emotions is like{/i}
    """

label tv_night_no_query:
    """
    {i}Show scene of Amy happily painting her picture. 
    A.I.MEE is sitting against the wall, waiting for a query{/i}
    """

label movie_menu:
    "Would you like A.I.MEE to try and make you a movie?"

menu:
    "Yes":
        "{i}User has selected to query A.I.MEE{/i}"
    "No":
        "{i}User has selected not to query the machine{/i}"

label game_day_yes_query:
    """
    {i}Show scene of Amy curled up on the floor crying,
    controller in front of her, because she forgot how to play games.
    A.I.MEE has a controller in her hand and is pressed against 
    the wall, as if she can sense Amy.{/i}
    """

label game_day_no_query:
    """
    {i}Show Amy happily playing a game in her living room.
    A.I.MEE is sitting against the back wall, waiting for a query{/i}
    """

label game_night_yes_query:
    """
    {i}Show scene of Amy standing, looking at her finished landscape picture,
    it has a hallow of light around it. You get the sense it has taken
    everything from her. A.I.MEE is standing at the front looking out,
    like she is breaking the fourth wall and can see us, with her hand raised{/i}
    """

label game_night_no_query:
    """
    {i}Show scene of Amy sitting and happily looking at her finished painting.
    A.I.MEE is sitting against the wall, waiting for a query{/i}
    """

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