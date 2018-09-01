
# print("Jack and Jill Went up the hill \n To fetch a pail of water\
# \n Jack fell down\n And broke his crown,\n And Jill came tumbling after.")
#
# print("Jack and Jill Went (adjective) the hill \n To fetch a (noun) of (noun)\
# \n Jack (verb) down \n And broke his (noun),\n And Jill (verb) (verb) after.")

# '''   print first portion of text until first input.
#       recieve input then place input into slot.
#       print second portion then add next input
#       continue process until all slots are filled then
#        print entire statement.
# '''

fullText = ["Jack and Jill Went", "the hill To fetch a", "of"
 "Jack  down", "And broke his", "And Jill", " after."]
addBlank = " ____"
inserts = ["adjective: ","noun: ","noun: ","verb: ","noun: ","verb: ","verb: "]
verseNumbers = ["firstVerse","SecondVerse","ThirdVerse","FourthVerse",]
index = 0

def inputText(index):
    while index < (len(fullText) - 1):
        print("{}{}".format(fullText[index], addBlank))
        verseNumbers[index] = input("{} ".format(inserts[index]))
        print("{} {}".format(fullText[index], verseNumbers[index]))
        index += 1

def insertText():
    firstText = "Jack and Jill Went ___"
    print(firstText)
    firstVerse = input("Adjective: ")
    print("{}{}".format(firstText[0:len(firstText) - 3], firstVerse))
    secondText = "the hill to fetch a ___"
    print(secondText)
    secondVerse = input("noun: ")
    print("{}{}".format(secondText[0:len(secondText) - 3], secondVerse))
    thirdText = "of ___"
    print(thirdVerse)
    thirdVerse = input("noun: ")
    print("{}{}".format(thirdText[0:len(thirdText) - 3], thirdVerse))

def firstRun():
    inputText(index)

# while index > len(fullText):
firstRun()






























# newText = "yess this is new text"
# print(len(newText) - 3)
