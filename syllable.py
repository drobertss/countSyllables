import pandas
import numpy as np
import nltk

# Count syllables in a word
def syllables(word):
    if(word == None or word == "" or word == " "):
        return -999999
    word = str(word)
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count+=1
    if count == 0:
        count +=1
    return count




df = pandas.read_csv("""LOCATION OF CSV""", low_memory=False)

#Iterate through data frame
#Get values in Animal.Name column
#Count syllables in name and create new column with number of syllables
location =0
for index, row in df.iterrows():
    name = row['Animal.Name']
    name = str(name)
    numLetters = len(str(name))
    hyphendName = name
    numSyll = syllables(name)

    #print ('Number of syllables in name ' + str(name) + ' is ' + str(numSyll) )

    #print ('The length of the name is ' + str(numLetters))

    for i in range(numLetters):

        # No hyphen to insert if there is only one syllable
        if(numSyll == 1):
            hyphendName = name
            break
        # Check if length of word is divisible by number of syllables
        # Inserts hyphen into then name
        if(numLetters % numSyll == 0):
            hyphendName = name[0:numLetters/numSyll] + '-' + name[numLetters/numSyll:]
            #print(hyphendName)
        elif(numLetters % numSyll != 0):
            inc = numLetters /numSyll
            counter = 0
            lenCounter = 0
            hyphenList = []
            if(numSyll == 2):
                hyphendName = name[:numSyll] + '-' +  name[numSyll:]
                #print(hyphendName)
            else:
                for i in range(numLetters):

                    if (counter==numSyll):
                        hyphenList.append(i)
                        counter = 0
                    counter = counter + 1
                    lenCounter = counter + 1

                for i in hyphenList:
                    hyphendName = name[:i] + "-" + name[i:]
                    #print(hyphendName)


    # Add value to dataframe where df ID[0]  == index
    df.loc[index, 'Syllables'] = str(syllables(name))
    df.loc[index, 'HyphenSyll'] = str(hyphendName)


df.to_csv("""NEW SYLLABUS CSV DIR\\ syllables.csv """)


