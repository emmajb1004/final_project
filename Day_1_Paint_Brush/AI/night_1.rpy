screen paintbrush_screen():
    imagebutton:
        idle "paint_brush"
        at item_hover, Transform(zoom=0.7)
        xpos 0.5 ypos 0.9 
        anchor (0.5, 1.0)
        action Jump("clicked_paintbrush")

label night_1_AI:
    scene background with pixellate
    show aimee at Position(xpos=0.6, ypos=0.85)
    
    # This calls the screen and waits for the user to click the brush
    call screen paintbrush_screen

label clicked_paintbrush:
    # This keeps the brush visible after the click so the scene can continue
    show paint_brush at Transform(xpos=0.47, ypos=0.75, zoom=0.7)
    
    AI "..."
    
    jump paint_menu