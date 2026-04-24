screen door():
    imagebutton:
        idle "door"
        at item_hover, Transform(zoom=0.5)
        xpos 0.4 ypos 0.75 anchor (0.5, 1.0)
        action Jump("open_door")

label bad_end:
    scene background at Transform(xpos=0.5,ypos=0.5,anchor=(0.5,0.5),zoom=1.2)
    show escape at Transform(xpos=0.65,ypos=0.85,anchor=(0.5,1.0),zoom=0.5)
    call screen door

label open_door:
        show door_open at Transform(xpos=0.43,ypos=0.8,anchor=(0.5,1.0),zoom=0.5)
        AI "I feel..."
        show escape_neutral at Transform(xpos=0.65,ypos=0.85,anchor=(0.5,1.0),zoom=0.5)
        AI "Nothing."
        return
