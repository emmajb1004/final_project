image good_movie = Movie(play="images/moviehappy.webm", loop=False)

screen remote_screen():
    imagebutton:
        idle "remote"
        at item_hover, Transform(zoom=0.2) 
        xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
        action Return()

label day_3_v4:
    show living_room
    show moviehappy at Transform (xpos=0.92, ypos=.55, anchor=(0.5,0.5),zoom=1.0)
    Amy "I really want to watch a movie today."
    Amy "I love low-budget horror films. They are so funny"
    Amy "But I also respect someone going for it and making something."
    "~click on the black remote to watch~"
    call screen remote_screen
    scene good_movie with dissolve
    pause 9.5
    scene living_room with dissolve
    show moviehappy at Transform (xpos=0.92, ypos=.55, anchor=(0.5,0.5),zoom=1.0)
    pause 0.5
    Amy "There really was a period of time where everything was zombie."
    Amy "I can only imagine how hard it is to remove the body paint..."
    Amy "That reminds me, I should work on my painting!"
    jump night_3_v4