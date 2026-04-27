# -- Set Screen (User Interface Container) --
# set screen for A.I.MEE clicked
screen good_end_ai():
    imagebutton:
        idle "waiting"
        at item_hover, Transform(zoom=0.55)
        xpos 0.45 ypos 0.85 anchor (0.5, 1.0)
        action Jump("clicked_good_ending_ai")

label good_end:
    scene entrance
    show good_ending at Transform(xpos=0.7,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
    show landscape4 at Transform(xpos=0.5,ypos=1.0,anchor=(0.5,1.0),zoom=0.5)
    Amy "I can't wait to show my parents this painting. I made it for them."
    Amy "About to head over to give it to them now."

label good_ending_ai:
    scene background with pixellate
    call screen good_end_ai

label clicked_good_ending_ai:
    show waiting at Transform(xpos=0.45, ypos=0.85, anchor=(0.5, 1.0), zoom=0.55)
    AI "..."
    pause 0.5
    AI "..."
    return