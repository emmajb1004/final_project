image aimeemovie = Movie(
    play="images/aimeemovie.webm", 
    size=(440, 230), 
    loop=False,
    keep_last_frame=True
)

screen movie_screen():
    imagebutton:
        idle "tv"
        at item_hover
        xpos 0.5 ypos 0.4 
        anchor (0.5, 0.5)
        action Jump("clicked_movie")

label night_3_AI_yes:
    scene background with pixellate
    show tv:
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    show watching at Transform(xpos=0.3, ypos=0.9, anchor=(0.5, 1.0), zoom=0.7)
    
    call screen movie_screen

label clicked_movie:
    show aimeemovie:
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    pause 9.0
    hide aimeemovie with Dissolve(0.2)
    jump finish_day_3_v1

label finish_day_3_v1:
    AI "...!"
    jump movie_menu

