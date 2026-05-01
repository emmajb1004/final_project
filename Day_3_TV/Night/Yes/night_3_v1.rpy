screen painting_screen_night_3_v1():
    imagebutton:
        idle "landscape2"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Jump("clicked_painting_night_3_v1")

label night_3_v1:
    scene studio with pixellate
    show easel
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "What is happening? I don't want to paint anymore. But I have to."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_3_v1


label clicked_painting_night_3_v1:
    show landscape3 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "Why do I have to?"
    jump night_3_AI_yes