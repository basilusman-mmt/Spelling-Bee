import random

import time

import os
import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 130)
engine.setProperty('volume', 1.0)


def clearterminal():

    os.system('cls' if os.name == 'nt' else 'clear')


tier1 = ['apple', 'book', 'cat', 'dog', 'sun', 'moon', 'star', 'tree', 'house', 'water', 'food', 'milk', 'bread', 'chair', 'table', 'phone', 'light', 'dark', 'happy', 'smile', 'laugh', 'friend', 'family', 'mother', 'father', 'sister', 'brother', 'child', 'baby', 'school', 'class', 'teacher', 'student', 'paper', 'pencil', 'pen', 'bag', 'door', 'window', 'floor', 'room', 'bed', 'pillow', 'blanket', 'shirt', 'shoes', 'pants', 'dress', 'hat', 'coat', 'hand', 'foot', 'head', 'face', 'hair', 'eye', 'nose', 'ear', 'mouth', 'tooth', 'heart', 'arm', 'leg', 'back', 'skin', 'page', 'word', 'name', 'time', 'day', 'night', 'week', 'month', 'year', 'today', 'tomorrow', 'yesterday', 'morning', 'evening', 'hello', 'goodbye', 'please', 'thanks', 'sorry', 'yes', 'no', 'maybe', 'okay', 'great', 'nice', 'good', 'bad', 'best', 'small', 'large', 'big', 'tiny', 'long', 'short', 'tall', 'wide', 'thin', 'fast', 'slow', 'quick', 'early', 'late', 'new', 'old', 'young', 'warm', 'cold', 'hot', 'cool', 'soft', 'hard', 'clean', 'dirty', 'easy', 'simple', 'bright', 'quiet', 'loud', 'sweet', 'sour', 'fresh', 'green', 'blue', 'red', 'black', 'white', 'brown', 'pink', 'purple', 'orange', 'yellow', 'gray', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine', 'ten', 'first', 'last', 'next', 'more', 'less', 'many', 'few', 'some', 'each', 'every', 'all', 'none', 'here', 'there', 'where', 'when', 'what', 'which', 'who', 'why', 'how', 'this', 'that', 'these', 'those', 'with', 'from', 'into', 'over', 'under', 'after', 'before', 'again', 'always', 'never', 'often', 'sometimes', 'inside', 'outside', 'around', 'above', 'below', 'world', 'place', 'thing', 'people', 'river', 'ocean', 'beach', 'grass', 'flower', 'fruit', 'ash', 'ant', 'arc', 'axe', 'bay', 'bee', 'bow', 'bug', 'bus', 'cap', 'cob', 'cod', 'dew', 'dig', 'dim', 'dip', 'dot', 'dry', 'eel', 'elm', 'fan', 'fig', 'fin', 'fix', 'fog', 'gap', 'gem', 'gum', 'gym', 'hem', 'hip', 'hop', 'hut', 'jam', 'jar', 'jet', 'jog', 'joy', 'jug', 'key', 'kid', 'kit', 'lap', 'lid', 'lip', 'log', 'lot', 'mad', 'map', 'mat', 'mud', 'nap', 'net', 'nib', 'oak', 'oat', 'pad', 'pan', 'paw', 'peg', 'pet', 'pie', 'pig', 'pin', 'pit', 'pot', 'pub', 'rag', 'ram', 'rap', 'rib', 'rim', 'rip', 'rod', 'rot', 'rub', 'rug', 'sap', 'sea', 'sew', 'sip', 'ski', 'sob', 'tap', 'tar', 'tea', 'toe', 'ton', 'top', 'tug', 'van', 'vat', 'vet', 'vow', 'wax', 'web', 'wig', 'win', 'wit', 'yam', 'zap', 'zip']


tier2 = ['animal', 'another', 'answer', 'anyone', 'anything', 'airport', 'already', 'amazing', 'ancient', 'apartment', 'apparent', 'arrange', 'article', 'attempt', 'balance', 'battery', 'because', 'bedroom', 'believe', 'between', 'bicycle', 'biology', 'building', 'business', 'calendar', 'camera', 'capital', 'careful', 'carried', 'central', 'century', 'certain', 'chapter', 'charity', 'chicken', 'citizen', 'classic', 'climate', 'clothing', 'college', 'comfort', 'command', 'company', 'compare', 'complete', 'computer', 'concern', 'concert', 'connect', 'control', 'correct', 'country', 'courage', 'culture', 'curious', 'current', 'customer', 'danger', 'decided', 'default', 'deliver', 'describe', 'design', 'despite', 'develop', 'diamond', 'digital', 'dinner', 'discuss', 'disease', 'display', 'distance', 'drawing', 'earlier', 'eastern', 'economy', 'edition', 'educate', 'effort', 'elegant', 'element', 'emotion', 'emperor', 'employee', 'enough', 'example', 'excited', 'exercise', 'expense', 'explain', 'explore', 'factory', 'failure', 'fashion', 'feature', 'feeling', 'fiction', 'finally', 'finance', 'finding', 'fitness', 'flavor', 'forward', 'freedom', 'gallery', 'general', 'gesture', 'glasses', 'goodness', 'grammar', 'grandma', 'grandpa', 'greater', 'grocery', 'habitat', 'happily', 'healthy', 'history', 'holiday', 'however', 'hundred', 'husband', 'imagine', 'improve', 'include', 'income', 'increase', 'industry', 'initial', 'inquiry', 'instant', 'instead', 'instruct', 'involved', 'island', 'journal', 'journey', 'justice', 'kitchen', 'language', 'largest', 'library', 'limited', 'machine', 'manager', 'meaning', 'measure', 'medical', 'meeting', 'mention', 'message', 'million', 'minimum', 'mixture', 'monitor', 'musical', 'natural', 'neither', 'network', 'nothing', 'notable', 'nuclear', 'observe', 'obvious', 'officer', 'opening', 'opinion', 'organic', 'package', 'painting', 'parents', 'passion', 'patient', 'pattern', 'payment', 'percent', 'perfect', 'perhaps', 'picture', 'plastic', 'popular', 'portion', 'position', 'possible', 'powerful', 'prepare', 'present', 'printer', 'private', 'problem', 'process', 'produce', 'product', 'program', 'project', 'promise', 'purpose', 'quality', 'quarter', 'quickly', 'quietly', 'reading', 'reality', 'receive', 'regular', 'related', 'remember', 'replace', 'request', 'respect', 'result', 'routine', 'science', 'section', 'serious', 'service', 'session', 'setting', 'several', 'similar', 'society', 'special', 'station', 'storage', 'subject', 'success', 'suggest', 'support', 'surface', 'system', 'thought', 'through', 'together', 'tonight', 'towards', 'traffic', 'training', 'trouble', 'usually', 'various',
         'village', 'visible', 'weather', 'weekend', 'welcome', 'western', 'without', 'working', 'writing', 'accurate', 'acquire', 'activate', 'adequate', 'adjacent', 'advocate', 'allocate', 'alternate', 'ambition', 'analysis', 'announce', 'annual', 'anxiety', 'approach', 'approval', 'argument', 'assistant', 'atmosphere', 'attitude', 'audience', 'available', 'awkward', 'benefit', 'boundary', 'brilliant', 'calculate', 'campaign', 'capacity', 'category', 'celebrate', 'challenge', 'character', 'chemical', 'clarify', 'colleague', 'combine', 'community', 'complex', 'component', 'concentrate', 'conclusion', 'confidence', 'consequence', 'consider', 'consistent', 'construct', 'consume', 'convenient', 'convince', 'creative', 'database', 'deliberate', 'delivery', 'demonstrate', 'department', 'dependent', 'desperate', 'determine', 'diagram', 'difference', 'difficult', 'direction', 'disaster', 'discover', 'discussion', 'document', 'dramatic', 'duration', 'efficient', 'elaborate', 'electricity', 'eliminate', 'emotional', 'encourage', 'enormous', 'entertain', 'environment', 'equipment', 'establish', 'estimate', 'evaluate', 'evidence', 'excellent', 'familiar', 'fascinating', 'favorite', 'flexible', 'frequent', 'generous', 'genuine', 'gradually', 'guarantee', 'guidance', 'identify', 'illustrate', 'immediate', 'impressive', 'independent', 'individual', 'influence', 'information', 'ingredient', 'innovative', 'inspire', 'instrument', 'intelligent', 'intention', 'introduce', 'investigate', 'invisible', 'invitation', 'knowledge', 'leadership', 'legendary', 'location', 'maintain', 'majority', 'manufacture', 'material', 'memorable', 'moderate', 'motivate', 'necessary', 'negative', 'negotiate', 'noticeable', 'objective', 'obstacle', 'occasion', 'official', 'operate', 'opportunity', 'ordinary', 'organize', 'original', 'participate', 'particular', 'patience', 'performance', 'permanent', 'personality', 'perspective', 'persuade', 'phenomenon', 'physical', 'practical', 'precious', 'precise', 'predict', 'prefer', 'previous', 'principle', 'priority', 'procedure', 'profession', 'progress', 'pronounce', 'protect', 'provide', 'publish', 'purchase', 'qualification', 'recognize', 'recommend', 'recover', 'reference', 'relationship', 'relevant', 'reliable', 'remarkable', 'represent', 'require', 'research', 'resource', 'responsibility', 'restaurant', 'ridiculous', 'sacrifice', 'satisfactory', 'scientific', 'secondary', 'security', 'significant', 'solution', 'specific', 'strategy', 'structure', 'successful', 'sufficient', 'surprising', 'temporary', 'technique', 'technology', 'tremendous', 'understand', 'unusual', 'valuable', 'variation', 'vehicle', 'version', 'victory']


tier3 = ['aberration', 'abhor', 'abnormality', 'abolition', 'abridgment', 'abstention', 'abundance', 'accelerate', 'accolade', 'accomplice', 'accumulate', 'acrimony', 'adaptation', 'adversity', 'aesthetic', 'affection', 'aggregate', 'allegiance', 'ambiguous', 'ambivalence', 'amendment', 'amiable', 'amplification', 'anachronism', 'analytical', 'animosity', 'anomaly', 'antagonist', 'anticipation', 'antiquated', 'apathy', 'apprehension', 'arbitrary', 'articulate', 'ascertain', 'aspiration', 'assimilate', 'astounding', 'auspicious', 'authentic', 'autonomous', 'belligerent', 'benevolent', 'bewilder', 'blasphemy', 'bureaucracy', 'cacophony', 'calamity', 'candid', 'capitulate', 'catastrophe', 'caustic', 'celestial', 'censorship', 'charismatic', 'chronic', 'circumstance', 'coherent', 'collaborate', 'commemorate', 'commencement', 'compassion', 'competence', 'complacent', 'complement', 'complication', 'comprehensive', 'conception', 'conclusive', 'concurrent', 'condescending', 'confidential', 'consequence', 'conservative', 'conspicuous', 'constellation', 'contemplate', 'contentious', 'contradiction', 'controversial', 'conventional', 'conviction', 'correlation', 'credibility', 'criterion', 'cumulative', 'declaration', 'deduction', 'deficiency', 'deliberate', 'demonstrate', 'denunciation', 'deprivation', 'derivative', 'descriptive', 'deteriorate', 'diligence', 'discrepancy', 'discretion', 'discrimination', 'disposition', 'disseminate', 'distinction', 'divergence', 'elaboration', 'eloquence', 'emancipation', 'embellishment', 'empirical', 'endeavor', 'enigmatic', 'enormous', 'entrepreneur', 'equilibrium', 'equivalent', 'eradicate', 'escalation', 'essential', 'exaggeration', 'exasperation', 'exemplary', 'exhaustive', 'existential', 'expenditure', 'exponential', 'facilitate', 'formidable', 'formulation', 'fortitude', 'frivolous', 'fundamental', 'futuristic', 'gregarious', 'hierarchy', 'hypothesis', 'hypothetical', 'idiosyncrasy', 'illegitimate', 'illustrious', 'immaculate', 'immaterial', 'imminent', 'impartial', 'imperative', 'imperceptible', 'implication', 'inaccessible', 'inadvertent', 'incentive', 'incoherent', 'incompatible', 'inconclusive', 'inconsistent', 'indefinite', 'independent', 'indispensable', 'indisputable', 'inevitable', 'inexplicable', 'infrastructure', 'ingenious', 'inherent', 'innovation', 'insatiable', 'insignificant', 'insinuation', 'integrity', 'intellectual', 'intelligence', 'interference', 'intermediate', 'interpretation', 'intimidation', 'intolerance', 'intriguing', 'intuition', 'irrelevant', 'irresistible', 'legitimate', 'legislation', 'magnificent', 'meticulous', 'misconception', 'miscellaneous', 'mitigation', 'monotonous', 'negligible', 'notorious', 'obligation', 'observation', 'obstruction', 'occurrence', 'opposition', 'ostentatious', 'paradigm', 'paradoxical', 'perception', 'perseverance', 'phenomenon', 'philosophical', 'plausibility', 'precarious', 'predicament', 'preliminary', 'preservation', 'proclamation', 'procrastination', 'proficiency', 'profound', 'proliferation', 'proposition', 'provisional', 'quintessential', 'rationality', 'reconciliation', 'redundancy', 'rejuvenation', 'relinquish', 'reminiscence', 'renaissance',
         'repercussion', 'resilience', 'resolution', 'retrospective', 'revolutionary', 'scrutinize', 'significance', 'simultaneous', 'skepticism', 'spontaneous', 'substantial', 'superficial', 'surveillance', 'susceptible', 'sustainable', 'systematic', 'transformation', 'transgression', 'transmission', 'transparent', 'unprecedented', 'versatility', 'vulnerability', 'abbreviation', 'abominable', 'abstruse', 'acclimatization', 'acknowledgment', 'acquiescence', 'adjudication', 'admonishment', 'advantageous', 'aestheticism', 'aforementioned', 'aggravating', 'allegorical', 'amelioration', 'anachronistic', 'anesthesiology', 'anthropological', 'antithetical', 'apocalyptic', 'apprehensive', 'archaeological', 'aristocratic', 'articulation', 'assimilative', 'authoritative', 'autobiography', 'beneficial', 'biographical', 'characteristic', 'circumstantial', 'clarification', 'collaboration', 'commemorative', 'commercialization', 'compassionate', 'compatibility', 'complementary', 'computational', 'concentration', 'conscientious', 'consciousness', 'consequential', 'consideration', 'constitutional', 'contemporary', 'contradictory', 'correspondence', 'crystallization', 'customizable', 'decipherable', 'decomposition', 'deterioration', 'determination', 'differentiation', 'disadvantage', 'disciplinary', 'disconcerting', 'disproportionate', 'documentation', 'eccentricity', 'effectiveness', 'egregious', 'electromagnetic', 'eloquently', 'encouragement', 'encyclopedia', 'entrepreneurial', 'environmental', 'epidemiology', 'equivalence', 'establishment', 'evolutionary', 'exceptionally', 'examination', 'exhilarating', 'extraordinary', 'familiarity', 'fermentation', 'flourishing', 'functionality', 'geographical', 'governmental', 'gratification', 'gravitational', 'hallucination', 'heterogeneous', 'hierarchical', 'humanitarian', 'identification', 'ideological', 'illumination', 'immeasurable', 'implementation', 'impossibility', 'improvisation', 'inauguration', 'incarceration', 'incomparable', 'incompatibility', 'inconsequential', 'inconsistency', 'incorporation', 'independence', 'individualistic', 'industrialization', 'inefficiency', 'ingenuity', 'inhibition', 'initiative', 'institutional', 'instantaneous', 'instructional', 'instrumental', 'insufficient', 'jurisdiction', 'justification', 'knowledgeable', 'malformation', 'manipulation', 'mathematical', 'measurement', 'melancholic', 'metamorphosis', 'meticulousness', 'misinterpretation', 'misunderstanding', 'monumental', 'multiplication', 'mutually', 'negotiation', 'nevertheless', 'nonchalant', 'occasionally', 'omniscient', 'optimization', 'organizational', 'originality', 'outstanding', 'participation', 'picturesque', 'predominantly', 'prerequisite', 'prestigious', 'probability', 'problematic', 'pronunciation', 'psychological', 'qualification', 'questionable', 'recommendation', 'recognizable', 'reconstruction', 'reconsideration', 'redistribution', 'rehabilitation', 'relationship', 'remarkable', 'representation', 'responsibility', 'sophistication', 'specification', 'susceptibility', 'synchronization', 'terminology', 'theoretical', 'thoroughly', 'transcendental', 'trustworthy', 'uncertainty', 'understanding', 'unfortunately', 'unprecedentedly']


newadditions = ["osseocarnisanguineoviscericartilaginonervomedullary", "bababadalgharaghtakamminarronnkonnbronntonnerronntuonnthunntrovarrhounawnskawntoohoohoordenenthurnuk", "perkodhuskurunbarggruauyagokgorlayorgromgremmitghundhurthrumathunaradidillifaititillibumullunukkunun", "klikkaklakkaklaskaklopatzklatschabattacreppycrottygraddaghsemmihsammihnouithappluddyappladdypkonpkot"'taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu', 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch', 'aequeosalinocalcalinoceraceoaluminosocupreovitriolic', 'chargoggagoggmanchauggagoggchaubunagungamaugg', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'fructosebisphosphatetriosephosphatelyase', 'ribulosebisphosphatecarboxylaseoxygenase', 'dermatofibrosislenticularisdisseminata', 'hepaticocholangiocholecystenterostomy', 'hexanitrohexaazatricyclododecanedione', 'juxtaanastomoticneointimalhyperplasia', 'scaphotrapeziotrapezoidosteoarthritis', 'uridinediphosphateglycosyltransferase', 'chondromyxohemangioendotheliosarcoma', 'hippopotomonstrosesquippedaliophobia', 'phosphorodiamidatemorpholinooligomer', 'congenitalnasalmeningoencephalocele', 'dimethyldioctadecylammoniumchloride', 'encephalocraniocutaneouslipomatosis', 'hypothalamicpituitaryadrenocortical', 'cholangiocholecystocholedochectomy', 'paroxysmalnocturnalhaemoglobinuria',
                'supercalifragilisticexpialidocious', 'acrocephalopolydactylousdysplasia', 'corynebacteriumpseudotuberculosis', 'laparohysterosalpingooophorectomy', 'percutaneousendoscopicgastrostomy', 'subacutesclerosingpanencephalitis', 'xanthogranulomatouspyelonephritis', 'orotatephosphoribosyltransferase', 'canaliculodacryocystorhinostomy', 'dichlorodiphenyltrichloroethane', 'pseudopseudohypoparathyroidism', 'floccinaucinihilipilification', 'hexakosioihexekontahexaphobia', 'methylenedioxymethamphetamine', 'antidisestablishmentarianism', 'hepaticocholangiogastrostomy', 'spectrophotofluorometrically', 'electroencephalographically', 'honorificabilitudinitatibus', 'psychoneuroendocrinological', 'radioimmunoelectrophoresis', 'psychopharmacotherapeutics', 'counterrevolutionaries', 'electroencephalography', 'immunohistochemistry', 'incomprehensibilities', 'deinstitutionalization', 'internationalization', 'mischaracterization', 'microarchitecture', 'multidimensionality', 'neuropsychological', 'otorhinolaryngological', 'psycholinguistics', 'spectrophotometry', 'telecommunications', 'uncharacteristically', 'unconstitutionality', 'overintellectualization', 'anthropomorphization', 'compartmentalization', 'disestablishmentarianism', 'incomprehensibility', 'institutionalization', 'magnetohydrodynamics', 'microspectrophotometry', 'psychoneuroimmunology', 'radioimmunoassay', 'transubstantiation']


allwords = list(dict.fromkeys(tier1 + tier2 + tier3 + newadditions))

wordspool = {

    '1': [word for word in allwords if len(word) <= 4],

    '2': [word for word in allwords if 5 <= len(word) <= 7],

    '3': [word for word in allwords if 8 <= len(word) <= 12],

    '4': [word for word in allwords if 13 <= len(word) <= 30],

    '5': [word for word in allwords if len(word) >= 35],

}


while True:

    clearterminal()

    print('=' * 54)

    print('              SPELLING BEE CHALLENGE')

    print('=' * 54)

    print('1. Simple      ({})'.format(len(wordspool['1'])))

    print('2. Medium      ({})'.format(len(wordspool['2'])))

    print('3. Hard        ({})'.format(len(wordspool['3'])))

    print('4. Long        ({})'.format(len(wordspool['4'])))

    print('5. Master      ({})'.format(len(wordspool['5'])))

    print("Type 'exit' to quit.")

    print('=' * 54)

    choice = input('Choose a difficulty: ').strip().lower()

    if choice == 'exit':

        print('Thanks for playing!')

        break

    if choice not in wordspool:

        print('Please choose a number from 1 to 5.')

        time.sleep(1.5)

        continue

    availablewords = wordspool[choice]

    if not availablewords:

        print('There are no words in this difficulty yet.')

        time.sleep(1.5)

        continue

    try:

        amount = int(input('How many words do you want to spell? ').strip())

        if amount < 1:

            print('Enter a number greater than 0.')

            time.sleep(1.5)

            continue

    except ValueError:

        print('Please enter a valid number.')

        time.sleep(1.5)

        continue

    amount = min(amount, len(availablewords))

    selectedwords = random.sample(availablewords, amount)

    score = 0

    for number, targetword in enumerate(selectedwords, 1):


        clearterminal()

        print('Word {} of {}'.format(number, amount))

        print('Listen carefully:')

        engine.say(targetword)
        engine.runAndWait()

        clearterminal()

        guess = input('Spell the word (or type exit to quit): ').strip().lower()

        if guess == 'exit':

            print('Thanks for playing!')

            raise SystemExit

        if guess == targetword:

            print('\nCorrect! Great work.')
