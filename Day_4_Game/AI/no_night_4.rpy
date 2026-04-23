screen aimee_interaction_day_4():
    imagebutton:
        idle "waiting"
        at item_hover, Transform(zoom=0.55)
        xpos 0.45 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_aimee_day_4")

label night_4_AI_no:
    scene background with pixellate
    call screen aimee_interaction_day_4

label clicked_aimee_day_4:
    show waiting at Transform(xpos=0.45, ypos=0.85, anchor=(0.5, 1.0), zoom=0.55)
    AI "..."
    jump game_query_menu