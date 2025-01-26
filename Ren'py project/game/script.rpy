# The script of the game goes in this file.

  # variables
default max_jumps = 4
default current_jumps = 0
default mc_name = ""
default has_magic_philo = False
default has_philo_philo = False
default has_industry_philo = False
default has_magic_intro = False
default has_philo_intro = False
default has_industry_intro = False
default magic_tour_suspended = False
default done_magic_tour = False
default is_solved_industry = False
default is_solved_magic = False
default is_solved_philo = False
default has_skipped_sciphilodialogue = False #if the player doesn't bother to ask the right question, makes it so they don't need to go menuing to find it again
default knows_industry_issue = False #if the player has discovered the problem facing the world, hey can bring it up again without the menus
default industry_bored = False #if the player answers boredom for why they entered science world, they get a sales pitch.
default has_witch_watch_info = False


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mc_name]", image='main.png', kind=bubble, color="#888888")
define b = Character("Book", kind=nvl)
define sr = Character("Sapona Ramune", image='sapona.png', kind=bubble, color="#000088")
define wm = Character("Wild Myst", image='wildmyst.png', kind=bubble, color="#880000")
define P = Character("Loopy Phil", image='phil.png', kind=bubble, color="#008800")

image main = "main.png"
image sapona = "sapona.png"
image wildmyst = "wildmyst.png"
image phil = "phil.png"

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

    scene bg black
    play music "hub.mp3"
    "You don't know where you are."
    "It's somewhere dark and silent... but perfectly calm."
    "You force your eyes open."
    scene bg hub with dissolve
    pause 1.5
    "You see void... and floating platforms... and bubbles... and yourself."
    show main at center
    with moveinbottom
    python:
        mc_name = renpy.input("This is you. What is your name?")
        mc_name = mc_name.strip() or "Witchley"
    mc "This place is..."
    menu firstchoice:
        "Weird.":
            mc "I bet the laws of physics don't even apply here."
            hide main
            with moveoutright
            show main at center
            with moveinbottom
            hide main
            with moveoutleft
            show main at center
            with moveinbottom
            mc "Yep. That's what I thought."
        "Depressing.":
            show main #confused
            mc "Maybe I should just go back to sleep and hope this is all a bad dream."
        "Fun!":
            show main #happy
            mc "I wonder if there are any other neat things around here?"
    "You notice a book lying open on the main platform."
    "It reads..."
    b "Dear newest Witch,"
    b "This interdimensional space is your home now."
    b "However, your destiny is elsewhere."
    b "You must bridge the worlds, or all will fall to ruin."
    b "Sorry I can't write more, but I'm running out of time."
    b "Also, I don't really like this pen."
    b "Good luck. Bye!"
    mc "Hmmm... this book makes me feel..."
    menu bookchoice:
        "Spooky. I want to throw it away.":
            "You toss the book into the void, but it just floats there."
            mc "Great."
        "Important. I want to treasure it.":
            "You close the book and gently set it back down in its place on the platform."
            show main #happy
            mc "There. Perfect."
            show main #neutral
        "Frustrated. I want to rip it to pieces.":
            show main #angry
            "You rip the pages of the book apart in a wild frenzy!"
            mc "Yaaargh!"
            "But the pieces just float around and keep poking you in the eye."
            show main #confused
            mc "Yaargh."
            show main #neutral
    mc "Well, I guess I'm supposed to go to those bubbles."
    mc "Where to first?"
    menu travel:
        "To the blue world.":
            jump scienceworld
        "To the red world.":
            jump magicworld
        "To the green world.":
            jump philosophyworld

    # This ends the game.
    # Probably simplify things by using the separate hub_world label below and not jumping back to this start label.

    return

label hub_world:

    scene bg hub with dissolve
    play music "hub.mp3"
    "You return to your home, the empty interdimensional space."
    mc "Where to next?"
    menu travelagain:
        "To the blue world.":
            jump scienceworld
        "To the red world.":
            jump magicworld
        "To the green world.":
            jump philosophyworld    

label scienceworld:

    scene bg science with dissolve
    play music "science.mp3"
    if has_industry_intro==False:
        #introduction
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
        menu sci_initial:
            "I'm just looking around, I was curious about this world.":
                sr "I see. I'm flattered to have piqued your interest"
            "I'm bored. This place looked interesting":
                #show sapona happy
                sr "Well you've come to the right place!"
                sr "Come and stay a while in one of our fantastic luxury hotels!"
                sr "Buy a souvenir, and stimulate the local economy!"
                $ industry_bored = True
            "I think it must have been fate that guided me here":
                #show sapona angry
                sr "If one believes in such things, I suppose."
                sr "This {i}is{/i} a land of opportunity"
        $ has_industry_intro = True
        jump sci_main
    else:
        #main menu, where you go if you have been here already
        #show sapona
        sr "Oh, you again."
        sr "Welcome back. What can I do for you?"
        menu sci_main:
            #show sapona
            "Who are you?":
                #show sapona angry
                sr "Ah, you must be one of the new ones."
                sr "Forgive me, you nothing-witches come and go so often I tend to forget your faces."
                #show sapona happy
                sr "I am the Witch of the City"
                sr "Patron of industry, and Bringer of prosperity."
                sr "I run this world with a cold, unbiased, and concrete hand..."
                #show sapona
                sr "...and as a result, my people are the wealthiest amoung the spheres."
                label sci_whoareyou:
                    if has_industry_philo==False:
                        $ has_skipped_sciphilodialogue = True
                    menu:
                        #show sapona
                        "What is a \"Witch\"?":
                            #show sapona angry
                            sr "{i}You{/i} are a Witch, Little Witch of the Dead Sphere."
                            #show sapona
                            sr "You are not the first, they tend to come and go somewhat aimlessly."
                            jump sci_whoareyou
                        "Tell me more about your business philosophy.":
                            #show sapona happy
                            sr "Very wise of you to seek my council, witch of nothingness."
                            sr "Perhaps with my guidance you can breath some life into that empty world of yours."
                            #show sapona
                            sr "First and foremost is efficiency."
                            sr "A good witch will not tolerate waste."
                            sr "Try new things, yes; that is the only way to prevent stagnation."
                            sr "But do not allow a failed product line to drag down your entire business."
                            sr "As soon as something stops working, you have to change it..."
                            #show sapona angry
                            sr "...or scrap it entirely"
                            $ has_industry_philo = True
                            $ has_skipped_sciphilodialogue = False
                            jump sci_whoareyou
                        "I'd like to ask something else.":
                            sr "If you insist."
                            jump sci_main
            "Where exactly am I?":
                #show sapona happy
                sr "We call it \"The Grand Metropolis\"."
                sr "It is a city of unprecedented wealth and beauty."
                sr "I'm sure you're quite overwhelmed, coming from that dinky little world, where nothing ever happens."
                sr "But don't worry, our industious workforce will ensure you are comfortable and taken care of."
                #show sapona embarrased/neutral
                sr "...er, well; most of them will."
                sr "I do apologise, this is a somewhat inconvenient timing."
                sr "There is a slight hiccup with some of our staff refusing to do their job."
                #show sapona happy
                sr "But I assure you, it's nothing that can't be fixed with high enough overtime pay."
                menu:
                    #illusion of choice lol
                    #also breaks up the monotony of a long exposition if the player has to do something.
                    "Why exactly are people refusing to do their job?":
                        pass
                    "What do you think they want?":
                        pass
                #show sapona angry
                sr "Certain {i}lazy{/i} individuals have got it in their heads they need..."
                "Sapona leans in and states in a low wisper:"
                #show sapona happy
                sr "{i}...vacation days!{/i}"
                sr "I know, it's absoultely absurd, right?"
                sr "I mean, it's not like they aren't paid well enough."
                sr "You'd think with this much compensation they would be chomping at the bit to come in."
                $ knows_industry_issue = True
                menu sci_issue:
                    "Scandalous! I can't believe there are people who could be so impertinent":
                        #show main
                        mc "How could they show such little gratitude for your kindness?"
                        #show sapona
                        sr "My thoughts exactly."
                        sr "You know, I didn't expect to find a kindred spirit in you, Little Witch."
                        sr "But you really have the right additude about things."
                        sr "If you ever tire of ruling over a blank slate, Let me know."
                        #show sapona happy
                        sr "You'd be perfect material for middle management."
                        jump sci_main
                    "I can see how you might think of it that way, but have you considered their point of view?":
                        #show sapona angry
                        sr "And what point of view is that?"
                        jump sci_conflict
                    "What is wrong with you?!":
                        #show main
                        mc "How could you be so callous as to deny your workers vacation days?"
                        mc "You're like some sort of cartoon villain."
                        mc "Like, seriously."
                        mc "If I was reading a book and you were in it, I'd consider the author to be a hack."
                        #show sapona angry
                        "Sapona starts visibly fuming."
                        sr "...I...well I never..."
                        "Just as you think steam might start shooting out of her ears, she suddenly calms herself."
                        #if we could pause the music here, that'd be cool
                        #show sapona
                        sr "..."
                        #show sapona happy
                        sr "Please; oh enlightened one."
                        sr "Inform me on what {i}you{/i} think is going on."
                        jump sci_conflict

                menu sci_conflict:
                    "I'm not quite sure yet":
                        "Placeholder dialogue!!!"
                    "It just ain't right to force people to work that many hours." if has_magic_philo:
                        #show sapona angry
                        sr "You think you know better than me, Little Witch?"
                        sr "What do you know of running a sphere?"
                        sr "Do you have thousands of lives in your hands, depending on you to keep them in house and home?"
                        menu:
                            "I guess not...":
                                #show main
                                mc "I don't really know all that much about business, but it still seems wrong..."
                                jump sci_main
                            "Your commitment to efficiency should compel you to change your stance." if has_industry_philo:
                                #show main
                                #que ace attourney music
                                mc "Overwork is just as large a threat to productivity as lack of work."
                                mc "And currently, due to your callous demeanour, you are experiencing both."
                                mc "You are stuck in a local maximum, your laser-focus has left you unable to see the forest for the trees."
                                #show sapona
                                sr "..."
                                sr "...I had not thought of it that way."
                                sr "I think you may actually be right."
                                sr "Who knew a nothing-witch could be so wise?"
                                $ is_solved_industry = True
                                jump sci_solved
                    "How can you really be sure the reason for this strike is the lack of vacation days?" if has_philo_philo:
                        #show main
                        mc "You have to think about this rationally."
                        mc "What reason do you have to believe that these workers are telling you the truth?"
                        mc "If you are to come to any sort of concrete conclusion you have to start at base principals."
                        mc "To start, you have to rule out the possibility you are living in a dream concocted by some evil imp..."
                        #show sapona
                        sr "..."
                        sr "Get out of my world."
                        "Sapona manifests a portal directly behind you, and sends you through it with a solid kick to centre mass."
                        jump hub_world

            "Tell me more about this hotel." if industry_bored:
                #show sapona
                sr "I'm glad you asked! only the finest accomodations are availible for our esteemed guests."
                sr "We keep them running 24/7, just in case a guest comes along."
                sr "Happens about once a century or so, but the jobs it creates are well worth it anyway."
                sr "Besides, what use is all this wealth if we can't show it off when the opportunity arises?"
                $ industry_bored = False
                jump sci_main

            "About your job earlier..." if has_skipped_sciphilodialogue:
                #show sapona
                sr "What about it?"
                jump sci_whoareyou
        
            "Remember that issue you were talking about?" if knows_industry_issue:
                #show sapona
                sr "Of course. What is it?"
                jump sci_issue

    label sci_solved:
        #do color change stuff
        "With those words, you feel a weight in the air lift."
        "A subtle change in the atmosphere,"
        "A shift in your perception,"
        "You think you have done something good."
        if (is_solved_magic and is_solved_philo):
            "Yay."
            jump hub_world
            # jump best_end
        elif (current_jumps > max_jumps):
            if (is_solved_magic):
                # jump magic_sci_end
                "Whoo."
                jump hub_world
            elif (is_solved_philo):
                # jump philo_sci_end
                "Okay."
                jump hub_world
        else:
            jump hub_world

# THIS COMMENT MARKS THE END OF SCIENCE WORLD
    



label magicworld:

    scene bg magic with dissolve
    play music "magic.mp3"
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
    play sound "thud.mp3"
    with hpunch
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
    play sound "fire.mp3"
    with vpunch
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
        "What exactly is a Witch of the Watch supposed to do?" if has_witch_watch_info==False:
            jump witchwatchinfo
        "This world is about more than magic, right?" if done_magic_tour==False:
            jump magicworldexposition
        "Actually, can we continue that tour?" if magic_tour_suspended==True:
            show wildmyst #happy
            wm "YAY! I knew you secretly LOVED my tour!"
            mc "(That's not really what I said, but sure.)"
            hide wildmyst
            hide main
            with moveoutright
            wm "Let's go!"
            $ magic_tour_suspended = False
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
            jump hub_world

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
            wm "Yeah, I guess."
            wm "..."
            show wildmyst #angry
            wm "FIRE SPELL!"
            play sound "fire.mp3"
            with vpunch
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

label magicworldexposition:

    $ done_magic_tour = True
    show wildmyst #happy
    wm "You'd better believe it, FRIEND!"
    wm "Come with me and I'll show you around."
    hide wildmyst
    hide main
    with moveoutright
    mc "Sure. That sounds like an idea."
    show main at left #neutral
    show wildmyst at leftish #neutral
    with moveinleft
    "Wild Myst whisks you off to the centre square of a town nearby."
    wm "This is where we sentence misbehaving citizens to SWIFT justice!"
    show wildmyst #shocked
    wm "In this world, you aren't allowed to make fun of anyone or judge anyone or tell anyone they can't be who they are!"
    show wildmyst #angry
    wm "And when people break the rules, I take their magic away."
    menu magictourquestion:
        "That seems fair.":
            show wildmyst #neutral
            "Yes. As I said, this is a world of freedom, which you can't have without justice."
        "Then what do you do with them?":
            show wildmyst #shocked
            wm "They aren't allowed to participate in society anymore, so I put them in a smelly cave."
            show main #confused
            mc "For how long?"
            wm "Hmmm... I'm not really sure. Long enough to teach them a lesson I guess."
            mc "Do you ever restore their magic to them?"
            wm "NO! They were mean, so being allowed out of the cave is good enough for them."
            menu magicagreedisagree:
                "I guess that makes sense.":
                    wm "Darn tootin'."
                "What? That sounds cruel!":
                    show wildmyst #neutral
                    wm "I appreciate your opinion. Passionate beliefs are welcome here."
                    show wildmyst #angry
                    wm "But threats to our freedom deserve ZERO tolerance!"
                    mc "(Intense.)"
                    show wildmyst #happy
        "Yes! Make them feel JUSTICE!":
            show wildmyst #happy
            "You really seem to GET what we're all about HERE!."
            show wildmyst #happy
    hide wildmyst
    hide main
    with moveoutleft
    wm "Let's continue the tour."
    show main at right #neutral
    show wildmyst at rightish #neutral
    with moveinright
    "Next, you descend the hill and come to a stop outside the entrance to a mineshaft."
    "We have mines like this all over our world. It's where we get our maginesium from."
    menu maginesiumquestion:
        "Maginesium? What's that, exactly?":
            wm "I'm glad you asked."
        "Sounds like some sort of vitamin.":
            show wildmyst #shocked
            wm "NO! It's not a VITAMIN!"
            show wildmsyt #neutral
            wm "Well, actually it is. Sort of."
        "Ah, of course. I know all about manganese.":
            show wildmyst #angry
            wm "It's not MANGANESE!"
            show wildmyst #neutral
            wm "Manganese is a metallic element used in rubber, glass, ceramics, and stainless steel alloys."
            mc "You sure know a lot about mining."
            show wildmyst #happy
            wm "Yes, I do!"
            show wildmyst #neutral
            wm "Anyway..."
    wm "Maginesium is the root of all magical energy on our world."
    wm "It can be used to make magical artifacts like my super cool badge-wand."
    wm "You can also consume small amounts of it to boost your own magical powers."
    mc "Nifty."
    show wildmyst #happy
    wm "Yes, it is. We have a lot of it here, which is why our world is so AWESOME!"
    show wildmyst
    wm "Okay, I think we can move on to the next part of our tour."
    menu magictourdecision:
        "Goody.":
            pass
        "Actually, I'm pretty bored of this tour.":
            $ magic_tour_suspended = True
            show wildmyst #shocked
            wm "Wha...?"
            show wildmyst #neutral
            wm "That's too bad, but I will respect your choice."
            hide wildmyst
            hide main
            with moveoutright
            wm "Let's go back to where we started."
            show wildmyst at right
            show main at left
            with moveinbottom
            jump magicrootdecision
    hide wildmyst
    hide main
    with moveoutright
    wm "Follow me. The last stop is my FAVOURITE!"

    label finaltourstop:
        show main at left #neutral
        show wildmyst at leftish #neutral
        with moveinleft
        "You descend further into the depths below the hills..."
        "Sweet-smelling steam starts to permeate the air around you."
        show wildmyst #happy
        wm "These are our HOT SPRINGS! I call them the happiest place in our world."
        wm "Here, more than anywhere else, people are free to relax and be their truest selves."
        menu hotspring:
            "Yes, I notice how relaxing the atmosphere is.":
                show wildmyst #neutral
                wm "You are perceptive. There's literal magic in the air from the surrounding Maginesium deposits."
                wm "These springs are a symbol of everything we stand for in this world."
                show wildmyst #angry
                wm "And if anything threatens this place, I will retaliate with EXTREME reprisal!"
                wm "Another FIRE SPELL!"
                play sound "fire.mp3"
                with vpunch
                mc "Aaaah!"
                mc "(Oh, this time the spell just heated up the springs a bit more.)"
            "Indeed, this is clearly a no-shame zone.":
                show wildmyst #shocked
                wm "RIGHT! There's no place for body shame or any other kind of shame in this world!"
                show wildmyst #angry
                wm "EXCEPT when someone tries to stop another person from being free. They can be shamed a LOT!"
            "Ah, I see some people smooching each other.":
                wm "Right. This is a world of freedom and LOVE. If people want to smooch each other, we let them!"
                show wildmyst #shocked
                wm "Standing in the way of love and identity is NOT okay!"
                show wildmyst #angry
                wm "And must be PUNISHED."
        show wildmyst #neutral
        wm "So, you see. There are some rules about what people can do here, but it's only to protect true freedom."
        wm "The collective is important, but it's made up of individuals."
        wm "Here, we NEVER forget the importance of individual freedom, and collective unity arises from that."
        wm "Happy people make better societies. Don't you think?"
        show main #confused
        mc "I'm a bit too much of an amnesiac to know for sure, but I certainly understand this world better now."
        show wildmyst #happy
        wm "YEEHAW!"
        show main #neutral
        "{cps=15}{colour=#880000}You learned the ways of the Magic World!{/color}{/cps}"
        $ has_magic_philo = True
        hide main
        hide wildmyst
        with moveoutleft
        mc "Let's go back outside."
        show main at left #neutral
        show wildmyst at right #neutral
        with moveinbottom
    jump magicrootdecision

label magicworldproblems:

    show wildmyst #happy
    wm "No way! This world is a happy place."
    menu insistmagic:
        "Oh. Okay, then.":
            jump magicrootdecision
        "Come on. There must be SOMETHING!":
            pass
    show wildmyst #neutral
    wm "Well, I don't know... but you asked with such enthusiasm..."
    wm "I guess..."
    show wildmyst #shocked
    wm "I don't know if I can TRUST you!"
    menu insistfurther:
        "Yeah, you probably can't.":
            show wildmyst #neutral
            wm "See? Exactly."
            jump magicrootdecision
        "Please. I think my destiny has something to do with helping you.":
            pass
    wm "Well..."
    wm "I suppose I can trust a Witch of the Watch. They've never done anything to harm us in the past."
    wm "You see... there is one thing..."
    mc "What is it?"
    show wildmyst at center
    with move
    "Wild Myst moves closer and speaks in a quieter voice, so as not to be overheard."

    
    jump magicrootdecision
    # highly branched conversation to find opportunity to present philosophy world's "idea" goes here

label philosophyworld:

    scene bg philosophy with dissolve
    play music "philosophy.mp3"
    "Wow. Time to go back to the Hub World."
    jump hub_world

"""
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
"""
        

