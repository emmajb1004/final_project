screen painting_screen_night_1():
    imagebutton:
        idle "landscape0"
        at item_hover, Transform(zoom=0.5)
        xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
        action Return()

label night_1:
    scene night_studio with dissolve # show background
    show easel
    show landscape0 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I've been feeling off all day. But I must paint, with or without the brush."
    "~click on the canvas to have Amy paint~"
    call screen painting_screen_night_1
    show landscape1 at Transform(xpos=0.5,ypos=0.4,anchor=(0.5,0.5),zoom=0.5) # show painting
    Amy "I'm trying to make something for my parents. They are both artists and met through art."
    Amy "It's going to be a painting of the field by the house where I grew up."
    jump night_1_AI
