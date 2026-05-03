# -- Set Screen (User Interface Container) --
# set aimee screen
screen aimee_interaction_day_4_yes:
    imagebutton:
        idle "awake"
        at item_hover, Transform(zoom=2.5)
        xpos 0.4 ypos 0.7 anchor (0.5, 0.5)
        action Return()

label night_4_AI_yes:
    scene background with pixellate
    show awake at Transform(xpos=0.4, ypos=0.7, anchor=(0.5, 0.5), zoom=2.5)
    call screen aimee_interaction_day_4_yes
    show awake at Transform(xpos=0.4, ypos=0.7, anchor=(0.5, 0.5), zoom=2.5)
    AI "What..."
    jump game_query_menu