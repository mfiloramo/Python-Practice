#  This module can be used to generate various random values.

import random

conjunctions = ['A minute later', 'Accordingly', 'Actually', 'After',
                'After a short time', 'Afterwards', 'Also', 'And', 'Another',
                'As an example', 'As a consequence', 'As a result', 'As soon as',
                'At last', 'At length', 'Because', 'Because of this', 'Before',
                'Besides', 'Briefly', 'But', 'Consequently', 'Conversely', 'Equally important',
                'Finally', 'First', 'For example', 'For instance', 'For this purpose',
                'For this reason', 'Fourth', 'From here on', 'Further', 'Furthermore',
                'Gradually', 'Hence', 'However', 'In addition', 'In conclusion', 'In contrast',
                'In fact', 'In short', 'In spite of', 'In spite of this', 'In summary',
                'In the end', 'In the meanwhile', 'In the meantime', 'In the same manner',
                'In the same way', 'Just as important', 'Least', 'Last', 'Last of all',
                'Lastly', 'Later', 'Meanwhile', 'Moreover', 'Nevertheless', 'Next',
                'Nonetheless', 'Now', 'Nor', 'Of equal importance', 'On the contrary',
                'On the following day', 'On the other hand', 'Other hand', 'Or', 'Presently',
                'Second', 'Similarly', 'Since', 'So', 'Soon', 'Still', 'Subsequently',
                'Such as', 'The next week', 'Then', 'Thereafter', 'Therefore', 'Third',
                'Thus', 'To be specific', 'To begin with', 'To illustrate', 'To repeat',
                'To sum up', 'Too', 'Ultimately', 'What', 'Whatever', 'Whoever', 'Whereas',
                'Whomever', 'When', 'While', 'With this in mind', 'Yet', 'Coincidentally', 'And then',
                'But actually', 'Soon thereafter', 'After all that bullshit', 'Before you knew it'
                ]

nouns = ['Actor', 'Gold', 'Painting', 'Advertisement', 'Grass', 'Parrot', 'Afternoon', 'Greece', 'Pencil',
         'Airport', 'Guitar', 'Piano', 'Ambulance', 'Hair', 'Pillow', 'Animal', 'Hamburger', 'Pizza', 'Answer',
         'Helicopter', 'Planet', 'Apple', 'Helmet', 'Plastic', 'Army', 'Holiday', 'Portugal', 'Australia',
         'Honey', 'Potato', 'Balloon', 'Horse', 'Queen', 'Banana', 'Hospital', 'Quill', 'Battery', 'House',
         'Rain', 'Beach', 'Hydrogen', 'Rainbow', 'Beard', 'Ice', 'Raincoat', 'Bed', 'Insect', 'Refrigerator',
         'Belgium', 'Insurance', 'Restaurant', 'Boy', 'Iron', 'River', 'Branch', 'Island', 'Rocket', 'Breakfast',
         'Jackal', 'Room', 'Brother', 'Jelly', 'Rose', 'Camera', 'Jewellery', 'Russia', 'Candle', 'Jordan',
         'Sandwich', 'Car', 'Juice', 'School', 'Caravan', 'Kangaroo', 'Scooter', 'Carpet', 'King', 'Shampoo',
         'Cartoon', 'Kitchen', 'Shoe', 'China', 'Kite', 'Soccer', 'Church', 'Knife', 'Spoon', 'Crayon',
         'Lamp', 'Stone', 'Crowd', 'Lawyer', 'Sugar', 'Daughter', 'Leather', 'Sweden', 'Death', 'Library', 'Teacher',
         'Denmark', 'Lighter', 'Telephone', 'Diamond', 'Lion', 'Television', 'Dinner', 'Lizard', 'Tent', 'Disease',
         'Lock', 'Thailand', 'Doctor', 'London', 'Tomato', 'Dog', 'Lunch', 'Toothbrush', 'Dream', 'Machine', 'Traffic',
         'Dress', 'Magazine', 'Train', 'Easter', 'Magician', 'Truck', 'Egg', 'Manchester', 'Uganda', 'Eggplant',
         'Market', 'Umbrella', 'Egypt', 'Match', 'Van', 'Elephant', 'Microphone', 'Vase', 'Energy', 'Monkey',
         'Vegetable', 'Engine', 'Morning', 'Vulture', 'England', 'Motorcycle', 'Wall', 'Evening', 'Nail', 'Whale',
         'Eye', 'Napkin', 'Window', 'Family', 'Needle', 'Wire', 'Finland', 'Nest', 'Xylophone', 'Fish', 'Nigeria',
         'Yacht', 'Flag', 'Night', 'Yak', 'Flower', 'Notebook', 'Zebra', 'Football', 'Ocean', 'Zoo', 'Forest',
         'Oil', 'Garden', 'Fountain', 'Orange', 'Gas', 'France', 'Oxygen', 'Girl', 'Furniture', 'Oyster', 'Glass',
         'Garage', 'Ghost'
         ]

verbs = ['accept', 'add', 'admire', 'admit', 'advise', 'afford', 'agree', 'alert', 'allow', 'amuse', 'analyze',
         'announce', 'annoy', 'answer', 'apologise', 'appear', 'applaud', 'appreciate', 'approve', 'argue', 'arrange',
         'arrest', 'arrive', 'ask', 'attach', 'attack', 'attempt', 'attend', 'attract', 'avoid', 'back', 'bake',
         'balance', 'ban', 'bang', 'bare', 'bat', 'bathe', 'battle', 'beam', 'beg', 'behave', 'belong', 'bleach',
         'bless', 'blind', 'blink', 'blot', 'blush', 'boast', 'boil', 'bolt', 'bomb', 'book', 'bore', 'borrow',
         'bounce', 'bow', 'box', 'brake', 'branch', 'breathe', 'bruise', 'brush', 'bubble', 'bump', 'burn', 'bury',
         'buzz', 'calculate', 'call', 'camp', 'care', 'carry', 'carve', 'cause', 'challenge', 'change', 'charge',
         'chase', 'cheat', 'check', 'cheer', 'chew', 'choke', 'chop', 'claim', 'clap', 'clean', 'clear', 'clip',
         'close', 'coach', 'coil', 'collect', 'colour', 'comb', 'command', 'communicate', 'compare', 'compete',
         'complain', 'complete', 'concentrate', 'concern', 'confess', 'confuse', 'connect', 'consider', 'consist',
         'contain', 'continue', 'copy', 'correct', 'cough', 'count', 'cover', 'crack', 'crash', 'crawl', 'cross',
         'crush', 'cry', 'cure', 'curl', 'curve', 'cycle', 'dam', 'damage', 'dance', 'dare', 'decay', 'deceive',
         'decide', 'decorate', 'delay', 'delight', 'deliver', 'depend', 'describe', 'desert', 'deserve', 'destroy',
         'detect', 'develop', 'disagree', 'disappear', 'disapprove', 'disarm', 'discover', 'dislike', 'divide',
         'double', 'doubt', 'drag', 'drain', 'dream', 'dress', 'drip', 'drop', 'drown', 'drum', 'dry', 'dust',
         'earn', 'educate', 'embarrass', 'employ', 'empty', 'encourage', 'end', 'enjoy', 'enter', 'entertain',
         'escape', 'examine', 'excuse', 'exercise', 'exist', 'expand', 'expect', 'explode', 'extend', 'face',
         'fade', 'fail', 'fancy', 'fasten', 'fax', 'fear', 'fence', 'file', 'fill', 'film', 'fire', 'fit', 'fix',
         'flap', 'float', 'flood', 'flow', 'flower', 'fold', 'follow', 'fool', 'form', 'found', 'frame', 'frighten',
         'fry', 'gather', 'gaze', 'glow', 'glue', 'grate', 'grease', 'greet', 'grip', 'groan', 'guarantee', 'guess',
         'guide', 'hammer', 'hand', 'handle', 'hang', 'happen', 'harass', 'harm', 'hate', 'haunt', 'head', 'heal',
         'heap', 'heat', 'help', 'hook', 'hop', 'hope', 'hover', 'hug', 'hum', 'hunt', 'hurry'
         ]

adjectives = ['adorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive', 'amused', 'angry', 'annoyed',
              'annoying', 'anxious', 'arrogant', 'ashamed', 'attractive', 'average', 'awful', 'bad', 'beautiful',
              'better', 'bewildered', 'black', 'bloody', 'blue', 'blue-eyed', 'blushing', 'bored', 'brainy', 'brave',
              'breakable', 'bright', 'busy', 'calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean', 'clear',
              'clever', 'cloudy', 'clumsy', 'colorful', 'combative', 'comfortable', 'concerned', 'condemned',
              'confused', 'cooperative', 'courageous', 'crazy', 'creepy', 'crowded', 'cruel', 'curious', 'cute',
              'dangerous', 'dark', 'dead', 'defeated', 'defiant', 'delightful', 'depressed', 'determined', 'different',
              'difficult', 'disgusted', 'distinct', 'disturbed', 'dizzy', 'doubtful', 'drab', 'dull', 'eager', 'easy',
              'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'energetic', 'enthusiastic', 'envious',
              'evil', 'excited', 'expensive', 'exuberant', 'fair', 'faithful', 'famous', 'fancy', 'fantastic', 'fierce',
              'filthy', 'fine', 'foolish', 'fragile', 'frail', 'frantic', 'friendly', 'frightened', 'funny', 'gentle',
              'gifted', 'gleaming', 'glorious', 'good', 'gorgeous', 'graceful', 'grieving', 'grotesque', 'grumpy',
              'handsome', 'happy', 'healthy', 'helpful', 'helpless', 'hilarious', 'homeless', 'homely', 'horrible',
              'hungry', 'hurt', 'ill', 'important', 'impossible', 'inexpensive', 'innocent', 'inquisitive',
              'itchy', 'jealous', 'jittery', 'jolly', 'joyous', 'kind', 'lazy', 'light', 'lively', 'lonely',
              'long', 'lovely', 'lucky', 'magnificent', 'misty', 'modern', 'motionless', 'muddy', 'mushy',
              'mysterious', 'nasty', 'naughty', 'nervous', 'nice', 'nutty', 'obedient', 'obnoxious', 'odd',
              'old-fashioned', 'open', 'outrageous', 'outstanding', 'panicky', 'perfect', 'plain', 'pleasant',
              'poised', 'poor', 'powerful', 'precious', 'prickly', 'proud', 'putrid', 'puzzled', 'quaint', 'real',
              'relieved', 'repulsive', 'rich', 'scary', 'selfish', 'shiny', 'shy', 'silly', 'sleepy', 'smiling',
              'smoggy', 'sore', 'sparkling', 'splendid', 'spotless', 'stormy', 'strange', 'stupid', 'successful',
              'super', 'talented', 'tame', 'tasty', 'tender', 'tense', 'terrible', 'thankful', 'thoughtful',
              'thoughtless', 'tired', 'tough', 'troubled', 'ugliest', 'ugly', 'uninterested', 'unsightly', 'unusual',
              'upset', 'uptight', 'vast', 'victorious', 'vivacious', 'wandering', 'weary', 'wicked', 'wide-eyed',
              'wild', 'witty', 'worried', 'worrisome', 'wrong', 'zany', 'zealous'
              ]

names = ['Craven Moorhead', 'Lou Tenant', 'Alotta Fagina', 'Howie Feltersnatch', 'Pat McRotch', 'Anita Dick',
         'Juan Hung Lowe', 'Amanda Hugenkiss', 'Hugh Jass', 'Hugh Jorgan', 'Al K. Holic', 'B. Problem',
         'Adam Baum', 'Ben Dover', 'Ivana Tinkle', 'Ivana Humpalot', 'Mike Okhurtz', 'Mike Hunt', 'Mike Hock',
         'Mike Lit', 'Mike Rotch', 'Jena Talia', 'Sharron Peters', 'Juwanna Hooker', 'April Pealot', 'Peter Wiener',
         'Aitor Mitrousers', 'Ophelia Teats', 'Forrest Ranger', 'Hedda Hare', 'Lotta Hare', 'Dick Hertz', 'Lon Moore',
         'Dick Lotion', 'Ben Gay', 'Don Bashinda Miccar', 'Jaques Strapp', 'Rosie Kuntz', 'Oliver Klozov',
         'Seymoure Butts', 'Dick Butkiss', 'Holly Woods', 'Harry Balls', 'Harry Kuntz', 'Dick Trickle', 'Dick Sweat',
         'Pete Moss', 'Tara Dikov', 'Iver Dick', 'Jack Cass', 'Ilene Dover', 'N. Brain', 'Leigha Tard', 'Anita Bath',
         'Pat Myass', 'Ivana Sukalot', 'Ima Horr', 'Darren Dick', 'Richard Dick', 'Willie Makeet', 'Betty Kant',
         'I.P. Freely', 'Spanky', 'M.T. Mylode', 'Anita Potty', 'Belle E. Flopp', 'Allota Dick', 'Benjamin Over',
         'Amanda Reckonwith', 'Haywood Jabuzov', 'Natalie Drest', 'Vishnu VerHeer', 'Neil DuPrey', 'Phill McCafferty',
         'Ella Mentry', 'Paige Turner', 'Eileen Left', 'Robyn DeCradle', 'Patty O-Ferncher', 'Chris Anthemum',
         'Norma Lee Oppin', 'Marge Innovera', 'Sarah Bellum', 'Tyron Shulaces', 'Scott Free', 'Dick Skidmore',
         'Sandy Fagina', 'Richard Head', 'Wyn Green', 'Dick Wood', 'Dick Stillhard', 'Dick Link', 'Stewart Pidd',
         'Barbara D. Wire', 'Anita Peter', 'Harry Cox', 'Sharon Cox', 'Holden Cox', 'Dick Holder', 'Rick O-Shae',
         'Felia Balls', 'Barb B. Cue', 'Annie Body', 'Anita Roddick', 'Nick Carrs', 'Robin Banks', 'Fawn Dell Maibalz',
         'Barry Abone', 'Stacy Rhect', 'Manny Kanblo', 'Phil Apeno', 'Rose Bush', 'Phylis Up', 'Tommy Gun',
         'Jack Pot', 'Anita Bonia', 'Tad Pole', 'Penny Candy', 'Dennis Toffice', 'Hugh DeMann', 'Holly Dayin',
         'Utits Besaggy', 'Bea Sting', 'April Showers', 'Ivanna B. Badd', 'Kitty Litter', 'Alpha Kenny Juan',
         'Max E. Padd', 'Boyd Schidtt', 'Harry P. Ness', 'Stanley Steamer', 'May Flowers', 'Barry Schmelly',
         'Milo Minute', 'Noah Ho', 'Bill Board', 'Kris Mass', 'Cole Kutz', 'Madame Dick Hertz', 'Hedda Lettuce',
         'Anita Moorehead', 'Wayne Kerr', 'Willie B. Hardigan', 'Dwayne Pipe', 'Titsiana Boobarini', 'Dick Fitzwell',
         'Peter B. Hangin', 'Manny Feltersnatch', 'Sharron D. Zeazes', 'Penny Nichols', 'Adolf Oliver Busch',
         'Liz B. Anne', 'Patty O-Dors', 'Dick Spring', 'Heaven Lee', 'Phil McCraken', 'Harry Dickman', 'Dick Gazinya',
          'Haywood Yablome'
         ]

articles = ["a", "an", "the", "his", "her", "their", "its", "those", "them", "that", "this", "these"]

custom_sents = ["Can you believe that?", f"That's what {random.choice(names)} thought.", "Isn't that unbelievable?",
                f"At least, according to the {random.choice(nouns)}s.", "Or so we thought.", "But, actually...",
                "It's pretty stupid that this was a thing.", "Sure, it was so, but nobody ever thought it would be so.",
                f"Or else you'll probably {verbs}, or... pretty much {verbs}.",
                f"That's because it was pretty {adjectives}.", f"Which originally belonged to {names}.",
                "If you're willing to believe that, you're an idiot.", "Obviously, right?",
                "This, you would be idiotic to believe.", "And that's how your grandma's hair got on fire.",
                f"...And that's how your {random.choice(names)}'s {random.choice(nouns)} blew up."
                ]

be_tenses = ["is", "was", "will be", "won't be", "can be", "would be", "should be", "could be", "is not"]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
vowels = "AaEeIiOoUu"
consonants = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
numbers = "1234567890"
symbols = "!@#$%^&*()_+=-"
punctuation = [".", "!", "?", "...", "!?"]

r_cons = {random.choice(consonants).lower()}
r_vowel = {random.choice(vowels).lower()}
r_word = "".join(f"{r_cons}{r_vowel}{r_cons}{r_vowel}{r_cons}{r_vowel}{r_cons}{r_vowel}")  # Needs tweaking.
r_character = random.choice(str([letters, numbers, symbols]))
r_conj = random.choice(conjunctions)
r_noun = random.choice(nouns)
r_verb = random.choice(verbs)
r_adj = random.choice(adjectives)
r_name = random.choice(names)
r_sent = random.choice(custom_sents)
r_be = random.choice(be_tenses)
r_art = random.choice(articles)
