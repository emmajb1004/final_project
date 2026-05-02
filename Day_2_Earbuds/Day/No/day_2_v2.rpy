# define audio variable
define audio.libby_song = "libby_song.mp3"

label day_2_v2:
    show living_room
    show singing at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=1.2)
    play sound libby_song fadeout 2.0
    Amy "My mom is a trained vocalist so she used to sing all the time when I was growing up."
    Amy "Sometimes it would just be to annoy us. But most of the time it was because she loved singing."
    Amy "I get my love of music from her."
    Amy "I feel so much better today. I'm so excited to paint."
    "~click through when you are ready to continue~"
    menu:
        "sing and get ready to paint":
            stop sound
            jump night_2_v2