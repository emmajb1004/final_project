screen painting_screen_night_2_v1():
    imagebutton:
        idle "landscape1"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Return()

label night_2_v1:
    scene night_studio with dissolve
    show easel
    show landscape1 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5)
    Amy "I'm having a harder time painting today."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_2_v1
    show landscape2 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "My painting just doesn't feel like it's mine."
    Amy "But who else's would it be?"
    jump night_2_AI_yes
