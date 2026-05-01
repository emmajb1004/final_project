screen painting_screen_night_4_v7():
    imagebutton:
        idle "landscape3"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_4_v7")

label night_4_v7:
    scene studio with dissolve
    show easel
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "Painting just doesn't feel right today. I don't know why."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_4_v7

label clicked_painting_night_4_v7:
    show landscape4 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "Hopefully it gets better."
    jump night_4_AI_yes