class analysedText(object):
    
    def __init__ (self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        formattedText = text.replace('.','').replace(',','').replace('!','').replace('?','').lower()
        
        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = formattedText
        pass 
    
    def freqAll(self):    

        # TODO: Split the text into a list of words  
        word = self.fmtText.split(' ')
        # TODO: Create a dictionary with the unique words in the text as keys
        freqMap = {}
        for uniqueWord in set(word):
            freqMap[uniqueWord] = word.count(uniqueWord)
        # and the number of times they occur in the text as values
        return freqMap
        pass # return the created dictionary
        
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        freqMap = self.freqAll()
        if word in freqMap:
            return freqMap[word]
        else:
            return 0
        pass
        
# def main():
#     text = analysedText("hi hi hi you you, how are you!")
#     text.freqAll()
#     print(text.freqOf("hi"))
# main()
