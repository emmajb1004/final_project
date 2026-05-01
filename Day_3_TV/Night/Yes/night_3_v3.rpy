screen painting_screen_night_3_v3():
    imagebutton:
        idle "landscape2"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_3_v3")

label night_3_v3:
    scene night_studio with pixellate
    show easel
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "What? I don't want..." 
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_3_v3

label clicked_painting_night_3_v3:
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "My hand feels so shaky. Something isn't right."
    jump night_3_AI_yes