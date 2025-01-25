# The script of the game goes in this file.

# variables
$ mc_name = ""
$ has_magic_philo = False
$ has_philo_philo = False
$ has_industry_philo = False
$ has_magic_intro = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define G = Character("Witch of Gluttony", image='LegallyDistictPinkBlob.png', kind=bubble)
<<<<<<< Updated upstream
define mc = Character(mc_name, image='main.png', kind=bubble)
# define wm = Character("Wild Myst", image='whatever.png', kind=bubble)
=======
define P = Character("Witch of the Mind", image='LegallyDistictPinkBlob.png', kind=bubble)
>>>>>>> Stashed changes

image Glutton = "LegallyDistinctPinkBlob.png"
image main = "main.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    show Glutton

    G "Hey there pal, you seem to have created some sort of videogame or somethin\'."

    G "Now that you have given me life, you must atone for the sins you have unleashed unto this world."

    G "I hope you had fun."

    jump philosophyworld

    # This ends the game.

    return

label scienceworld:

    # all science world scripting goes here

    return

label magicworld:

    show main at left #neutral
    with moveinleft
    "You step out of the portal into a strange place."
    if (has_magic_intro==True):
        show wildmyst at right #neutral
        with moveinright
        jump magicrootdecision
    "Dashing down the steps of a building is a figure who seems to have been expecting you."
    show wildmyst at right #shocked
    with moveinright
    wm "It's YOU!"
    show wildmyst at left #neutral
    with move
    hide main
    with moveoutleft
    wm "WELCOME!"
    menu reactionfromground:
        "Okay. Help me up now, please.":
            show wildmyst at center
            with move
            show main at left #neutral
            with moveinbottom
            wm "Oh, you're no fun."
        "Hey! Watch where you're going!":
            show wildmyst at center #happy
            with move
            show main at left #neutral
            with moveinbottom
            wm "Oooh! You've got a temper on you. I like it!"
            mc "That makes one of us."
        "THANK YOU!":
            show wildmyst at center #shocked
            with move
            show main at left #neutral
            with moveinbottom
            wm "That's right! Let's shout our excitement from the hilltops. YAY!"
            mc "HOORAY?"
    show wildmyst at right #neutral
    with move
    wm "SO! My name is Wild Myst and you are the new Witch of the Watch."
    show main #confused
    mc "(Did she just introduce me to myself?)"
    wm "We haven't had a Witch of the Watch visit our world for a really long time!"
    menu questionleadership:
        "So, you're in charge around here?":
            wm "Yep, basically. I'm the Witch who controls the craft of magic and I lead this world."
        "Wild Myst is a COOL name!":
            show wildmyst #happy
            wm "I know, right? A fitting name for the Witch of magic-craft and leader of this amazing world!"
            show wildmyst #neutral
        "Can you take me to your boss already?":
            wm "Boss?"
            show wildmyst #mad
            wm "HEY! I {i}am{/i} the boss around here!"
            wm "Don't you know a fellow Witch when you see one? I control the craft of magic, so I get to be the leader!"
            mc "Whoopsie."
            show wildmyst #neutral
    wm "Anyway, it's good that you're visiting. This is a place where everyone is free to be themselves and cast magic spells all the time!"
    show wildmyst #angry
    wm "Like a FIRE SPELL!"
    #play sound "fire.mp3" with hpunch
    mc "Aaaah!"
    show wildmyst #neutral
    hide wildmyst
    with moveoutright
    wm "Okay. BYE!"
    show main #confused
    mc "What? Wait!"
    show wildmyst at right #neutral
    with moveinright
    wm "Oh yeah. You probably came here for some reason, right?"
    mc "(Finally.)"
    $ has_magic_intro = True
    menu magicrootdecision:
        "What exactly is a Witch of the Watch supposed to do?":
        "This world is about more than magic, right?":
        "What do you know about the other worlds?":

    return

label philosophyworld:

    scene bg room

    P "Hark! Who enters my lair!?"

    menu:
        "The valient bubble-witch of the fantastically sophisticated nether-realm!":
            jump intro_branch_1
        
        "[Actual cannonical hub world name]":
            jump intro_branch_2

        "That's none of your business!":
            jump intro_branch_3


    label intro_branch_1:
        "Oh, utterly resplendent! A fortuitious parlay, this will be!" :
            jump intro_branch_1 done

    label intro_branch_2:
        "Ah, I see. A grave undertaking indeed." :
            jump intro_branch_2 done

    label intro_branch_3:
        "Oh, how unfortunate you conceal things from me! But if that is how you choose"
        "to approach, so be it!" :
            jump intro_branch_3 done

    P "And what is your import?"

    loopy_phil_1 = False
    label sticking_loop1:
        menu:
             $ if loopy_phil_1 == True:
                "Well, what are you, then!?"
                $ break
            
            "Sir, I'm not a delivery driver!":
                jump sticking_loop1
                 $ loopy_phil_1 = True

            "I'm nobody.":
                jump sticking_response_1

            "I don't know. A book said I was important.":
                jump sticking_response_2

            label sticking_response_1:
                "Well, that's no way to treat yourself! come! have a chat!"
                jump sticking_loop1 done
            
            label sticking_response_2:
                "Ah, and yet your title flatters you so! I suppose the training was never
                quite transparent"
                jump sticking_loop1 done

        

    return
