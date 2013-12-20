#Pig Latin -
#Pig Latin is a game of alterations played on the English language game.
#To create the Pig Latin form of an English word the initial consonant sound is transposed
#to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
#Read Wikipedia for more information on rules.

vowels = 'aeiou'

phrase = raw_input("Input a word for translation into Pig Latin: ")

if (not(any(phrase[0].lower() in ch for ch in vowels))):
   phrase = phrase[1:] + phrase[0] + 'ay'
else:
    phrase = phrase + 'ay'

print phrase