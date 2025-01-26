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
default magic_tour_suspended = False
default done_magic_tour = False
default has_industry_intro = False
default is_solved_industry = False
default is_solved_magic = False
default is_solved_philo = False
default has_skipped_sciphilodialogue = False #if the player doesn't bother to ask the right question, makes it so they don't need to go menuing to find it again
default knows_industry_issue = False #if the player has discovered the problem facing the world, hey can bring it up again without the menus
default industry_bored = False #if the player answers boredom for why they entered science world, they get a sales pitch.
default has_witch_watch_info = False
default challenge_time = False
default loopy_phil_1 = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mc_name]", image='main.png', kind=adv, color="#DDDDDD")
define b = Character("Book", kind=nvl)
define sr = Character("Sapona Ramune", image='sapona.png', kind=adv, color="#0066FF")
define wm = Character("Wild Myst", image='wildmyst.png', kind=adv, color="#FF0000")
define P = Character("Loopy Phil", image='phil.png', kind=adv, color="#00BB00")
define V = Character("Loopy Phil", image='phil.png', kind=nvl, color="#00BB00")
define r = Character("rat.jpg")

image main = "main.png"
image sapona = "sapona.png"
image wildmyst = "wildmyst.png"
image phil = "phil.png"
image granite = "granite.png"
image rat = "rat.jpg"

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
    show main at leftish
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
            show main at rightish
            with moveinbottom
            hide main
            with moveoutleft
            show main at leftish
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
    b "Sorry I can't write more; I'm running out of time."
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
        "To the left-most world.":
            $ current_jumps += 1
            jump scienceworld
        "To the middle world.":
            $ current_jumps += 1
            jump magicworld
        "To the right-most world.":
            $ current_jumps += 1
            jump philosophyworld

    # This ends the game.
    # Probably simplify things by using the separate hub_world label below and not jumping back to this start label.

    return

label hub_world:

    scene bg hub with dissolve
    play music "hub.mp3"
    "You return to your home, the empty interdimensional space."
    mc "Where to next?"
    if current_jumps >= max_jumps:
        if (has_industry_philo and has_magic_philo) or (has_industry_philo and has_philo_philo) or (has_magic_philo and has_philo_philo):
            jump ending
    menu travelagain:
        "To the left-most world.":
            $ current_jumps += 1
            jump scienceworld
        "To the middle-most world.":
            $ current_jumps += 1
            jump magicworld
        "To the right-most world.":
            $ current_jumps += 1
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
        "After some time of aimless wandering, a large black limo abruptly pulls in front of you."
        "Out from the vehicle steps an imposing but clean-cut creature."
        show sapona at right
        with moveinright
        sr "Welcome, traveller."
        sr "What brings you to our grand metropolis?"

        #first branch, no consequense
        menu sci_initial:
            "I'm just looking around. I was curious about this world.":
                sr "I see. I'm flattered to have piqued your interest."
            "I'm bored. This place looked interesting.":
                #show sapona happy
                sr "Well you've come to the right place!"
                sr "Come and stay a while in one of our fantastic luxury hotels!"
                sr "Buy a souvenir, and stimulate the local economy!"
                $ industry_bored = True
            "I think it must have been fate that guided me here.":
                #show sapona angry
                sr "If one believes in such things, I suppose."
                sr "This {i}is{/i} a land of opportunity."
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
                sr "I am the Witch of the City..."
                sr "Patron of industry, and Bringer of prosperity."
                sr "I run this world with a cold, unbiased, and concrete hand..."
                #show sapona
                sr "...and as a result, my people are the wealthiest among the spheres."
                label sci_whoareyou:
                    if has_industry_philo==False:
                        $ has_skipped_sciphilodialogue = True
                    menu:
                        #show sapona
                        "What is a \"Witch\"?":
                            #show sapona angry
                            sr "{i}You{/i} are a Witch, Little Witch of the Dead Sphere."
                            #show sapona
                            sr "You are not the first. They tend to come and go somewhat aimlessly."
                            jump sci_whoareyou
                        "Tell me more about your business philosophy.":
                            #show sapona happy
                            sr "Very wise of you to seek my council, Witch of nothingness."
                            sr "Perhaps with my guidance you can breath some life into that empty world of yours."
                            #show sapona
                            sr "First and foremost is efficiency."
                            sr "A good Witch will not tolerate waste."
                            sr "Try new things, yes; that is the only way to prevent stagnation."
                            sr "But do not allow a failed product line to drag down your entire business."
                            sr "As soon as something stops working, you have to change it..."
                            #show sapona angry
                            sr "...or scrap it entirely"
                            "{cps=15}{color=#0066FF}You learned the ways of the Science World!{/color}{/cps}"
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
                sr "...er, well, most of them will."
                sr "I do apologise. This is a somewhat inconvenient timing."
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
                sr "Certain {i}lazy{/i} individuals have got it in their heads that they need..."
                "Sapona leans in and states in a low whisper:"
                #show sapona happy
                sr "{i}...vacation days!{/i}"
                sr "I know. It's absoultely absurd, right?"
                sr "I mean, it's not like they aren't paid well enough."
                sr "You'd think with this much compensation they would be chomping at the bit to come in."
                $ knows_industry_issue = True
                menu sci_issue:
                    "Scandalous! I can't believe there are people who could be so impertinent.":
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
                        "Just as you think steam might start shooting out of their ears, Sapona suddenly calms themself."
                        #if we could pause the music here, that'd be cool
                        #show sapona
                        sr "..."
                        #show sapona happy
                        sr "Please, oh enlightened one."
                        sr "Inform me on what {i}you{/i} think is going on."
                        jump sci_conflict

                menu sci_conflict:
                    "I'm not quite sure yet":
                        sr "Then come back to me when you ARE sure."
                        sr "Time is money, and I don't appreciate having mine wasted."
                        jump sci_main
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
                                "{cps=15}{color=#0066FF}You helped the Magic World get out of their bubble!{/color}{/cps}"
                                $ is_solved_industry = True
                                jump sci_solved
                    "How can you really be sure the reason for this strike is the lack of vacation days?" if has_philo_philo:
                        #show main
                        mc "You have to think about this rationally."
                        mc "What reason do you have to believe that these workers are telling you the truth?"
                        mc "If you are to come to any sort of concrete conclusion you have to start at base principles."
                        mc "To start, you have to rule out the possibility you are living in a dream concocted by some evil imp..."
                        #show sapona
                        sr "..."
                        sr "Get out of my world."
                        "Sapona manifests a portal directly behind you, and sends you through it with a solid kick to centre mass."
                        jump hub_world

            "Tell me more about this hotel." if industry_bored:
                #show sapona
                sr "I'm glad you asked! only the finest accomodations are available for our esteemed guests."
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
            
            "Can I leave?":
                sr "I can't keep you here, if you must go."
                sr "At least buy something on the way out, will you?"
                jump hub_world


    label sci_solved:
        #do color change stuff
        "With those words, you feel a weight in the air lift."
        "A subtle change in the atmosphere..."
        "A shift in your perception..."
        "You think you have done something good."
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
            jump finaltourstop
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
    with moveoutright
    hide main
    with moveoutright
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
    show wildmyst at rightish #neutral
    show main at right #neutral
    with moveinright
    "Next, you descend the hill and come to a stop outside the entrance to a mineshaft."
    "We have mines like this all over our world. It's where we get our maginesium from."
    menu maginesiumquestion:
        "Maginesium? What's that, exactly?":
            wm "I'm glad you asked."
        "Sounds like some sort of vitamin.":
            show wildmyst #shocked
            wm "NO! It's not a VITAMIN!"
            show wildmyst #neutral
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
        show wildmyst at leftish #neutral
        show main at left #neutral
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
        wm "So, you see. There are some rules about what people can do here, but it's only to protect true freedom."
        wm "The collective is important, but it's made up of individuals."
        wm "Here, we NEVER forget the importance of individual freedom, and collective unity arises from that."
        wm "Happy people make better societies. Don't you think?"
        show main #confused
        mc "I'm a bit too much of an amnesiac to know for sure, but I certainly understand this world better now."
        show wildmyst #happy
        wm "YEEHAW!"
        show main #neutral
        "{cps=15}{color=#FF0000}You learned the ways of the Magic World!{/color}{/cps}"
        $ has_magic_philo = True
        hide main
        hide wildmyst
        with moveoutleft
        mc "Let's go back outside."
        show main at left #neutral
        show wildmyst at right #neutral
        with moveinbottom
        jump magicrootdecision


    # slightly branched conversation to learn about and reveal magic world's "idea" goes here

label magicworldproblems:

    $ done_magic_problem_intro = True
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
    wm "My people recently discovered a new vein of maginesium, the resource that powers our magic, deep underground."
    show wildmyst #happy
    wm "It's the biggest deposit ever found, which is actually PRETTY exciting!"
    show wildmyst #shocked
    wm "But it runs under the lands of many different towns and farms..."
    wm "So it's not clear who should have the right to start mining the maginesium."
    wm "And two competing groups have formed, claiming the resource belongs to them."
    show wildmyst #angry
    wm "They've actually started FIGHTING with MAGIC!"
    wm "It's FIRE SPELLS all over the place!"
    play sound "fire.mp3"
    with vpunch
    mc "Aaaah!"
    show wildmyst #neutral
    wm "Like that one."
    menu badadvice:
        "Can't you just use your powers to mine the resource yourself?":
            wm "I could, but that wouldn't make anyone happy. I try to work with my people where I can."
        "Can't you just punish the people who have started fighting?":
            wm "Normally, I would, but too many people are involved now."
    wm "Usually, I have a very clear picture of what is right and what is wrong."
    show wildmyst #shocked
    wm "But both sides are huge! And I can't decide which one is right..."
    show wildmyst #neutral
    wm "I've never had to deal with anything like this before."
    hide wildmyst
    with moveoutbottom
    wm "DARN!"
    mc "(She's thrown herself to the ground and is now lying in a pitiful heap.)"
    mc "Hey, I'm sure every problem can be solved."
    mc "Maybe I can help?"
    show wildmyst at leftish #happy
    with moveinbottom
    wm "YES! You're a Witch of the Watch! You've come to help us in our hour of NEED!"
    wm "PLEASE! Tell me you know what to do!"
    menu solvemagic:
        "Actually, I don't have any ideas right now.":
            wm "Awww..."
            show wildmyst at right
            with move
            wm "Well, on the off chance that you come up with something, please let me know."
            mc "'Kay."
            $ magic_problem_suspended = True
            jump magicrootdecision
        "I learned something from another world that might help." if has_philo_philo:
            $ magic_problem_suspended = False
            show wildmyst at center
            with move
            wm "Another world? Really?"
            show wildmyst #angry
            wm "But those scientists and philosophers are so SNOOTY! They don't know ANYTHING about love or justice!"
            mc "Maybe not, but the philosophers do know something about ideas."
            show wildmyst #neutral
            mc "You're seeing your problem in black and white. You think you have to make a moral judgement between only two possibilities."
            mc "But the philosophers would tell you that there are always infinite possibilities, shades between extremes."
            wm "What?!"
            mc "Being just doesn't mean being rigid."
            mc "Find the fairest solution by giving yourself FREEDOM to explore the nuance."
            wm "Well, I do like freedom."
            wm "Hmmm... Let me think..."
            hide wildmyst
            with moveoutbottom
            show wildmyst at right
            with moveinright
            hide wildmyst
            with moveoutbottom
            show wildmyst at center
            with moveinright
            hide wildmyst
            with moveoutbottom
            show wildmyst at right #happy
            wm "OKAY! You convinced me."
            show wildmyst #neutral
            wm "Maybe I could find a way for the groups to share the mine?"
            mc "Yep. Or you could ask if any of them have ideas to fairly decide the issue. Trust in them."
            wm "Yeah..."
            wm "..."
            wm "Well, I have to say that I'm feeling a lot better, like I can lead my people through the next steps!"
            show wildmyst #happy
            wm "Actually, it makes me so happy that..."
            wm "FIRE SPELL!"
            play sound "fire.mp3"
            with vpunch
            mc "(Huh. That didn't surprise me at all. Guess I got used to it.)"
            wm "Seriously... just..."
            show wildmyst at left
            with move
            play sound "thud.mp3"
            with hpunch
            hide main
            with moveoutleft
            wm "THANK YOU SO MUCH!"
            menu thankyou:
                "... ... ... you're welcome.":
                    pass
                "No problem, fellow Witch.":
                    pass
                "HAPPY TO DO IT!":
                    pass
            show wildmyst at right #neutral
            with move
            wm "I guess... the other worlds have some good ideas after all..."
            "Deep down, you feel you have achieved something important - something you were meant to do."
            show main at left
            with moveinbottom
            $ is_solved_magic = True
            "{cps=15}{color=#FF0000}You helped the Magic World get out of their bubble!{/color}{/cps}"
    jump magicrootdecision
    # highly branched conversation to find opportunity to present philosophy world's "idea" goes here

label philosophyworld:


    # all philosophy world scripting goes here


    play music "philosophy.mp3"
    scene bg philosophy with dissolve

    show main at left
    with moveinleft
    "You step through the portal into a strange, very musty room."
    show phil at right
    with moveinright
    P "Hark! Who enters my lair!?"

    menu:
        "The valient Bubble-Witch of the fantastically sophisticated nether-realm!":
            P "Oh, utterly resplendent! A fortuitous parlay, this will be!"
        
        "[mc_name]":
            P "Ah - well met, Mrs. Sir. Bubbleton!"
        
        "That's none of your business!":
            P "Oh, how unfortunate you conceal things from me! But if that is how you choose to approach, so be it!"

    P "And now, what is your purpose? What is your import?"

    menu self_id:   
        "Sir, I'm not a delivery driver!":
            P "...well, what are you, then!?"
            jump self_id

        "I'm nobody.":
            P "Well, that's no way to treat yourself! Come! Have a chat!"

        "I don't know. A book said I was important.":
            P "Ah, is that so? Books are wonderful and give us so much good information, but your information is good, too! We can all learn so much from each other!"

        "I have to go now. My planet needs me.":
            P "Oh, so soon! How inconvenient! Our fun was just beginning to blossom. À bientôt!"
            jump hub_world
    
    if loopy_phil_1 == True:
        "...well, what are you, then!?"
        jump self_id

    P "There are so many wonderful things, and we are all managing our figures and abaci intently to find the figure in the sky!"
    P "And yet, people have so many good ideas of how to find it and what it is, sometimes I don't want the journey to end!"

    P "Now tell me, what is your purpose in seeing me? What brings such a lovely being from the outside to my own wonderful abode?"

    menu first_big_choice:

        "What's happening in this world?" if has_philo_philo == False: # This is how you get the philosophy idea 
            #time cost?
            jump expo_dump

        "Your bourgeois metaphysical thinking is unbecoming of you, comrade!": # This just insults them
            P "{cps=5}That hurts, \"comrade.\"{/cps}" # concerned
            P "Now tell me, what was it that you wanted from me?" # concerned
            jump self_id

        "What's in the sky?": # This leads to a gag exchange
            P "Well, there are many theories..."

            V """
            {clear}
            
            One day, my roommate told me how if you triangulate the velocity of the Austrlabus Valley's teloscope
            quite right, the object is {i}clearly{/i} a magnificent dragon that we must feast to every night, lest he

            {clear}
            
            be lonely and eat us! Of course, I'm so busy with my figures that planning a feast right now seems very hard,
            but of course we must keep him happy! Another friend suggested that the object is a dancing elephant on a tightrope,
            and it's trying to perform to us and keep {i}us{/i} happy! Of course! A evil dragon that's hungry to eat us that
            also a gregarious circus elephant! What an amazing discovery.

            {clear}

            Somebody also decide to roll their Napier's Bones like dice to see what could be deduced, and used the position of three different
            villages' sundials to derive a trigonometric equation that made the object look exactly like a meringue pie! Incredible! And, of course,
            my friend Geoffery used the mass of the amount of cats in the universe divided by the amount of dogs, and looking there, we found someone making
            an outhouse for dragonflies!

            {clear}

            Of course! A vindictive, gregarious dragon-elephant that's also a meringue pie that's building an outhouse for dragonflies on a tightrope
            that also wants to eat and kill all of us if we don't give it enough attention! Isn't science wonderful!?
            """

            menu perplexed_response:
                "Yeah, that's... science.":
                    pass
                "No, that's stupid.":
                    pass
                "So how do you get anything {i}done{/i}?":
                    pass
                "Wow! Amazing!":
                    pass
            P "Yes, that's - wait, what was I saying?"
            jump self_id

        "Have you considered that science should be efficient?" if (has_philo_philo==True) and (has_industry_philo==True): # This leads to solving the problem; requires having learned the lesson from the science witch
            jump challenge_time

    label expo_dump:
        # music gets sad and reflective
        V """

        {clear}

        Well, one day I wasn't, and then I was. There's not much to tell there. Oh, but so much in between! Yes, that's the space I like.
        When I was born, the vivacious place full of life you see was barren, if you can believe it! It was a barren field of grass and dirt, if
        you could believe it, but it stretched out for miles, so many miles you could walk back to the place you started! And see nothing but a planet of grass! 
        One day, I hit my foot on something - something other than the brobdingnagian expanse, anyway - and I saw a little brick with little smaller bricks inside of it. 
        There was nothing there, of course, but my mind knew the word: book. I read the {i}book{/i} and it told me I was the "Witch of the Mind," whatever that meant. 
        It said I was in charge of this world and that it must be shaped and filled with people.

        {clear}


        I didn't know what "people" meant before I wasn't the only one, of course. But for the time being, I started to make rules for this place: "an object in motion must
        stay in motion," "eukaryotic cells have nuclei," that sort of thing. Eventually, from these rules, other people were made. At first, I talked to them about the way people
        should treat each other. At first it was simple: "don't hurt people." But then others starting to say, "don't do things that cause harm." Our minds started to rail against each
        other, and eventually, philosophy was born from that dialectic. I was so invested, I started to forget the rules. Eventually, we figured out how to work through them, though.
        That was science. Science was hard, but it was hardest for me, because I was remembering what I had forgotten. I began to mourn my lost memories.

        {clear}


        I saw people making mistakes; doing the wrong things. They challenged me, and sometimes they were right, but I was impatient with them and, really, myself. I started to
        rule them with a rod of iron, enforcing on them a strict sense of justice and a need to adhere to the rule of their superior in the hierarchy that I put myself on top of.
        It worked, to some extent: people got things done. But they also grew fearful, so fearful they weren't really able to go any further with things. I began to realize that I
        was hurting them because I was hurt, not because they needed it. I realized that people need autonomy, so I gave them that.

        {clear}


        They got better after they had a sense of self, and after we all realized that complicated things have nuance.

        """
        # music returns to normal
        # elated
        P "So now, I take everyone's ideas seriously, no matter how absurd! People might be wrong sometimes, but by and large they're smart and capable!"
        P "You never know where genius can strike! All it takes is a little trust, and people can do wondrous things!"
        P "Now we spend our days chasing the wildest fancies our eyes and our abaci can detect. Like now, with the celestial object!"
        P "We don't really care for outsiders. We get so excited, we don't really need anyone else!"
        # neutral
        P "Besides, some of them..."
        # concerned
        P "...act like I used to be."
        #  elated
        P "So, are you all caught up?"

        menu expo_dump_react:
            "That was... traumatising.":
                P "well, that..." # neutral
                # conerned
                # beat
                P "{cps=15}...yeah, that was a lot."

            "Your words fly like a finch! Hence, you are amazing!":
                P "I am, aren't I!? And so are you!!"

            "Thanks, doofus!":
                P "I {i}am{/i} a doofus! What a fun word to say! You sure are a clever one, Mrs. Sir. Bubbleton!"

            "I'm gonna be honest: I absorbed {i}none{/i} of what you just said.":
                P "Well isn't that wonderful!? Isn't it {i}amazing{/i} how there's always something else to learn!?"
        
        "{cps=15}{color=#00BB00}You learned the ways of the Philosophy World!{/color}{/cps}"
        $ has_philo_philo = True

        P "Now - where were we, again?"
        jump self_id

    label challenge_time:
        
        # concerned
        P "\"Efficiency\"? What about \"efficiency\"? Eveyone will get what needs to be done in their time!"
        P "There's really no need to rush things here. We'll all get through it in the end!"

        menu first_challenge:

            "You know what, you're right. Forget about it.":
                P "Yeah, that's right! We'll get there!" # elated
                P "We just need to consider {i}everyone's{/i} ideas, and {i}then{/i} we'll get this celestial object thing sorted out!"
                # concerned
                # beat
                P "Now, tell me about yourself!" # elated
                jump self_id

            "You need to be ruthless. You need to be cunning":
                P "I..." # neutral
                P "...I can't be like like that again. I need to be better than that." # concerned
                P "Tell me - just who are you?"
                jump self_id

            "Science has to be replicable. You need to fail to succeed. That's {i}real{/i} autonomy":
                pass

            "You're not getting ANYTHING DONE! GROW A SPINE!":
                P "I don't have a spine! I'm a Bubble Witch!"
                P "It would be interesting to have one, though - great suggestion!"
                P "Tell me again - are you a Bubble Witch?"
                jump self_id

        P "That..."
        P "...is true actually. I suppose it wasn't very scientific of me to neglect critical thinking like that."
        P "But I know all too well the pitfalls of a real \"leader's\" leader. Tell me: how can I not be like that again?"

        menu second_challenge:

            "Get ahold of yourself. Make the big decisions. Others are too weak and stupid to.":
                P "I.."
                P "...you know that's not true."
                P "Tell me - who are you to say that!?"
                jump self_id

            "Train others to be leaders in their own right. Trust them to fail and {i}learn{/i}":
                pass

            "Exactly the way you are! You're perfect!":
                P "I am, aren't I!?"
                P "And so are you!! <3"
                P "Yes, you - wait, who are you?"
                jump self_id

            "You can't. You're doomed to a life of spinning in circles.":
                P "That..."
                P "...I don't want to believe that."
                jump self_id

        P "You know what, that makes sense. But that still means {i}I{/i} have to be a leader. And when I lead, I hurt people."
        P "I don't want to do that agaain."

        menu third_challenge:

            "HURT THEM. THEY MUST LEARN!":
                P "..."
                jump self_id

            "Don't try! You're amazing the way you are and so are your people!":
                P "Thank you!"
                P "And to whom do I owe the honour?"
                jump self_id

            '"Sticks and stones may break your bones, but words can never hurt me.':
                P "I..."
                P "...I don't know if I can trust you on that."
                P "And who is you? Is you you? Are me me?"
                jump self_id

            "Not all challenge is abuse. Philosophy needs rigorous debate.":
                pass

        V """
        You're right. It was that debate that sparked all the good that people did: the arguing,
        the fierce determination, and yet the genuinely kind ones always manage to synthesize things
        and make things more that their parts. I understand. But I need to know: how can I trust myself
        enough to trust I won't do what I did to my people again?
        """

        menu final_challenge:

            "Because you're great! I know you'll be great!":
                P "I..."
                P "...yeah"
                mc "I know you'll be great because I am..."
                jump self_id

            "Because you know more than anyone.":
                P "I..."
                P "...guess..."
                P "...except I can never even remember who you are!"
                jump self_id

            "Because {i}I{/i} trust you":
                P "Yes, but..."
                P "...that doesn't feel like enough."
                jump self_id
            
            "You need to take some time to think. Really {i}listen{/i} to yourself for once.":
                pass
        V """
        You're right. I knew how to talk, and be jovial and accept people. And I learned how to trust
        people. But I forgot how to think, and that makes me a bad scientist and philosopher. I haven't
        really thought in a while. I got so caught up in all the different ways of doing things, I forgot
        to do those things. But those days are over. I'm going to take a stand, and stand with the people
        I haven't always stood with, whether because I was mean or I was neglectful. No more. We are going to
        find this object, and now {i}exactly{/i} what it is, {i}scientifically!{/i}! And you know what? If 
        I can help other worlds out, I'll open my arms to them, too! Trust and challenge: that is the essense of being human!
        """

        "{cps=15}{color=#00BB00}You helped the Philosophy World get out of their bubble!{/color}{/cps}"

        $ is_solved_philo = True

label ending:

    play music "rock.mp3"
    scene bg hub with dissolve

    show main at center
    with moveinbottom
    "You have a bad feeling about this. This place feels unfamiliar, unstable, somehow. And was that rock always so close!?" # earthquake SFX
    play sound "fire.mp3"
    with hpunch
    "You see another book has arrived for you. At a loss of what to do, you decide to read what's there." # more violent earthquake SFX

    b """
    
    Hi there! Hope the job's going okay, and you're settling in! Just a quick thing you need to know:

    {clear}

    The entire multiverse has been collapsing the entire time you've been on the job, and we're all going to 
    die if we don't stop an interdimensional moon from destroying all worlds. 

    {clear}
    
    Sorry, should have lead with that! 
    
    {clear}

    We call it the Literal-Embodiment-of-Hate-Rock here because, well, it starting coming at us when the bubble witches outside of
    the interdimensional realm started to isolate themselves and become fearful of others' ideas. No idea how {i}that{/i} happened! 
    Again, so sorry! Thankfully, though, it's both the literal embodiment of hate {i}and{/i} a rock! Which means: you just need to 
    get some of the bubble witches together and blow it up! Of course, if you could get at least a core trio of them together to 
    ward it off forever, that would be ideal.

    {clear}

    Don't worry, though! If you get at least two of them together, at least that much should be enough of a starting point to start off with!
    Again, again, sorry, sorry! It's just so weird adjusting to being a transcendental essence that can only communicate cryptically! Ciao brutta!

    {clear}

    But, wait, did you not do good on getting everyone together?
    """

    "Well..."
    "...that's not ideal."
    
    "A strange sense of finality fills the air."
    "That celestial object between the shperes..."
    "The one that draws nearer at every breath"
    "You suddenly understand that it's approach is inevitable"
    mc "That thing is going to destroy us all!"
    menu:
        "Contact the witches!":
            pass
        "Somebody save me!":
            pass
        "Heh, I can handle it alone.":
            "You could {i}not{/i} handle it alone."
            "GAME OVER"
            "RETRY THAT LAST DECISION?"
            menu:
                "Yeah, sure.":
                    jump ending
                "Nah, I'm too cool for school, even if it kills me.":
                    return
    if is_solved_industry and is_solved_magic and is_solved_philo:
        jump good_end
    elif is_solved_industry==False:
        jump magic_philo_end
    elif is_solved_magic==False:
        jump philo_industry_end
    elif is_solved_philo==False:
        jump magic_industry_end
  
label magic_philo_end:
    "You contact your allies in the worlds of magic and philosophy."
    "Working together, you hatch a genius plan."
    show phil
    with moveinright
    "Loopy Phil and the academy calculate the exact size, diameter, mass, distance and trajectory of the object."
    hide phil
    with moveoutright
    show wildmyst
    with moveinright
    "While Wild Myst rounds up a posse of fire mages to blast that varmint outta the sky." 
    hide wildmyst
    with moveoutright
    "Unfortunately, without transportation, the team is unable to travel close enough to intecept at a safe distance."
    "Instead, the team waits until the object has almost struck them, then obliterates it with supreme power and precision."
    "The shrapnel from the blast rains down on the spheres, causing widespread destruction."
    "Regardless, nothing is lost that cannot be rebuilt."
    jump fin_screen

label philo_industry_end:
    "You contact your allies in the worlds of science and philosophy."
    "Working together, you concoct a wily scheme."
    show phil
    with moveinright
    "Loopy Phil and the academy calculate the exact size, diameter, mass, distance and tragectory of the object."
    hide phil
    show sapona
    with moveinright
    "While Sapona and the worker's union manufacture a ship to intercept it."
    hide sapona
    with moveoutright
    "Unfortunately, with inadequate firepower, the team can't permanently destroy it."
    "Instead, the team sends the starship on a collision course with the celestial threat."
    "Striking with precise force and velocity, its approach vector changes enough to barely miss the spheres."
    "However, the sheer mass of the thing causes powerful tidal shifts as it passes."
    "Tsunamis and earthquakes plague the worlds, but eventually they cease."
    "While there is widespread destruction, it is nothing that can't be rebuilt."
    jump fin_screen
    
label magic_industry_end:
    "You contact your allies in the worlds of magic and philosophy."
    "Working together, you figure yerselves a solution."
    show wildmyst
    with moveinright
    "Wild Myst rounds up a posse of fire mages to blast that varmint outta the sky." 
    hide wildmyst
    with moveoutright
    show sapona
    with moveinright
    "While Sapona and the worker's union manufacture a ship to intercept it."
    hide sapona
    with moveoutright
    "Unfortunately, without proper intel, you are unable to triangulate the exact location of the object."
    "The fire mages load a powerful spell onto the ship, but have to constantly correct their course as they go."
    "By the time they reach it, the object is too close to avoid collateral damage."
    "A close-range blast vaporizes the threat, but the excess heat bakes the surface of the worlds."
    "The blinding warmth lasts but a moment, just long enough to cause widespread crop failures among the spheres."
    "Times are tough for a while, but you are confident that eventually everyone can pull through."
    jump fin_screen
    
label good_end:

    "And wait.." # flash
    show main at left
    with move
    "is that..." # flash
    show sapona at leftish
    show wildmyst at rightish
    show phil at right
    with moveinbottom
    "YES!! Some of your friends have come!" # flash if you got the good ending.

    P "You..."
    wm "You..."
    sr "You..."

    P "It's been a long time since I could see anyone so bellicosely close-minded..."
    wm "Well, it's been a long time since I've seen anyone so cold hearted..."
    sr "Speak for yourselves! I would {i}never{/i} hire workers as lackadasical as you lot!"

    P "Yet, despite our differences, we need to come together, because I don't have the resources to do this myself."
    P "I need to learn to trust you."

    wm "And I think all y'all's plans are STUPID and if we just had a bit more time I'm sure I could get a big FIREBALL BLAST to DESTROY everything!"
    wm "But, I suppose I don't have time to figure that one out, so I guess I need to trust y'all to take me down a notch so we can do this quickly."

    sr "Harumph! As if I'd be able to trust the likes of you!"
    sr "But I guess people need to be able to ask for help while getting their own backyard trimmed..."
    sr "So I suppose I can step back on the latter and put a foot forward on how to do the former."

    "Finally! People behaving like {i}people{/i}!"

    P "My people and I have triangulated the location of Mr. Ma'am Mean Moon, as well as where it's going."
    P "With the skills from your realms, its days are as numbered as there are cats in the ocean!"

    sr "Hmph! This \"end of the world\" business is uninteresting in the extreme!"
    sr "But it's bad for profits, and without some concessions I'll end up with riots and eternal death."
    sr "Very well, my infrastructure and labour reserves are at your beck and call. My engineers have proposed a rocket."

    P "I've already sent my engineers to help yours, Noodle-kun! I can't wait to work together after so much time alone!"

    sr "I can't say I will return the favour. But yes, this partnership will be..."
    sr "...interesting, and dare I say..."
    sr "...fun."

    wm "Well, what are we waiting for!?"
    wm "My maginesium loaded onto that baby is going to EXPLODE THAT DUMB ROCKET'S FACE INTO SMITHEREENS!!!"

    P "Well put, Wintery Mint! This gargantuan granite is no mach for the flowering power of partnership!"

    wm "And, hey, we haven't let the most {i}important{/i} partner speak! [mc_name], you're the {i}real{/i} hero of this story!"

    P "Indeed. Without you, we would never have worked together! Thank you ever so!"

    sr "Pheh. Some congratulations are in order, I suppose."

    mc "...No."

    sr "Pardon?"

    mc "I didn't do anything. I just blubbered about figuring out a job I didn't understand."
    mc "You and the people around you were the ones to put your heads together to actually solve a problem."
    mc "{i}You{/i} are the ones bending heaven and earth to save the multiverse!"

    P "That's true, but we all have our own agency in what happened."
    P "And your part to play, just by talking to people who wouldn't without you, is just as invaluable as any rocket headed to the sky!"

    wm "Yeah, don't beat yourself up! Self-pity is ANNOYING and NOT AWESOME!"
    wm "We all have a part to play in revolutionizing the way we live our lives!"

    sr "Heh. I'm reticent to say it, but the brash one is right..."
    sr "...on most accounts."

    mc "I suppose, on that, I feel..."

    menu I_need_to_go:

        "Jubilant! We've all saved the world!":
            P "Excellent! I'm glad to hear it!"

        "I'm just getting my accounts in order.":
            sr "Good. As we all must."

        "Happy, but also kind of sentimental!? That was so fun!!":
            wm "Yeah, you strangers are so much nicer than I thought!"
            wm "The world should almost end more often!"

        "I did my part, and you did yours. I guess that's all we can do.":
            sr "Yes, we all have our part to play. A good assessment."
            P "We fit in like a puzzle! We challenge, we build, and we grow!"
            wm "Yeeeeeeeeeehawwwwwwwww!"

    mc "We were all in our bubbles before."
    mc "But after stepping out and seeing the world, I think we all kind of know now - people can do anything, as long as they work together!"

    P "Together!"

    wm "Together!"

    sr "Everyone in their place, together."

    jump good_end_narration


label good_end_narration:
    scene bg black with dissolve

    """
    And so, our valiant heroes saved the day, and used all their powers together to stop
    the impending doom of the Literal-Embodiment-of-Hate-Rock. With Loopy Phil's compassion,
    Wild Myst's passionate magic, and Sapona Ramune's...
    ...business...
    ...acumen...
    the stupid piece of granit was blasted to smithereens (Myst's words). You did it!
    But never forget the people who made that possible. Remember: people can only do
    what seems impossible when they work together!"
    """

    # "That said..."

    # jump sequel_bait

    jump fin_screen

label sequel_bait:
    scene granite with dissolve
    sr "Is everything prepared for the market expansion, Mr. Rat?"
    r "Yes, yes, don't rush me!"
    sr "[mc_name] has reminded me of just how lucrative multiverse travel is."
    sr "I've extracted all the profits I can from my world. It's time to expand."
    sr "The gaping maw of capital demands it."

    r "Yes, yes, I'm getting all the systems organized to prepare for your \"business expansion.\" But don't these plans seem to be..."

    sr "I care little for ethics. So long as there is a world, there is profit to be had, and I am prepared to be the one to make those profits."

    r "So you can have a fancier life than you already do?"

    sr "...someone will do this. Be thankful that person is {i}me{/i}."

label fin_screen:
    scene bg fin_screen

    pause 4.0

    return
