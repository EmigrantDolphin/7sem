# ##################
# 1) Paaiškinti kaip veikia ir kam gali būti naudojamas Decision Tree Exploration 
# 	(in information transfer)
# 
# Veikia naudojant skirtumo konceptą. Kai vienas daiktas/idėja turi du skirtumus/būsenas, pavyzdžiui degtukas gali būti užsidegęs arba ne. Tai tas vienas daiktas turi du skirtingus informacijos vienietus.
# Tai galima pazymeti kaip 2^1. Tada jeigu turim du tokius pačius daiktus ir kiekvienas turi tiek pat skirtumų, jų kombinavimas suteikia 4 skirtingus informacijos vienetus. Tada galima susitarti su visais, jog vienas unikalus skirtumas, turi tam tikrą reikšmę. Tai turėdami du degtukus, galime pavaizduoti 4 skirtingas reikšmes. Na ir taip pridėdant tų kombinacijų galima išreikšti abėcėlę. 


import random

#1.2 TEXT TO MORSE CODE CONVERTER
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def printTextInMorseCode(text):
    print("converted text: text")
    for letter in text:
        print(MORSE_CODE_DICT[letter], end=" ")
    print()

#####################

#1.3 MARKOV CHAIN SIMULATION
def markovChain(probabilityOfStayingOnOne, probabilityOfStayingOnZero, actionCount):
    state = 0
    zeroCounter = 0
    for i in range(actionCount):
        if (state == 0):
            if (random.uniform(0, 1) > probabilityOfStayingOnZero):
                state = 1
            else:
                zeroCounter += 1
            #print(state)
        else:
            if (random.uniform(0, 1) > probabilityOfStayingOnOne):
                state = 0
                zeroCounter += 1
            #print(state)
    print("Zero occured times: " + str(zeroCounter) + ". One occured times: " + str(actionCount - zeroCounter))

########################

#1.4 1.5 MARKOV TEXT GENERATING SIMULATION
def generateMarkovDictionary(text, order):
    textArray = text.split()
    dictionary = dict()
    #while len(textArray) > 2:
    dictionaryKeys = [' '.join(textArray[i:i+order]) for i in range(0, len(textArray),order)]
    print(dictionaryKeys)
#        if (dictionaryKeys[1].split())
#        dictionary[dictionaryKeys[0]] = dictionaryKeys[1].split()[0]
#        textArray.pop(0)
#    for i, word in enumerate(textArray):
#        if (i >= order):
#            dictionaryKey = ""
#            for i in range(order):
#                dictionaryKey += 
#            print(textArray[i])
    return text


def markovTextChain():
    text = "A tall human tribesman strides through a blizzard, draped in fur and hefting his axe. He laughs as he charges toward the frost giant who dared poach his people’s elk herd. A half-orc snarls at the latest challenger to her authority over their savage tribe, ready to break his neck with her bare hands as she did to the last six rivals. Frothing at the mouth, a dwarf slams his helmet into the face of his drow foe, then turns to drive his armored elbow into the gut of another. These barbarians, different as they might be, are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling eservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength. People of towns and cities take pride in how their civilized ways set them apart from animals, as if denying one’s own nature was a mark of superiority. To a barbarian, though, civilization is no virtue, but a sign of weakness. The strong embrace their animal nature—keen instincts, primal physicality, and ferocious rage. Barbarians are uncomfortable when hedged in by walls and crowds. They thrive in the wilds of their homelands: the tundra, jungle, or grasslands where their tribes live and hunt. Barbarians come alive in the chaos of combat. They can enter a berserk state where rage takes over, giving them superhuman strength and resilience. A barbarian can draw on this reservoir of fury only a few times without resting, but those few rages are usually sufficient to defeat whatever threats arise."
    wordDictionary = generateMarkovDictionary(text, 3)

    # create ngram list. Where order is number of letters and these letters become dictionary key,
    #   while dictionary value is the array of next possible letters that appear after that key in text.
    # cycle N times with predefined ngram value. Find that ngram value in dictionary. Get random value from the value list.
    # Append it to text. Take last orderVar of character from text string and repeat with that

print("#1.2 Name in morse code")
printTextInMorseCode("NORMAN,BUIKO")
print()
print()
print("#1.3 Markov chain simulation")
markovChain(probabilityOfStayingOnZero = 0.1, probabilityOfStayingOnOne = 0.9, actionCount = 1000)
print()
print()
print("#1.4/5 n-gram text generation")
markovTextChain()