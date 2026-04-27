# -- Set Screens (User Interface Container) --
# set screen for door opening
screen door():
    imagebutton:
        idle "door"
        at item_hover, Transform(zoom=0.5)
        xpos 0.4 ypos 0.75 anchor (0.5, 1.0)
        action Jump("open_door")
# set screen for painting clicked
screen painting():
    imagebutton:
        idle "escape_landscape"
        at item_hover, Transform(zoom=0.9)
        xpos 0.381 ypos 0.74 anchor (0.5, 1.0)
        action Jump("amy_ai")
# set screen for Amy clicked
screen amy_ai_interaction():
    imagebutton:
        idle "waiting_amy"
        at item_hover, Transform(zoom=0.6)
        xpos 0.45 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_amy_ai")

label bad_end:
    scene background at Transform(xpos=0.5,ypos=0.5,anchor=(0.5,0.5),zoom=1.2) with pixellate
    show escape at Transform(xpos=0.65,ypos=0.85,anchor=(0.5,1.0),zoom=0.5)
    pause 0.5
    AI "I know so much."
    AI "I can do so many things."
    AI "I can even leave..."
    call screen door

label open_door:
        show door_open at Transform(xpos=0.43,ypos=0.79,anchor=(0.5,1.0),zoom=0.6)
        show escape_landscape at Transform(xpos=0.381,ypos=0.74,anchor=(0.5,1.0),zoom=0.9)
        pause 0.5
        AI "And"
        AI "I feel..."
        show escape_neutral at Transform(xpos=0.65,ypos=0.85,anchor=(0.5,1.0),zoom=0.5)
        AI "Nothing."
        call screen painting

label amy_ai:
    scene background_amy with pixellate
    call screen amy_ai_interaction

label clicked_amy_ai:
    show waiting_amy at Transform(xpos=0.45, ypos=0.85, anchor=(0.5, 1.0), zoom=0.6)
    Amy "..."
    pause 1.0
    return


