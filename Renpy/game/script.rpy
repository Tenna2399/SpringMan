# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("spring guy")
# The game starts here.
image e mad = Image("springman.png", oversample=0.5)
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show e mad 

    # These display lines of dialogue.

    e "hi i am spring guy and i have springs for arms."

    e "Once apon a time i had normal arms!"
    e "but than fall guy stole them and replaced them with springs."
    e "i will get my arms back and KIll fall guy" with hpunch

    menu:
        "what will you do?"

        "runnnnn!":

    
    label run!