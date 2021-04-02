#readability

#loop through all letters in string to figure out how many letters, words, and sentences there are
#read through assignment closely for details and examples
#use the Coleman-Liau index formula to find the grade level
#test for below grade 1 and above grade 16

wordCount=0
letterCount=0
sentenceCount=0

#this defines the fuction that will count letters in whatever string it receives 
def countLetters(text):
    count = 0
    for character in text:
        if (character.isalpha()):
            count += 1
    return count
#this defines the fuction that will count words in whatever string it receives
def countWords(text):
    count = 0
    for character in text:
        if(character == " "):
            count += 1
    return count
#this defines the function that will count sentences in whatever string it receives
def countSentences(text):
    


#run the input function and save the input into
#the variable calle inputText
inputText = input("Enter your text: ")


#call the countLetters fucntion and send it the input
#this function call is missing the required argument
letterCount = countLetters(inputText)

#call the countWords function and send it the input
#this function call is missing the required argument
wordCount = countWords()

#call the countSetences function and send it the input
#this function call is missing the required argument
sentenceCount = countSentences()





#do something with the letter/word/sentence counts to calculate the L & S







#use the Coleman-Liau formula to calculate the grade level








#round the grade level






#check if the grade level is below 1, print ("Grade level below 1")
#check if grade level is above 16, print ("Grade level 16+")
#else just print the grade level 






