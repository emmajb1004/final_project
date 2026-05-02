# -- Set Screens (User Interface Container) --
# set for remote control screen
screen remote_screen():
    imagebutton:
        idle "remote"
        at item_hover, Transform(zoom=0.2) 
        xpos 0.45 ypos 0.68 anchor (0.5, 0.5)
        action Return()

# set up screen for kitchen
screen kitchen_day3():
    imagebutton:
        idle "water"
        at item_hover, Transform(zoom=0.3)
        xpos 0.42 ypos 0.59 anchor (0.5, 1.0)
        action Return()

# variable to set up visual effect
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# variable to set up movie clip
image bad_movie = Movie(play="images/zombiebad.webm", channel="movie", loop=False)

label day_3_v1:
    label day_3_intro_v1:
        scene living_room
        show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
        Amy "I feel so out of it today. I think I just need to relax and watch something."
        "~Click the black remote to turn on the TV~"
        call screen remote_screen
        scene bad_movie with dissolve
        pause 14.0
        scene living_room with dissolve
        show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
        Amy "I don't understand what's going on. What was that?"
        Amy "Why does my head hurt so much?"
        Amy "I feel like I'm burning up. I should get some water." 
    menu:
        "Go to Kitchen":
            scene master_bedroom with pixellate
            show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
            Amy "What.. Why am I in the bedroom? I thought... I was going to the kitchen."
    menu:
        "Go Get a Glass of Water":
            scene kitchen with pixellate
            "~click on the glass of water~"
            call screen kitchen_day3
            show ai_hand at center with flash # Show the messed up AI hand asset
            with hpunch
            pause 2.0
            Amy "I .. I don't understand. What's wrong with my hand? What's going on?"
            hide ai_hand with dissolve
    menu:
        "Try to Lay Down":
            scene living_room with pixellate
            show scared at Transform(xpos=0.8,ypos=1.2,anchor=(0.5,1.0),zoom=0.8)
            Amy "I think I just need to lay down and..."
            jump night_3_v1