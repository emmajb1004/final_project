# -- this is the instructions screen for the start of the game --
screen start_instructions():
    # This prevents the player from clicking past the screen accidentally
    modal True 
    
    # Background for the instruction box
    zorder 100
    add Solid("#000000cc") # Semi-transparent black background
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background Solid("#ffffffff") # Light transparent white frame
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "HOW TO PLAY" size 40 xalign 0.5 bold True
            
            text "• Click to advance dialogue and progress through the game."
            text "• Use the Mouse to interact with game elements."
            text "• There will be multiple moments throughout the game where audio and video clips will play. Clicking during them will end the clip early."
            text "• If you click too fast through dialogue, click back button on lower left side of the UI box."
            text "• Click history button at bottom of UI box to read through past dialogue."
            text "• Click the save button in the UI box at any point to save your progress."
            text "• Press 'H' to hide the UI and see the screen."
            text "• Press the help button in the UI box at any point to see these instructions again."
            
            
            null height 20
            
            textbutton "START GAME":
                xalign 0.5
                action Return() # Simply hides the overlay

# -- this is the instructions screen --
screen instructions():
    # This prevents the player from clicking past the screen accidentally
    modal True 
    
    # Background for the instruction box
    zorder 100
    add Solid("#000000cc") # Semi-transparent black background
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background Solid("#ffffffff") # Light transparent white frame
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "HOW TO PLAY" size 40 xalign 0.5 bold True
            
            text "• Click to advance dialogue and progress through the game."
            text "• Use the Mouse to interact with game elements."
            text "• If you click too fast through dialogue, click back button on lower left side of the UI box."
            text "• Click history button at bottom of UI box to read through past dialogue."
            text "• Click the save button in the UI box at any point to save your progress."
            text "• There will be multiple moments throughout the game where audio and video clips will play. Clicking during them will end the clip early."
            text "• Press 'H' to hide the UI and see the screen."
            
            null height 20
            
            textbutton "CLOSE":
                xalign 0.5
                action Hide("instructions") # Simply hides the overlay