# -- Set Screen (User Interface Container) --
# set living room screen
screen living_room_day4_v8():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# define game clip variable
image good_game = Movie(play="images/goodgame.webm", loop=False)

label day_4_v8:
    show living_room
    show gamehappy at Transform (xpos=0.92, ypos=.60, anchor=(0.5,0.5),zoom=1.0)
    Amy "I want to play a game today!"
    "~click controller to play game~"
    call screen living_room_day4_v8
    scene good_game with dissolve
    pause 8.5
    scene living_room with dissolve
    show gamehappy at Transform (xpos=0.92, ypos=.60, anchor=(0.5,0.5),zoom=1.0)
    Amy "I love games. Even simple platformers. Games were a huge bonding experience for me and my sibling growing up." 
    Amy "We still talk about games together to this day."
    menu:
        "Call Your Sibling and Get Ready to Paint":
            jump night_4_v8