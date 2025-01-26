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

define mc = Character("[mc_name]", image='main.png', kind=bubble)
define b = Character("Book", kind=nvl)
define sr = Character("Sapona Ramune", image='sapona.png', kind=bubble)
define wm = Character("Wild Myst", image='wildmyst.png', kind=bubble)
define P = Character("Loopy Phil", image='phil.png', kind=bubble)
define V = Character("Loopy Phil", image='phil.png', kind=nvl)

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
    #do hub world things

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
                        $ dummyvariable = 1
                    "What do you think they want?":
                        $ dummyvariable = 2
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
                        jump start

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
            jump start
            # jump best_end
        elif (current_jumps > max_jumps):
            if (is_solved_magic):
                # jump magic_sci_end
                "Whoo."
                jump start
            elif (is_solved_philo):
                # jump philo_sci_end
                "Okay."
                jump start
        else:
            jump start

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
        "What exactly is a Witch of the Watch supposed to do?" if has_witch_watch_info==False:
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
            wm "Yeah, I guess."
            wm "..."
            show wildmyst #angry
            wm "FIRE SPELL!"
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

label magicworldexposition:

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
            "Wow."
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
            "Wow."
    jump magicrootdecision


    # slightly branched conversation to learn about and reveal magic world's "idea" goes here

label magicworldproblems:

    "There is nothing here yet!"
    jump magicrootdecision
    # highly branched conversation to find opportunity to present philosophy world's "idea" goes here

label philosophyworld:


    # all philosophy world scripting goes here

    scene bg philosophy with dissolve
    play music "philosophy.mp3"

    P "Hark! Who enters my lair!?"

    menu:
        "The valient bubble-witch of the fantastically sophisticated nether-realm!":
            P "Oh, utterly resplendent! A fortuitious parlay, this will be!"
        
        "[mc_name]":
            P "Ah — well met, Mrs. Sir. Bubbleton!"
        
        "That's none of your business!":
            P "Oh, how unfortunate you conceal things from me! But if that is how you choose"
            P "to approach, so be it!"

    P "And now, what is your purpose? What is your import?"

    menu self_id:   
        "Sir, I'm not a delivery driver!":
            P "..."
            jump self_id

        "I'm nobody.":
            P "Well, that's no way to treat yourself! come! have a chat!"

        "I don't know. A book said I was important.":
            "Ah, is that so? Books are wonderful and give us so much good information, but your information is good, too! We can all learn so much from each other!"

        "I have to go now. My planet needs me.":
            P "Oh, so soon! How inconvinient! Our fun was just beginning to blossom. À beintôt!"
            jump start
    
    if loopy_phil_1 == True:
        "...well, what are you, then!?"
        jump self_id

    P "There are so many wonderful things, and we are all managing our figures and abaci intently to find the figure in the sky! And yet, people have so many"
    P "Good ideas of how to find it and what it is, sometimes I don't want the journey to end!"

    P "Now tell me, what is your purpose in seeing me? What brings such a lovely being from the outside to my own wonderful abode?"

    menu first_big_choice:

        "What's happening in this world?" if has_philo_philo == False: # This is how you get the philosophy idea 
            #time cost?
            jump expo_dump

        "Your bourgeois metaphysical thinking is unbecoming of you, comrade!": # This just insults them
            P '{cps=5}That hurts, "comrade."{/cps}' # concerned
            P "Now tell me, what was it that you wanted from me?" # concerned
            jump self_id

        "What's in the sky?": # This leads to a gag exchange
            P "Well, there are many theories..."

            V """
            One day, my roomate told me how if you triangulate the velocity of the Austrlabus Valley's teloscope
            quite right, the object is {i}clearly{/i} a magnificent dragon that we must feast to every night, lest he
            be lonely and eat us! Of course, I'm so busy with my figures that planning a feast right now seems very hard,
            but of course we must keep him happy! Another friend suggested that the object is a dancing elephant on a tightrope,
            and it's trying to perform to us and keep {i}us{/i} happy! Of course! A evil dragon that's hungry to eat us that'Magic World Dialogue Sample.txt'
            also a gregarious circus elephant! What an amazing discovery

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
            P "Yes, that's — wait, what was I saying?"
            jump self_id

        "Have you considered that science should be efficient?" if (has_philo_philo==True)and(has_industry_philo==True): # This leads to solving the problem; requires having learned the lesson from the science witch
            jump challenge_time

    label expo_dump:
        # music gets sad and reflective
        V '''
        {clear}

        Well, one day I wasn't, and then I was. There's not much to tell there. Oh, but so much in between! Yes, that's the space I like.
        When I was born, the vivacious place full of life you see was barren, if you can believe it! It was a barren field of grass and dirt, if
        you could believe it, but it stretched out for miles, so many miles you could walk back to the place you started! and see nothing but a planet of grass! 
        One day, I hit my foot on something — something other than the brobdingnagian expanse, anyway — and I saw a little brick with little smaller bricks inside of it. 
        There was nothing there, of course, but my mind knew the word: book. I read the, {i}book{/i}, and it told me I was the "Witch of the Mind," whatever that meant. 
        It said I was in charge of this world and that it must be shaped and filled with people.

        {clear}

        I didn't know what "people" meant before I wasn't the only one, of course. But for the time being, I started to make rules for this place: "an object in motion must
        stay in motion," "eukaryotic cells have nuclei," that sort of thing. Eventually, from these rules, other people were made. At first, I talked to them about the way people
        should treat each other. At first it was simple: "don't hurt people." But then others starting to say, "don't do things that cause harm." Our minds started to rail against each
        other, and eventually, philosophy was born from that dialectic. I was so invested, I started to forget the rules. Eventually, we figuered out how to work through them, though.
        That was science. Science was hard, but it was hardest for me, because I was remembering what I had forgotten. I began to mourn my lost memories.

        {clear}

        I saw people making mistakes; doing the wrong things. They challenged me, and sometimes they were right, but I was impatient with them and, really, myself. I started to
        rule them with a rod of iron, enforcing on them a strict sense of justice and a need to adhere to the rule of their superior in the hierarchy that I put myself on top of.
        It worked, to some extent: people got things done. But they also grew fearful, so fearful they weren't really able to go any further with things. I began to realize that I
        was hurting them because I was hurt, not because they needed it. I realized that people need autonomy, so I gave them that.

        {clear}

        They got better after they had a sense of self, and after we all realized that complicated things have nuance.
        '''
        # music returns to normal
        # elated
        P "So now, I take everyone's ideas seriously, no matter how absurd! People might be wrong sometimes, but by and large they're smart and capable!"
        P "You never know where genius can strike! All it takes is a little trust, and people can do wondrous things!"
        P "Now we spend our days chasing the wildest fancies our eyes and our abaci can detect. Like now, witht the celestial object!"
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
                P "{cps=15}...yeah, that was a lot"

            "Your words fly like a finch! Hence, you are amazing!":
                P "I am, aren't I!? And so are you!!"

            "Thanks, doofus!":
                P "I {i}am{/i} a doofus! What a fun word to say! You sure are a clever one, Mrs. Sir. Bubbleton!"

            "I'm gonna be honest: I absorbed {i}none{/i} of what you just said.":
                P "Well isn't that wonderful!? Isn't it {i}amazing{/i} how there's always something else to learn!?"
        
        $ has_philo_philo = True

        P "Now we — where were we, again?"
        jump self_id

    label challenge_time:
        
        # concerned
        P '"Efficiency"? What about "efficiency"? Eveyone will get what needs to be done in their time!'
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
                P "Tell me — just who are you?"
                jump self_id

            "Science has to be replicable. You need to fail to succeed. That's {i}real{/i} autonomy":
                pass

            "You're not getting ANYTHING DONE! GROW A SPINE!":
                P "I don't have a spine! I'm a bubble witch!"
                P "It would be interesting to have one, though — great suggestion!"
                P "Tell me again — are you a bubble witch?"
                jump self_id

        P "That..."
        P "...is true actually. I suppose it wasn't very scientific of me to neglect critical thinking like that."
        P "But I know all too well the pitfalls of a real \"leader's\" leader. Tell me: how can I not be like that again?"

        menu second_challenge:

            "Get ahold of yourself. Make the big decisions. Others are too weak and stupid to.":
                P "I.."
                P "...you know that's not true."
                P "Tell me — who are you to say that!?"
                jump self_id

            "Train others to be leaders in their own right. Trust them to fail and {i}learn{/i}":
                pass

            "Exactly the way you are! You're perfect!":
                P "I am, aren't I!?"
                P "And so are you!! <3"
                P "Yes, you — wait, who are you?"
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

        V '''
        You're right. It was that debate that sparked all the good that people did: the arguing,
        the fierce determination, and yet the genuinely kind ones always manage to synthesize things
        and make things more that their parts. I understand. But I need to know: how can I trust myself
        enough to trust I won't do what I did to my people again?
        '''

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
        V '''
        You're right. I knew how to talk, and be jovial and accept people. And I learned how to trust
        people. But I forgot how to think, and that makes me a bad scientist and philosopher. I haven't
        really thought in a while. I got so caught up in all the different ways of doing things, I forgot
        to do those things. But those days are over. I'm going to take a stand, and stand with the people
        I haven't always stood with, whether because I was mean or I was neglectful. No more. We are going to
        find this object, and now {i}exactly{/i} what it is, {i}scientifically!{/i}! And you know what? If 
        I can help other worlds out, I'll open my arms to them, too!
        '''

        $ is_solved_philo = True


    return
