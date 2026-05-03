transform credits_scroll(t):
    # Start below the screen
    ypos 1.0 yanchor 0.0
    # Move to above the screen
    linear t ypos 0.0 yanchor 1.0

screen rolling_credits(credits_string, t):
    frame:
        background "#00000044"
        xalign 0.5
        
        text credits_string:
            size 40
            text_align 0.5
            xalign 0.5
            color "#ffffff"
            outlines [ (2, "#000000", 0, 0) ]
            at credits_scroll(t)

label credits:
    $ credits_text = """
    A.I.MEE
    
    Lead Developer, Designer and Writer
    ~Emma Bass
    
    Art & Assets
    ~Amy House Backgrounds: https://spiralatlas.itch.io/visual-novel-house-backgrounds-complete
    ~Art Studio: https://www.artstation.com/artwork/xDwd22 
    ~Grey Query Backgrounds: Pixabay
    ~House Item Assets: Freepik
    ~Amy: Character Creator
    ~AI Generated Assets (for narrative purposes): Gemini
    ~AI Generated Song: Suno
    
    Special Thanks

    ~Halley Bass (Writing Consultant)
    ~Natalie Marr (Psychology Consultant)
    ~Libby Stafford (Song Writing and Performance)
    
    ~Dr. Jamie Ward (Academic Advisor)
    ~Goldsmiths, University of London
    
    Thanks for playing!
    """
    
    # Hide the interface
    window hide
    
    # Show the credits
    show screen rolling_credits(credits_text, 20)
    
    # Pause the game so the scroll can finish before returning to menu
    pause 20
    
    hide screen rolling_credits
    return