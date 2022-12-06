class Naive:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.pattern_length = len(self.pattern)
        self.text_length = len(self.text)
        self.location = []
    
    def search(self):
        loop_counter = 0
        for i in range(self.text_length - self.pattern_length + 1):
            loop_counter += 1
            counter = 0
            while (counter < self.pattern_length):
                loop_counter += 1
                if self.text[i+ counter] != self.pattern[counter]:
                    break
                else:
                    counter += 1
            
            if counter == self.pattern_length:
                self.location.append(i)
        
        return(len(self.location),loop_counter,self.text_length,self.text_length*self.text_length,self.location)


if __name__ == '__main__':
    
    file = open("The Complete Works of William Shakespeare.txt", "r", encoding='UTF-8')
    doc = file.readlines() 
    text = "".join(doc)

    pattern = "Book"
    SM = Naive(text,pattern)
    out = SM.search()
    print(f"Pattern found {out[0]:,} times.")
    print(f"Pattern found on loactions: {out[4]}.")
    print(f"Total number of loop iterations: {out[1]:,}.")
    print(f"Expected Best or Average case time complexity:{out[2]:,}.")
    print(f"Expected Worst case time complexity:{out[3]:,}.")