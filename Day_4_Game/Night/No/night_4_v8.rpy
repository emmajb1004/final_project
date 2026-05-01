screen painting_screen_night_4_v8():
    imagebutton:
        idle "landscape3"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_4_v8")

label night_4_v8:
    scene studio with dissolve
    show easel
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "I think it's finally done!"
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_4_v8

label clicked_painting_night_4_v8:
    show landscape4 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "My parents have done so much for me and my art. This painting is the least I could do."
    jump night_4_AI_no