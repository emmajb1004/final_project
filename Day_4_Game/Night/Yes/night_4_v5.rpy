screen painting_screen_night_4_v5():
    imagebutton:
        idle "landscape3"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_4_v5")

label night_4_v5:
    scene night_studio with pixellate
    show easel
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "It is sick. I'm sick. This painting..."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_4_v5
    
label clicked_painting_night_4_v5:
    show landscape4 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I can't stop."
    jump night_4_AI_yes