screen movie_screen():
    imagebutton:
        idle "movie"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.5 
        anchor (0.5, 0.5)
        action Jump("clicked_movie")

label night_3_AI_yes:
    scene background with pixellate
    show watching at Transform(xpos=0.3, ypos=0.9, anchor=(0.5, 1.0), zoom=0.7)
    
    call screen movie_screen

label clicked_movie:
    "Show scene of movie playing"
    AI "...!"
    
    jump movie_menu