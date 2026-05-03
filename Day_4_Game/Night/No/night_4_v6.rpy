screen painting_screen_night_4_v6():
    imagebutton:
        idle "landscape3"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Return()

label night_4_v6:
    scene night_studio with dissolve
    show easel
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "Hmm.. I think I like this piece so far."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_4_v6
    show landscape4 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I was questioning it earlier. And something still feels... off. But it's better."
    jump night_4_AI_no