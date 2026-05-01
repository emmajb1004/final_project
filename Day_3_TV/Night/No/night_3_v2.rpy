screen painting_screen_night_3_v2():
    imagebutton:
        idle "landscape2"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_3_v2")

label night_3_v2:
    scene studio with dissolve
    show easel
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "I really do love painting."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_3_v3


label clicked_painting_night_3_v2:
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I've been feeling off lately but I think painting is helping today."
    jump night_3_AI_no