# The script of the game goes in this file.

# variables
$ mc_name = ""
$ has_magic_philo = False
$ has_philo_philo = False
$ has_industry_philo = False
$ has_magic_intro = False
$ has_witch_watch_info = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define G = Character("Witch of Gluttony", image='LegallyDistictPinkBlob.png', kind=bubble)
define mc = Character(mc_name, image='main.png', kind=bubble)
define sr = Character("Sapona Ramune", image='', kind=bubble) #placeholder name
# define wm = Character("Wild Myst", image='whatever.png', kind=bubble)
define P = Character("Witch of the Mind", image='LegallyDistictPinkBlob.png', kind=bubble)

image Glutton = "LegallyDistinctPinkBlob.png"
image main = "main.png"
image sapona = ''

# defining consistent transforms for use

transform rightish:
    xalign 0.75
    yalign 1.0
transform leftish:
    xalign 0.25
    yalign 1.0

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
    show main at left
    with moveinleft
    "You slip through the membrane, into another sphere."
    "A soft neon glow fills your vision."
    "After some time of aimless wandering, a large black limo abruptly pulls in front of you"
    "Out from the vehicle steps an imposing, but clean-cut creature"
    show sapona at right
    with moveinright
    sr "Welcome, traveller"
    sr "What brings you to our grand metropolis?"

    #first branch, no consequense
    menu sci_main_menu:
        "I'm just looking around, I was curious about this world.":
            sr "I see. I'm flattered to have piqued your interest"
        "I'm bored. This place looked interesting":
            #show sapona happy
            sr "Well you've come to the right place!"
            sr "Come and stay a while in one of our fantastic luxury hotels!"
            sr "Buy a souvenir, and stimulate the local economy!"
        "I think it must have been fate that guided me here":
            sr "If one believes in such things, I suppose."
            sr "This {i}is{/i} a land of opportunity"

    



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
            show wildmyst #angry
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
        "What exactly is a Witch of the Watch supposed to do?" if (has_witch_watch_info == False):
            jump witchwatchinfo
        "This world is about more than magic, right?":
            jump magicworldexposition
        "Are there any problems in this world I should know about?":
            jump magicworldproblems
        "I have to go now.":
            show wildmyst #shocked
            wm "WHAT?! ALREADY?!"
            mc "Yep."
            show wildmyst #neutral
            wm "Okay. Come back soon."
            hide main
            with moveoutleft
            "You step back into the portal."
            jump start

label witchwatchinfo:

    wm "Ummm... it's been a long time, so I'm not really sure."
    show wildmyst #happy
    wm "I remember them visiting and asking questions. I got to show them around!"
    show wildmyst #angry
    wm "It's nice to have visitors as long as they aren't STUPID or always JUDGING us!"
    show main #happy
    mc "Well, I'm not planning on being stupid or judgemental on this visit. Maybe next time."
    show wildmyst #neutral
    wm "Good. Haha."
    wm "..."
    show wildmyst #shocked
    wm "WAIT! I remember something else."
    wm "One Witch of the Watch used to say something about \"the bubble bursting\" but I never knew what they meant."
    show main #confused
    mc "Yeah. That's pretty vague."
    show wildmyst #neutral
    wm "Sorry I don't remember anything else."
    menu witchwatchinforeaction:
        "Well, you still gave me a little bit of context.":
            wc "Yeah, I guess."
            wc "..."
            show wildmyst #angry
            wc "FIRE SPELL!"
            #play sound "fire.mp3" with hpunch
            hide main
            with moveoutbottom
            mc "Aaaah!"
            show wildmyst #happy
            wm "That always makes me feel better."
            show main at left #confused
            with moveinbottom
        "How uninformative.":
            show wildmyst #angry
            wm "That's RUDE. You said you WEREN'T going to be JUDGEMENTAL!"
            mc "Whoopsie."
            show wildmyst #neutral
        "YOU were very HELPFUL!":
            show wildmyst #happy
            wm "I KNOW!"
            show wildmyst #neutral
    $ has_witch_watch_info = True
    jump magicrootdecision

label magicworldexposition

    show wildmyst #happy
    wm "You'd better believe it, FRIEND!"
    wm "Come with me and I'll show you around."
    hide wildmyst
    with moveoutright
    hide main
    with moveout right
    mc "Sure. That sounds like an idea."
    show wildmyst at leftish #neutral
    with moveinleft
    show main at left #neutral
    with moveinleft
    "Wild Myst whisks you off to the centre square of a town nearby."
    wm "This is where we sentence misbehaving citizens to SWIFT justice!"
    show wildmyst #shocked
    wm "In this world, you aren't allowed to make fun of anyone or judge anyone or tell anyone they can't be who they are!"
    show wildmyst #angry
    wm "And when people break the rules, I take their magic away."
    menu magictourquestion:
        "That seems fair.":
            #
        "Then what do you do with them?":
            show wildmyst #shocked
            wm "They aren't allowed to participate in society anymore, so I put them in a smelly cave."
            show main #confused
            mc "For how long?"
            wm "Hmmm... I'm not really sure. Long enough to teach them a lesson I guess."
            mc "Do you ever restore their magic to them?"
            wm "NO! They were mean, so being allowed out of the cave is good enough for them."
            # quick menu choice about agree or disagree
        "Yes! Make them feel JUSTICE!":
            #


    # slightly branched conversation to learn about and reveal magic world's "idea" goes here

label magicworldproblems

    # highly branched conversation to find opportunity to present philosophy world's "idea" goes here

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

        

