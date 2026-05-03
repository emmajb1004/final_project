# -- Set Screens (User Interface Container) --
# set living room screen for controller click
screen living_room_day4_v7():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# set living room screen for controller clicked again
screen living_room_day4_v7_again():
    imagebutton:
        idle "controller"
        at item_hover, Transform(zoom=0.3)
        xpos 0.76 ypos 0.85 anchor (0.5, 1.0)
        action Return()

# set kitchen screen for water
screen kitchen_day4_v7():
    imagebutton:
        idle "water"
        at item_hover, Transform(zoom=0.3)
        xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
        action Return()

# define visual effect variable
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
# define game clip variable
image game_play_v7 = Movie(play="images/gameplayv7.webm", channel="movie", loop=False)

label day_4_v7:
    scene living_room with pixellate
    show day_4_v7_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
    Amy "I have a bit of a headache today."
    Amy "But I want to try to play a game."
    "~click controller to play game~"
    call screen living_room_day4_v7
    scene game_play_v7 with dissolve
    pause 8.0
    scene living_room with dissolve
    show day_4_v7_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
    Amy "I'm just not playing as well today. I don't know what's going on with me."
    Amy "Maybe it's the headache. I should drink some water."
menu:
    "Get a Glass of Water":
        scene kitchen with pixellate
        call screen kitchen_day4_v7
        show ai_hand at center with flash
        hide ai_hand with pixellate
        pause 0.5
        show day_4_v7_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.8)
        Amy "Huh? That was weird. I swear my hand..." 
        Amy "I just didn't sleep well, that's all."
        Amy "I'm going to get back to my game."
menu:
    "Try to Play Again":
        scene living_room with dissolve
        call screen living_room_day4_v7_again
        show bad_controller at Transform(xpos=0.76,ypos=0.85, anchor=(0.5, 1.0), zoom=1.1) with flash
        hide bad_controller with dissolve
        pause 0.5 
        show day_4_v7_amy at Transform (xpos=0.9, ypos=.60, anchor=(0.5,0.5),zoom=0.9)
        Amy "Woah, I couldn't recognize the controller for a minute."
        Amy "I feel a bit off today." 
        Amy "I think I just need a minute."
menu:
    "Get Some Rest and Get Ready to Paint":
        jump night_4_v7