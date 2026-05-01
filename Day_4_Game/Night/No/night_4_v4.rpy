screen painting_screen_night_4_v4():
    imagebutton:
        idle "landscape3"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_4_v4")

label night_4_v4:
    scene night_studio with dissolve
    show easel
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)    
    Amy "I don't know why I have been struggling with this piece a little."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_4_v4


label clicked_painting_night_4_v4:
    show landscape4 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "But I am feeling better now."
    jump night_4_AI_no