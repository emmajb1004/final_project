screen aimee_interaction_day_2():
    imagebutton:
        idle "waiting"
        at item_hover, Transform(zoom=0.55)
        xpos 0.45 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_aimee_day_3")

label night_2_AI_no:
    scene background with pixellate
    call screen aimee_interaction_day_2

label clicked_aimee_day_2:
    show waiting at Transform(xpos=0.45, ypos=0.85, anchor=(0.5, 1.0), zoom=0.55)
    AI "..."
    jump sing_menu