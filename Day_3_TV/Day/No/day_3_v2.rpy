# -- Set Screen (User Interface Container) --
# set remote control screen
screen remote_day_3_v2():
    # Remote
        imagebutton:
            idle "remote"
            at item_hover, Transform(zoom=0.2) 
            xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
            action Return()

# set movie clip variable
image zombieconfused = Movie(play="images/zombieconfused.webm", loop=False)

label day_3_v2:
    scene living_room
    show day_3_v2_amy at Transform (xpos=0.92, ypos=.55, anchor=(0.5,0.5),zoom=1.0)
    Amy "I feel a little bit better from yesterday."
    Amy "Maybe I should try to watch something."
    "~click black remote to watch something~"
    call screen remote_day_3_v2
    scene zombieconfused with dissolve
    pause 6.0
    scene living_room with dissolve
    pause 0.5
    show day_3_v2_amy at Transform (xpos=0.92, ypos=.55, anchor=(0.5,0.5),zoom=1.0)
    Amy "That was... weird. What was that?"
    Amy "Maybe my TV is acting up."
    Amy "Oh well. I should probably just call it a day."
    menu:
        "Try to Ignore It and Get Ready to Paint":
            jump night_3_v2