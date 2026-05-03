# -- Set Screen (User Interface Container) --
screen earbuds_screen():
    imagebutton:
        idle "earbuds"
        at item_hover, Transform(zoom=0.15)
        xpos 0.55 ypos 0.82 
        anchor (0.5, 1.0)
        action Return()

# music variable
define audio.sweetheart = "sweethearthuman.mp3"

label night_2_AI_yes:
    scene background with pixellate
    show aimeefloor at Transform(xpos=0.4, ypos=0.9, anchor=(0.5, 1.0), zoom=1.3)
    call screen earbuds_screen
    play sound sweetheart volume 10.0
    pause 8.0
    AI "...?"
    stop sound
    jump sing_menu