image zombieconfused = Movie(play="images/zombieconfused.webm", loop=False)
screen remote_day_3_v2():
    # Remote
        imagebutton:
            idle "remote"
            at item_hover, Transform(zoom=0.2) 
            xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
            action Return()

label day_3_v2:
    scene living_room
    Amy "I woke up with such a weird headache today. I don't know why."
    Amy "Maybe I should just try to relax and watch something."
    "~click black remote to watch something~"
    call screen remote_day_3_v2
    scene zombieconfused with dissolve
    pause 10.5
    scene living_room with dissolve
    pause 0.5
    Amy "That was... weird. What was that?"
    Amy "My headache is getting worse. Maybe I just need to call it a day. And paint."
    jump night_3_v2