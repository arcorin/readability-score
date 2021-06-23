import re
import argparse
import math


text1 = "Readability is the ease with which a reader can understand a written text. \
In natural language, the readability of text depends on its content and its presentation. \
Researchers have used various factors to measure readability. \
Readability is more than simply legibility, \
which is a measure of how easily a reader can distinguish individual letters or characters from each other. \
Higher readability eases reading effort and speed for any reader, \
but it is especially important for those who do not have high reading comprehension. \
In readers with poor reading comprehension, \
raising the readability level of a text from mediocre to good can make the difference between success and failure"

text2 = "This is the page of the Simple English Wikipedia. \
A place where people work together to write encyclopedias in different languages. \
That includes children and adults who are learning English. \
There are 142,262 articles on the Simple English Wikipedia. \
All of the pages are free to use. \
They have all been published under both the Creative Commons License 3 and the GNU Free Documentation License. \
You can help here! You may change these pages and make new pages. \
Read the help pages and other good pages to learn how to write pages here. \
You may ask questions at Simple talk."

text3 = "Gothic architecture are building designs, as first pioneered in Western Europe in the Middle Ages. \
It began in France in the 12th century. \
The Gothic style grew out of Romanesque architecture. \
It lasted until the 16th century. \
By that time the Renaissance style of architecture had become popular. \
The important features of Gothic architecture are the pointed arch, the ribbed vault, \
the flying buttress, and stained glass windows which are explained below. \
Gothic architecture is best known as the style of many of the great cathedrals, abbeys and churches of Europe. \
It is also the architecture of many castles, palaces, town halls, universities, and also some houses. \
Many church buildings still remain from this period. \
Even the smallest Gothic churches are often very beautiful, \
while many of the larger churches and cathedrals are thought to be priceless works of art. \
Many are listed with the United Nations Educational, \
Scientific and Cultural Organization (UNESCO) as World Heritage Sites. \
In the 19th century, the Gothic style became popular again, particularly for building churches and universities. \
This style is called Gothic Revival architecture."

text4 = "This is the front page of the Simple English Wikipedia. \
Wikipedias are places where people work together to write encyclopedias in different languages. \
We use Simple English words and grammar here. \
The Simple English Wikipedia is for everyone! \
That includes children and adults who are learning English. \
There are 142,262 articles on the Simple English Wikipedia. \
All of the pages are free to use. \
They have all been published under both the Creative Commons License \
and the GNU Free Documentation License. \
You can help here! You may change these pages and make new pages. \
Read the help pages and other good pages to learn how to write pages here. \
If you need help, you may ask questions at Simple talk. \
Use Basic English vocabulary and shorter sentences. \
This allows people to understand normally complex terms or phrases."

text5 = "Frequency is how often an event repeats itself over a set amount of time. \
In physics, the frequency of a wave is the number of wave crests that pass a point in one second \
(a wave crest is the peak of the wave). Hertz is the unit of frequency. \
All electromagnetic waves travel at the speed of light in a vacuum \
but they travel at slower speeds when they travel through a medium that is not a vacuum. \
Other waves, such as sound waves, travel at much much lower speeds and can not travel through a vacuum. \
Examples of electromagnetic waves are: light waves, radio waves, infrared radiation, microwaves, and gamma waves."

# Project: Readability Score
# Stage 1/5: Simple estimation
# https://hyperskill.org/projects/155/stages/808/implement

"""
new_text = input()
print('EASY' if len(new_text) <= 100 else 'HARD')
"""

# Stage 2/5: Words and sentences
# https://hyperskill.org/projects/155/stages/809/implement

"""
text = input()
# create a list of the sentences in the input text
sentences_list = re.split(r'\. |\? |! ', text)

# create a list of the length of the sentences in the input text
sentences_length = [len(el.split()) for el in sentences_list]

# calculate the average length of the sentences
mean_length = sum(sentences_length) / len(sentences_length)
print('EASY' if mean_length <= 10 else 'HARD')
"""

# Stage 3/5: What's the score
# https://hyperskill.org/projects/155/stages/810/implement

"""
sentences_delimiters = r"\. |\? |! "
words_delimiters = r"\. *|\? *|! *|, *|'|\s"
years_list = []


class Text:
    '''Analyze the text and output the result'''
    def __init__(self, text):
        self.text = text
        # list of sentences
        self.sentences_list = self.sentences_calc()
        # list of sentences length
        self.sentences_len_list = [len(el) for el in self.sentences_list]
        # list of words
        self.words_list = self.text.split()
        # list of words length
        self.words_len_list = [len(el) for el in self.words_list]
        # number of characters
        self.chars_number = sum(self.words_len_list)
        # readability score
        self.score = self.score_calc()
        self.years = self.years_calc()
        self.output = self.output()

    def sentences_calc(self):
        return re.split(sentences_delimiters, self.text)

    def score_calc(self):
        chars = self.chars_number
        words = len(self.words_list)
        sentences = len(self.sentences_list)
        score = 4.71 * chars / words + 0.5 * words / sentences - 21.43
        return round(score, 2)

    def years_calc(self):
        years = ''
        score = math.ceil(self.score)
        if score in [1, 3]:
            years = f'{score + 4}-{score + 5}'
        elif score == 2 or score in range(4, 13):
            years = f'{score + 5}-{score + 6}'
        elif score == 13:
            years = '18-24'
        elif score >= 14:
            years = '25'
        return years

    def output(self):
        features = {'Words': len(self.words_list),
                    'Sentences': len(self.sentences_list),
                    'Characters': self.chars_number,
                    'The score is': self.score}
        print(f'The text is:\n{self.text}\n')
        for key, value in features.items():
            print(f'{key}: {value}')

        print(f'This text should be understood by {self.years}-year-olds.')


parser = argparse.ArgumentParser()
parser.add_argument('--infile')
args = parser.parse_args()

file = args.infile
"""
"""
# write the test text to the test file 
with open(file, 'w') as f:
    f.write(text3)
"""
"""
# open the argument file and read the text
with open(file, 'r') as f:
    read_text = f.read()

# create an object that analyze the text read from the file and output the result
new_text = Text(read_text)
"""

# Stage 4/5: More formulas!
# https://hyperskill.org/projects/155/stages/811/implement

# Stage 5/5: Frequency Inc
# https://hyperskill.org/projects/155/stages/812/implement

# ARI  https://en.wikipedia.org/wiki/Automated_readability_index
# FK  https://readabilityformulas.com/flesch-reading-ease-readability-formula.php
# SMOG  https://readabilityformulas.com/smog-readability-formula.php
# CL  https://readabilityformulas.com/coleman-liau-readability-formula.php
# PB  https://readabilityformulas.com/new-dale-chall-readability-formula.php
scores_types = {'ARI': 'Automated Readability Index',
                'FK': 'Flesch–Kincaid readability tests',
                'SMOG': 'Simple Measure of Gobbledygook',
                'CL': 'Coleman–Liau index',
                'PB': 'Probability-based score'}

text_elements = ['Words', 'Difficult words', 'Sentences', 'Characters', 'Syllables', 'Polysyllables']
vowels = 'aeiou'
sentences_delimiters = r"\. |\? |! |; "
punctuation_signs = r"\,|:|\)|\("
# frequent_words = 'carrot dude mind some wander a abandon ability able about above abroad absence absolute absolutely absorb abuse academic accept acceptable access accident accommodation accompany according account accurate accuse achieve achievement acid acknowledge acquire across act action active activist activity actor actual actually ad adapt add addition additional address adequate adjust administration administrative admire admission admit adopt adult advance advanced advantage advert advertise advertisement advertising advice advise adviser affair affect afford afraid after afternoon afterwards again against age aged agency agent aggressive ago agree agreement agriculture ahead aid aim air aircraft airline airport alarm album alcohol alive all allow allowance almost alone along alongside already also alter alternative although altogether always amazing ambition ambulance among amount an analyse analysis analyst ancient and anger angle angry animal announce announcement annoy annual another answer anticipate anxiety anxious any anybody anyhow anyone anything anyway anywhere apart apartment apologize apology apparent apparently appeal appear appearance apple application apply appoint appointment appreciate approach appropriate approval approve approximate architect architecture area argue argument arise arm armed army around arrange arrangement arrest arrival arrive art article artificial artist as ashamed aside ask asleep aspect assess assessment assignment assist assistance assistant associate association assume assumption assure at atmosphere attach attack attempt attend attention attitude attorney attract attraction attractive audience aunt author authority automatic automatically autumn available average avoid awake award aware awareness away awful awkward baby back background backwards bacon bad badly bag bake balance ball ban band bang bank bar barrier base baseball basic basically basis basket bat bath bathroom battery battle be beach bean bear beard beat beautiful beauty because become bed bedroom beef beer before beforehand begin beginning behalf behave behaviour behind being belief believe bell belong below belt bench bend beneath benefit beside best bet better between beyond bicycle bid big bike bill bin bird birth birthday biscuit bit bite bitter black blade blame blank bless blind block bloke blonde blood blow blue board boat body boil boiler boiling bomb bone bonus book boom boot border bored boring born borrow boss both bother bottle bottom bounce bound bowl box boy boyfriend brain branch brave bread break breakfast breast breath breathe brick bridge brief briefly bright brilliant bring broad brother brown brush buck bucket buddy budget bug build builder building bump bunch burn burst bury bus business busy but butcher butter button buy buyer by bye cabinet cable cake calculate calculation calculator calendar call calm camera camp campaign can cancel cancer candidate candle candy cap capable capacity capital captain capture car card care career careful carefully carpet carry cartoon case cash cast castle cat catalogue catch category cause cease ceiling celebrate celebration cell cellphone cent centimetre central centre century cereal certain certainly certificate chain chair chairman challenge champion championship chance change channel chap chapter character characteristic characterize charge charity chart chase chat cheap cheat check cheek cheese chemical chemist chemistry cheque cherry chest chicken chief child childhood chip chocolate choice choose chop chuck church cigarette cinema circle circuit circumstance citizen city civil claim class classic classical classroom clean cleaner clear clearly clerk clever click client climate climb clock close closed closely closet cloth clothes cloud club clue coach coal coast coat code coffee coin cold collapse collar colleague collect collection college colour column combination combine come comfort comfortable command comment commercial commission commit commitment committee common communicate communication community company compare comparison compete competition competitive complain complaint complete completely complex complicated component comprehensive comprise computer concentrate concentration concept concern concerned concerning concert conclude conclusion condition conduct conference confidence confident confine confirm conflict confused confusing confusion congratulation connect connection conscious consciousness consent consequence consider considerable considerably consideration consist consistent constant constantly constitute construct construction consult consumer consumption contact contain contemporary content contest context continue continuous contract contrast contribute contribution control convenient convention conventional conversation convert conviction convince cook cooker cookie cool cooperation cope copy core corn corner correct corridor cost cottage cotton could council count counter country countryside county couple courage course court cousin cover cow crack craft crash crazy create creation creative creature credit crew crime criminal crisis criterion critic critical criticism criticize crop cross crowd crown crucial cruel cry cultural culture cup cupboard curious currency current currently curtain curve cushion custom customer cut cute cycle dad daddy daft daily damage dance danger dangerous dare dark darkness darling data database date daughter day dead deaf deal dealer dear death debate debt decade decent decide decision declare decline deep deeply defeat defence defend define definite definitely definition degree delay deliberately deliver delivery demand democracy democratic demonstrate demonstration dentist deny department departure depend dependent deposit depression depth derive describe description desert deserve design designer desire desk desperate despite destroy destruction detail detailed detect determination determine determined develop development device devil diagram diamond diary die diet differ difference different difficult difficulty dig dimension dinner direct direction directly director directory dirt dirty disabled disagree disappear disappoint disappointed disaster disc discipline discount discover discovery discuss discussion disease disgusting dish disk dismiss display dispute distance distant distinct distinction distinguish distribute distribution district disturb divide division divorce do doctor document dog dollar domestic dominant dominate door dot double doubt down downstairs downtown dozen draft drag drama dramatic draw drawer drawing dream dress drink drive driver drop drug drunk dry duck due dull dumb dump during dust duty each ear early earn earth ease easily east eastern easy eat economic economics economy edge edition editor education educational effect effective effectively efficiency efficient effort egg either elderly elect election electric electrical electricity electronic element elevator else elsewhere email embarrassed emerge emergency emotion emotional emphasis emphasize empire employ employee employer employment empty enable encounter encourage encouraging end enemy energy engage engine engineer engineering enhance enjoy enjoyable enormous enough enquiry ensure enter enterprise entertainment enthusiasm enthusiastic entire entirely entitle entrance entry envelope environment environmental equal equally equipment equivalent era error escape especially essay essential essentially establish establishment estate estimate ethnic even evening event eventually ever every everybody everyone everything everywhere evidence evil exact exactly exam examination examine example excellent except exception exchange excitement exciting exclude excuse executive exercise exhibition exist existence existing exit expand expansion expect expectation expenditure expense expensive experience experienced experiment experimental expert explain explanation explore explosion export expose express expression extend extension extensive extent external extra extraordinary extreme extremely eye face facility fact factor factory fail failure fair fairly faith fall false familiar family famous fan fancy fantastic far farm farmer fascinating fashion fast fat father fault favour favourite fear feature federal fee feed feedback feel feeling fellow female fence festival fetch few field fight figure file fill film filthy final finally finance financial find finding fine finger finish fire firm first firstly fish fishing fit fix fixed flash flat flavour flesh flight flood floor flow flower fly focus fold folk follow following food foot football for force foreign forest forever forget forgive fork form formal formally formation former formula forth fortnight fortunate fortune forward foundation frame frankly free freedom freeway freeze freezer frequent frequently fresh fridge friend friendly friendship frightened from front fruit fry fuel fulfil full fully fun function fund fundamental funeral funny furniture further fuss future gain gallery game gang gap garage garbage garden garlic gas gasoline gate gather gay gear gene general generally generate generation generous gentle gentleman gently genuine get giant gift girl girlfriend give glad glance glass global glove go goal god gold golden golf good goodbye goodness goods gorgeous gosh govern government governor grab grade gradually gram grammar grand grandad grandfather grandma grandmother grandpa granny grant graph grass grateful great greatly green grey grocery gross ground group grow growth guarantee guard guess guest guidance guide guilty guitar gun guy habit hair half halfway hall hand handbag handle handy hang happen happy hard hardly harm hat hate have he head headquarters health healthy hear hearing heart heat heater heating heaven heavily heavy height hell hello help helpful hence her here hero hers herself hesitate hi hide high highlight highly highway hill him himself hire his historian historical history hit hold holder holding hole holiday holy home homework honest honestly honey honour hook hope hopefully hopeless horrible horror horse hospital host hot hotel hour house household housing how however huge human hungry hunt hurry hurt husband ice idea ideal ideally identify identity idiot if ignore ill illegal illness illustrate image imagination imagine immediate immediately impact implement implication imply import importance important impose impossible impress impression impressive improve improvement in inch incident include including income incorporate increase increasingly incredible incredibly indeed independence independent index indicate indication individual industrial industry inevitable inevitably infant infection inflation influence inform informal information initial initially initiative injure injury inner innocent innovation input inquiry insect inside insist inspection inspector install instance instant instead institute institution instruction instrument insurance intellectual intelligence intelligent intend intense intention interaction interest interested interesting interjection internal international internet interpret interpretation interval intervention interview into introduce introduction invest investigate investigation investment invite involve involved involvement iron island issue it item its itself jacket jam job join joint joke journalist journey joy judge judgment juice jump jumper junior jury just justice justify keen keep kettle key keyboard kick kid kill kilometre kind king kiss kit kitchen knee knife knock know knowledge known lab label laboratory labour lack lad ladder lady lake lamb lamp land landlord landscape lane language large largely last late later latter laugh launch law lawyer lay layer lazy lead leader leadership leading leaf league lean learn least leather leave lecture left leg legal legislation leisure lend length less lesson let letter level liberal library licence lick lid lie life lift light lighting like likely limit limitation limited line link lip liquid list listen literally literary literature little live lively living load loan local locate location lock log logical lonely long long-term look loose lord lorry lose loss lost lot loud lounge love lovely lover low lower luck luckily lucky lump lunch lunchtime machine machinery mad madam magazine magic mail main mainly maintain maintenance major majority make male mall man manage management manager manner manufacturer manufacturing many map march margin mark market marketing marriage married marry marvellous mass massive master match mate material math maths matter maximum may maybe me meal mean meaning means meanwhile measure measurement meat mechanism media medical medicine medieval medium meet meeting member membership memory mental mention menu mere merely mess message messy metal method metre middle midnight might mile military milk millimetre mind mine mineral minimum minister ministry minor minority minute mirror misery miss mission mistake mix mixed mixture mobile mode model modern mom moment mommy money monitor month mood moon moral more moreover morning mortgage most mostly mother motion motor motorway mountain mouse mouth move movement movie much mud mum mummy murder muscle museum mushroom music musical must my myself mystery nail naked name narrow nasty nation national native natural naturally nature naughty near nearby nearly neat necessarily necessary neck need negative negotiate negotiation neighbour neighbourhood neither nerve nervous net network never nevertheless new newly news newspaper next nice nicely night nil no nobody nod noise noisy none nonsense nope nor normal normally north northern nose not notably note nothing notice notion novel now nowadays nowhere nuclear nuisance number numerous nurse nut object objection objective obligation observation observe obtain obvious obviously occasion occasional occasionally occupation occupy occur ocean odd odds of off offence offer office officer official often oil old on once one onion only onto open opening operate operation operator opinion opponent opportunity oppose opposite opposition option or orange order ordinary organ organic organization organize organized origin original originally other otherwise ought ounce our ours ourselves out outcome output outside outstanding oven over overall overcome overseas overtime owe own owner ownership o’clock pace pack package packet pad page pain paint painting pair palace pale pan panel panic pants paper parcel pardon parent park parking parliament part participate particular particularly partly partner partnership party pass passage passenger passion past path patience patient pattern pause pay payment peace peaceful peak pen penalty pencil penny pension people pepper per perceive percent percentage perception perfect perfectly perform performance perhaps period permanent permission permit person personal personality personally personnel perspective persuade petrol phase philosophy phone photo photocopy photograph phrase physical physically physics piano pick picture pie piece pig pile pill pilot pin pink pint pipe pitch pity pizza place plain plan plane planet plant plastic plate platform play player pleasant please pleased pleasure plenty plot plug plus pocket poem poet poetry point pole police policeman policy polite political politician politics poll pollution pond pool poor pop popular population port pose position positive possess possession possibility possible possibly post poster pot potato potential pound pour poverty power powerful practical practically practice practise praise pray prayer precise precisely predict prefer preference pregnant premise preparation prepare prepared presence present presentation preserve president press pressure presumably presume pretend pretty prevent previous previously price pride priest primarily primary prince princess principal principle print printer prior priority prison prisoner private privilege prize probably problem procedure proceed proceeding process produce producer product production profession professional professor profile profit program programme progress project promise promote promotion prompt proof proper properly property proportion proposal propose proposed prosecution prospect protect protection protest proud prove provide provided providing provision psychological psychology pub public publication publicity publish publisher pudding pull punch punishment pupil purchase pure purely purple purpose purse pursue push put qualification qualify quality quantity quarter queen question queue quick quickly quid quiet quietly quit quite quote race racing radical radio rail railway rain raise range rank rapid rapidly rare rarely rate rather ratio raw reach react reaction read reader readily reading ready real realistic reality realize really reason reasonable reasonably recall receipt receive recent recently reception recipe reckon recognition recognize recommend recommendation record recording recover recovery red reduce reduction refer reference reflect reflection reform refrigerator refuse regard regime region regional register registration regret regular regularly regulation reinforce reject relate related relation relationship relative relatively relax release relevant relief relieve religion religious rely remain remaining remains remark remarkable remember remind remote remove rent repair repeat replace replacement reply report reporter represent representation representative republic reputation request require requirement rescue research reserve resident residential resign resignation resist resistance resolution resolve resort resource respect respectively respond response responsibility responsible rest restaurant restore restrict restriction result retain retire retirement return reveal revenue reverse review revolution reward rhythm rice rich rid ride ridiculous right ring rip rise risk rival river road rob rock role roll roof room root rope rough roughly round route routine row royal rub rubber rubbish rude ruin rule run rural rush sack sad safe safety sail sake salad salary sale salt same sample sand sandwich satellite satisfaction satisfied satisfy sauce sausage save saving say scale scared scene schedule scheme school science scientific scientist scope score scratch scream screen screw script sea seal search season seat second secondary secondly secret secretary section sector secure security see seed seek seem seize select selection self sell send senior sense sensible sensitive sentence separate sequence series serious seriously servant serve service session set setting settle settlement several severe sew sex sexual shadow shake shall shame shape share sharp sharply shave she shed sheep sheet shelf shell shelter shift shine ship shirt shock shocked shocking shoe shoot shop shopping short shortly shot should shoulder shout shove show shower shrug shut sick side sight sign signal signature significance significant significantly silence silent silly silver similar similarly simple simply sin since sing singer single sink sir sister sit site situation size skill skin skirt sky sleep slice slide slight slightly slim slip slope slow slowly small smart smell smile smoke smoking smooth snap snow so so-called soap social society sock soft software soil soldier sole solicitor solid solution solve some somebody somehow someone something sometimes somewhat somewhere son song soon sore sorry sort soul sound soup source south southern space spare speak speaker special specialist species specific specifically specify speech speed spell spelling spend spill spin spirit spiritual spite split spoil spokesman spoon sport spot spray spread spring squad square squeeze stable staff stage stair stake stall stamp stand standard star stare start starve state statement station statistic status stay steady steak steal steam steel steep step stick stiff still stir stock stomach stone stop storage store storm story straight straightforward strain strange stranger strategic strategy straw strawberry stream street strength strengthen stress stretch strict strike string strip stroke strong strongly structure struggle student studio study stuff stupid style subject submit subsequent subsequently substance substantial succeed success successful successfully such suck sudden suddenly suffer sufficient sugar suggest suggestion suit suitable sum summer sun super supermarket supper supply support supporter suppose sure surely surface surgery surprise surprised surprising surprisingly surround survey survival survive suspect suspicion suspicious sustain swap swear sweep sweet swim swimming swing switch symbol sympathy system table tablet tackle tail take tale talent talk tall tank tap tape target task taste tax taxi tea teach teacher teaching team tear technical technique technology telephone television tell telly temperature temporary tend tendency tennis tension tent term terrible terribly territory terror terrorist test text than thank thanks that the theatre their theirs them theme themselves then theoretical theory there therefore they thick thin thing think this though thought threat threaten three throat through throughout throw thus ticket tidy tie tight tile till time tin tiny tip tired title to toast today toe together toilet tomato tomorrow ton tone tongue tonight too tool tooth top topic total totally touch tough tour tourist towards towel tower town toy track trade tradition traditional traffic trailer train trainer training transaction transfer transform transition translate transport transportation trash travel tray treat treatment treaty tree tremendous trend trial trick tricky trip troop trouble trousers truck true truly trust truth try tube tune tunnel turn twice twist type typical tyre ugly ultimate ultimately unable unbelievable uncle under underneath understand understanding undertake unemployed unemployment unfair unfortunate unfortunately unhappy uniform union unique unit united unity universal universe university unknown unless unlike unlikely until unusual up upon upper upset upstairs urban urge urgent us use used useful user usual usually vacation vague valley valuable value van variation variety various vary vast vegetable vehicle version very vet via victim victory video view village violence violent virtually virtue virus visible vision visit visitor visual vital voice volume voluntary vote vulnerable wage wait wake walk wall want war ward wardrobe warm warn warning wash washing waste watch water wave way we weak weakness wealth weapon wear weather web website wedding week weekend weekly weigh weight weird welcome welfare well west western wet what whatever whatsoever wheel when whenever where whereas wherever whether which while whisky whisper white who whoever whole whom whose why wicked wide widely widespread wife wild will willing win wind window windy wine wing winner winter wipe wire wise wish with withdraw within without witness woman wonder wonderful wood wooden wool word work worker working workshop world worried worry worrying worse worth would wound wrap write writer writing wrong yard yeah year yellow yep yes yesterday yet you young youngster your yours yourself youth zone'
# frequent_words.sort()


class Text:
    def __init__(self, text):
        self.text = text

        self.elements = {el: {} for el in text_elements}

        # list of sentences
        self.elements['Sentences']['list'] = self.sentences_calc()
        # list of sentences length (number of words in each sentence)
        self.elements['Sentences']['len_list'] = [len(el) for el in self.elements['Sentences']['list']]
        # number of sentences
        self.elements['Sentences']['number'] = len(self.elements['Sentences']['list'])

        # list of words
        self.elements['Words']['list'] = self.text.split()
        # list of words length
        self.elements['Words']['len_list'] = [len(el) for el in self.elements['Words']['list']]
        # number of words
        self.elements['Words']['number'] = len(self.elements['Words']['list'])

        # number of characters
        self.elements['Characters']['number'] = sum(self.elements['Words']['len_list'])

        # calculate the number of syllables and polysyllables
        self.syllables_polysyllables_calc()

        # score types
        self.scores = {k: {'name': v, 'value': 0, 'age': ''} for k, v in scores_types.items()}
        # calculate scores
        self.scores_calc()
        # calculate readabilty age for each score and average readability age
        self.readability_age_avg = self.readability_age_calc()

        # output solution
        self.output()

    def sentences_calc(self):
        """ create a list of sentences """
        return re.split(sentences_delimiters, self.text)

    def syllables_polysyllables_calc(self):
        """ Calculate the number of syllables for each word
        and the number of polysyllables.
            To count the number of syllables, use the letters a, e, i, o, u, y as vowels.
            Use 4 simple rules to count the syllables:
            1. Count the number of vowels in the word.
            2. Omit the so-called double vowels (for example, "rain" has 2 vowels but only 1 syllable).
            3. Subtract the silent vowels (for example, "e" in "side" is silent, the word has only 1 syllable).
            4. If it turns out that the word contains 0 vowels, then consider this word a monosyllable.
        """

        syllabs = self.elements['Syllables']
        polysyllabs = self.elements['Polysyllables']

        # list of number of syllables for each word
        syllabs['number_list'] = []
        # list of tuples for each word - (word, number of syllables)
        syllabs['word_number_list'] = []

        # lists of words for 1 to 6 number of syllables
        list1, list2, list3, list4, list5, list6 = ([] for _ in range(6))

        # create a new list for the words in lower case, without punctuation marks, without digit and abbreviation ...
        # ... in the 'elements[Words]' attribute of Text class
        self.elements['Words']['words_to_lower'] = []

        # counter of the words that will not be included in the list of number of syllables
        # ... numbers and abbreviation
        self.elements['Words']['abbreviations'] = []
        self.elements['Words']['numbers'] = []
        abbreviations = self.elements['Words']['abbreviations']
        numbers = self.elements['Words']['numbers']

        extracted_words = len(abbreviations) + len(numbers)

        # add the words without digits and not abbreviated to the 'words_to_lower' list
        # count the number of syllables for each word
        for w in self.elements['Words']['list']:

            # strip the punctuation marks
            if w[0] in sentences_delimiters or w[0] in punctuation_signs:
                w = w[1:]
            if w[-1] in sentences_delimiters:
                w = w[:-1]
            if w[-1] in punctuation_signs:
                w = w[:-1]

            # extract  the numbers and the abbreviation from the list of words
            if re.match('\d', w):
                abbreviations.append(w)
            elif w.isupper() and len(w) > 1:
                numbers.append(w)
            else:
                # add the word in lowercase to the list 'words_to_lower' in the 'elements' attribute of the Text class
                self.elements['Words']['words_to_lower'].append(w.lower())

                n = len(w)  # the lengths of the word
                s = 0  # the number of syllables
                w = w.lower()

                # ---------------------
                # calculate the number of syllables
                # count the number of single vowels and group of vowels in each word
                for _ in range(n - 1):
                    if w[_] in vowels and w[_ + 1] not in vowels:
                        s += 1

                # rules for the final vowel
                if w[-1] in 'aiou':
                    s += 1
                # rules for 'includes'
                if w.endswith('udes'):
                    s -= 1
                # rules for 'used'
                if w.endswith('ed') and n > 2 and w[-3] not in vowels:
                    s -= 1
                # rules for 'people'
                if w.endswith('le') and n > 2 and w[-3] not in vowels:
                    s += 1
                # rules for 'wikipedia' and 'encyclopedia'
                if w.endswith('ia') or w.endswith('ias'):
                    s += 1
                # rules for 'individual'
                if w.endswith('ual'):
                    s += 1
                # rules for 'employee'
                if w.endswith('ee'):
                    s += 1
                # rules for final 'y'
                if w[-1] == 'y' and w[-2] not in vowels:
                    s += 1
                # rules for 'creative' and 'mediocre'
                if re.match('.*cre', w):
                    s += 1
                if re.match(r'(.*io)', w) and not w.endswith('ion'):
                    s += 1
                if re.match(r'(.*ia)', w) and not w.endswith('ian'):
                    s += 1
                if re.match(r'(.*eo)', w):
                    s += 1

                if s == 0:
                    s += 1
                # --------------------------

                # add the word and the number of syllables to each list
                syllabs['number_list'].append(s)
                syllabs['word_number_list'].append((w, s))
                if s == 1:
                    list1.append((w, s))
                elif s == 2:
                    list2.append((w, s))
                elif s == 3:
                    list3.append((w, s))
                elif s == 4:
                    list4.append((w, s))
                elif s == 5:
                    list5.append((w, s))
                elif s == 6:
                    list6.append((w, s))

        # sort and print the lists of words for each number of syllables
        syllables_list = [list1, list2, list3, list4, list5, list6]
        for l in syllables_list:
            l.sort()
        '''
        print(f'{extracted_words} words are extracted:')
        [print(d, end=', ') for d in numbers]
        [print(a, end=', ') for a in abbreviations]
        print()
        [print(f'{syllables_list.index(l) + 1} syllables - {len(l)} words: {l}') for l in syllables_list]
        print()
        '''

        # assign to the attribute 'elements' of the Text class the total numbers of syllables and polysyllables
        syllabs['number'] = sum(syllabs['number_list'])
        polysyllabs['number'] = syllabs['number_list'].count(3) + \
                                syllabs['number_list'].count(4) + \
                                syllabs['number_list'].count(5) + \
                                syllabs['number_list'].count(6)

    def scores_calc(self):
        """ Calculate values for each type of score """

        # create shorter variables for each element of the text
        chars = self.elements['Characters']['number']
        words = self.elements['Words']['number']
        sentences = self.elements['Sentences']['number']
        syllables = self.elements['Syllables']['number']
        polysyllables = self.elements['Polysyllables']['number']

        # calculate the number of difficult words
        frequent_words_list = frequent_words.split()
        difficult_words_list = [w for w in self.elements['Words']['words_to_lower'] if w not in frequent_words_list]
        difficult_words_number = len(difficult_words_list) \
                + len(self.elements['Words']['abbreviations']) \
                + len(self.elements['Words']['numbers'])
        self.elements['Difficult words']['number'] = difficult_words_number
        difficult_words_percentage = difficult_words_number / words * 100
        coef = 0 if difficult_words_percentage < 5 else 1

        print(difficult_words_list)

        # the average number of characters per 100 words
        avg_characters = chars / words * 100
        # the average number of sentences per 100 words
        avg_sentences = sentences / words * 100

        # calculate each score
        self.scores['ARI']['value'] = 4.71 * chars / words + 0.5 * words / sentences - 21.43
        self.scores['FK']['value'] = 0.39 * words / sentences + 11.8 * syllables / words - 15.59
        self.scores['SMOG']['value'] = 1.043 * ((polysyllables * 30 / sentences) ** 0.5) + 3.1291
        self.scores['CL']['value'] = 0.0588 * avg_characters - 0.296 * avg_sentences - 15.8
        self.scores['PB']['value'] = 0.1579 * difficult_words_percentage + 0.0496 * words / sentences + coef * 3.6365

        # round each score with 2 decimals
        for k in scores_types.keys():
            self.scores[k]['value'] = round(self.scores[k]['value'], 2)

    def readability_age_calc(self):
        """  Calculate the readability age for each type of score
             and return the average readability age.
        """

        for k, v in self.scores.items():
            age = ''

            # readability age for the PB score
            if k == 'PB':
                score = round(self.scores[k]['value'], 1)
                if score <= 4.9:
                    age = '10'
                elif 5.0 <= score <= 5.9:
                    age = '12'
                elif 6.0 <= score <= 6.9:
                    age = '14'
                elif 7.0 <= score <= 7.9:
                    age = '16'
                elif 8.0 <= score <= 8.9:
                    age = '18'
                elif 9.0 <= score <= 9.9:
                    age = '24'

            # readability age for the first 4 scores
            else:
                # round each score to an integer
                score = round(self.scores[k]['value'], 0)
                # use the table from the link to determine the readability age for each score (the upper bound)
                # https://en.wikipedia.org/wiki/Automated_readability_index
                if score in [1, 2]:
                    age = f'{score + 5}'
                elif score in range(3, 13):
                    age = f'{score + 6}'
                elif score == 13:
                    age = '24'
                elif score >= 14:
                    age = '25'

            self.scores[k]['age'] = age

        # print(f'scores values are {scores_values}')
        ages = [float(v['age']) for v in self.scores.values()]

        # calculate the average readability age
        return sum(ages) / 5

    def output(self):
        """ Output the solution """

        print(f'The text is:\n{self.text}\n')

        # output the number of elements in text: words, sentences, characters, syllables, polysyllables
        for key, value in self.elements.items():
            print(f"{key}: {value['number']}")

        # user input of the scores to be displayed
        score = input("Enter the score you want to calculate (ARI, FK, SMOG, CL, all): ")
        print()

        # create a list with the scores to be displayed
        if score in self.scores.keys():
            scores_list = [score]  # if one score is chosen
        else:
            scores_list = self.scores.keys()  # if all scores are chosen

        # output the scores chosen by the user
        for s in scores_list:
            print(f"{self.scores[s]['name']}: {self.scores[s]['value']} (about {self.scores[s]['age']}-year-olds).")

        # output the average readability age
        print(f'\nThis text should be understood in average by {self.readability_age_avg}-year-olds.')


# '''
# add arguments that will be introduced to the console
parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--words')
args = parser.parse_args()

file = args.infile
w_file = args.words
# '''

'''
file = 'file.txt'
with open(file, 'w') as f:
    f.write(text1)
'''

# '''
# read the file introduced from the command line
with open(file, 'r') as f:
    read_text = f.read()

# '''
with open(w_file, 'r') as f_w:
    frequent_words = f_w.read()
# '''

# create a Text object that will calculate and display all the required elements
new_text = Text(read_text)
# '''

# Terminal command: "readability.py --infile my_file.txt"
# new_text = Text('hello!')

'''
[print(f'{k}: {v}') for k, v in new_text.elements.items()]

print()
[print(new_text.elements['Syllables']['number_list'].count(_)) for _ in range(1,6)]
'''

# print('\nfrequent_words:')
# print(frequent_words)
