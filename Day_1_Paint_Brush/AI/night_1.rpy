# -- Set Screen (User Interface Container) --
screen paintbrush_screen(): # make paintbrush clickable
    imagebutton:
        idle "paint_brush"
        at item_hover, Transform(zoom=0.7)
        xpos 0.5 ypos 0.9 
        anchor (0.5, 1.0)
        action Jump("clicked_paintbrush")

label night_1_AI:
    scene background with pixellate
    show aimee at Position(xpos=0.6, ypos=0.45, anchor=(0.5, 0.1))
    call screen paintbrush_screen

label clicked_paintbrush:
    AI "..."
    jump paint_menu