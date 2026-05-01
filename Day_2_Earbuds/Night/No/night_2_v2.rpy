screen painting_screen_night_2_v2():
    imagebutton:
        idle "landscape1"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_2_v2")

label night_2_v2:
    scene studio with dissolve
    show easel
    show landscape1 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "I'm so excited to paint."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_2_v2

label clicked_painting_night_2_v2:
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "It's probably one of my favorite parts of the day."
    jump night_2_AI_no