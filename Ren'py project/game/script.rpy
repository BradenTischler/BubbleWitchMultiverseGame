﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define G = Character("Witch of Gluttony", image='LegallyDistictPinkBlob.png', kind=bubble)
# define wm = Character("Wild Myst", image='whatever.png', kind=bubble)
<<<<<<< Updated upstream
=======
=======
define P = Character("Witch of the Mind", image='LegallyDistictPinkBlob.png', kind=bubble)
define V = Character("Witch of the Mind", image='LegallyDistictPinkBlob.png', kind=nvl)
>>>>>>> Stashed changes
>>>>>>> Stashed changes

image Glutton = "LegallyDistinctPinkBlob.png"

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

    # This ends the game.

    return

label scienceworld:

    # all science world scripting goes here

    return

label magicworld:

    show main at left #neutral
    with moveinleft
    "You step out of the portal into a strange place."
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
        "So, you're in charge around here?"
    

    return

label philosophyworld:

<<<<<<< Updated upstream
    # all philosophy world scripting goes here
=======
    $ expo_dump = False
    $ challenge_time = False

    scene bg room

    P "Hark! Who enters my lair!?"

    menu:
        "The valient bubble-witch of the fantastically sophisticated nether-realm!":
            "Oh, utterly resplendent! A fortuitious parlay, this will be!" :
        
        "[Actual cannonical hub world name]":
            "Ah — well met, Mrs. Sir. Bubbleton!":
        
        "That's none of your business!":
            "Oh, how unfortunate you conceal things from me! But if that is how you choose"
            "to approach, so be it!"

    P "And now, what is your purpose? What is your import?"

    $ loopy_phil_1 = False
    menu self_id:   
        "Sir, I'm not a delivery driver!":
            jump sticking_loop1
                $ loopy_phil_1 = True

        "I'm nobody.":
            "Well, that's no way to treat yourself! come! have a chat!"
            $ loopy_phil = False

        "I don't know. A book said I was important.":
            "Ah, is that so? Books are wonderful and give us so much good information, but your information is good, too! We can all learn so much from each other!"
            $ loopy_phil = False
    
    if loopy_phil_1 == True:
        "Well, what are you, then!?"
        jump self_id

    P "There are so many wonderful things, and we are all managing our figures and abaci intently to find the figure in the sky! And yet, people have so many"
    P "Good ideas of how to find it and what it is, sometimes I don't want the journey to end!"

    P "Now tell me, what is your purpose in seeing me? What brings such a lovely being from the outside to my own wonderful abode?"

    menu first_big_choice:

        "What's happening in this world? [costs 1 time]" if has_philo_philo == False: # This is how you get the philosophy idea
            $ expo_dump = True

        "Your bourgeois metaphysical thinking is unbecoming of you, comrade!": # This just insults them
            P '{cps = 5}That hurts, "comrade."' # concerned
            P "Now tell me, what was it that you wanted from me?" # concerned
            $ loopy_phil_1 = True
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

                "No, that's stupid.":

                "So how do you get anything {i}done{/i}?"

                "Wow! Amazing!":

            P "Yes, that's — wait, what was I saying?"
            jump self_id

        "Have you considered that science should be efficient?" if has_philo_philo == True: # This leads to solving the problem; requires having learned the lesson from the science witch
            $ challenge_time = True

        if expo_dump == True:
            # music gets sad and reflective
            V '''
            [elated]
            Well, one day I wasn't, and then I was. There's not much to tell there. Oh, but so much in between! Yes, that's the space I like.
            When I was born, the vivacious place full of life you see was barren, if you can believe it! It was a barren field of grass and dirt, if
            you could believe it, but it stretched out for miles, so many miles you could walk back to the place you started! and see nothing but a planet of grass! 
            One day, I hit my foot on something — something other than the brobdingnagian expanse, anyway — and I saw a little brick with little smaller bricks inside of it. 
            There was nothing there, of course, but my mind knew the word: book. I read the, {i}book{/i}, and it told me I was the "Witch of the Mind," whatever that meant. 
            It said I was in charge of this world and that it must be shaped and filled with people.

            {clear}

            [neutral]
            I didn't know what "people" meant before I wasn't the only one, of course. But for the time being, I started to make rules for this place: "an object in motion must
            stay in motion," "eukaryotic cells have nuclei," that sort of thing. Eventually, from these rules, other people were made. At first, I talked to them about the way people
            should treat each other. At first it was simple: "don't hurt people." But then others starting to say, "don't do things that cause harm." Our minds started to rail against each
            other, and eventually, philosophy was born from that dialectic. I was so invested, I started to forget the rules. Eventually, we figuered out how to work through them, though.
            That was science. Science was hard, but it was hardest for me, because I was remembering what I had forgotten. I began to mourn my lost memories.

            {clear}

            [concerned]
            I saw people making mistakes; doing the wrong things. They challenged me, and sometimes they were right, but I was impatient with them and, really, myself. I started to
            rule them with a rod of iron, enforcing on them a strict sense of justice and a need to adhere to the rule of their superior in the hierarchy that I put myself on top of.
            It worked, to some extent: people got things done. But they also grew fearful, so fearful they weren't really able to go any further with things. I began to realize that I
            was hurting them because I was hurt, not because they needed it. I realized that people need autonomy, so I gave them that.

            {clear}

            [neutral]
            They got better after they had a sense of self, and after we all realized that complicated things have nuance.
            [this is a hint for how to solve the western world's problems]
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
                    P "I {i]am{/i} a doofus! What a fun word to say! You sure are a clever one, Mrs. Sir. Bubbleton!"

                "I'm gonna be honest: I absorbed {i}none{/i} of what you just said.":
                    P "Well isn't that wonderful!? Isn't it {i}amazing{/i} how there's always something else to learn!?"
            
            expo_dump = False
            has_philo_philo = True

            P "Now we — where were we, again?"
                jump self_id

        if challenge_time == True:
            
            # concerned
            P '"Efficiency"? What about "efficiency"? Eveyone will get what needs to be done in their time!'
            P "There's really no need to rush things here. We'll all get through it in the end!"

            menu first_challenge:

                "You know what, you're right. Forget about it.":
                    P "Yeah, that's right! We'll get there!" # elated
                    P "We just need to consider {i]everyone's{/i} ideas, and {i}then{/i} we'll get this celesiatl object thing sorted out!"
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

            "Not all challenge is abuse. Philosophy needs rigorous debate.":

            V:
            '''
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

            V:
            '''
            You're right. I knew how to talk, and be jovial and accept people. And I learned how to trust
            people. But I forgot how to think, and that makes me a bad scientist and philosopher. I haven't
            really thought in a while. I got so caught up in all the different ways of doing things, I forgot
            to do those things. But those days are over. I'm going to take a stand, and stand with the people
            I haven't always stood with, whether because I was mean or I was neglectful. No more. We are going to
            find this object, and now {i}exactly{/i} what it is, {i}scientifically!{/i}! And you know what? If 
            I can help other worlds out, I'll open my arms to them, too!
            '''

            $ philo_solve = True

>>>>>>> Stashed changes

    return
