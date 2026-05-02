# -- Set Screen (User Interface Container) --
# set movie screen
screen movie_screen():
    imagebutton:
        idle "tv"
        at item_hover
        xpos 0.5 ypos 0.4 
        anchor (0.5, 0.5)
        action Return()

# define movie clip variable to specific size
image aimeemovie = Movie(
    play="images/aimeemovie.webm", 
    size=(440, 230), 
    loop=False,
    keep_last_frame=True
)

label night_3_AI_yes:
    scene background with pixellate
    show tv:
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    show watching at Transform(xpos=0.3, ypos=0.9, anchor=(0.5, 1.0), zoom=0.7)
    call screen movie_screen
    show aimeemovie:
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    pause 10.0
    hide aimeemovie with Dissolve(0.2)
    AI "...!"
    jump movie_menu

