screen painting_screen_night_3_v4():
    imagebutton:
        idle "landscape2"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Return()

label night_3_v4:
    scene night_studio with dissolve
    show easel
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "I think this painting is turning out really well."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_3_v4
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I can't wait to show my parents."
    jump night_3_AI_no