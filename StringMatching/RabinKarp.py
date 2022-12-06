## String matching Algorithm
## Rabin-Karp ALgorithm

class RabinKarp:
    def __init__(self,text,pattern, prime_number = 13):
        self.text = text
        self.pattern = pattern
        
        self.prime_number = prime_number ## default 13 

        self.pattern_length = len(self.pattern)
        self.text_length = len(self.text)

        self.hash_pattern = 0    # hash value for pattern
        self.hash_text = 0    # hash value for txt

    
    def search(self):

        i = 0
        j = 0
        h = 1
        counter = 0
        iterator_outter_loop = 0
        iterator_inner_loop = 0
        location = []
        for i in range(self.pattern_length-1):
            h = (h*self.text_length)

        #Calculate hash of pattern and text

        for i in range(self.pattern_length):
            self.hash_pattern = (self.text_length * self.hash_pattern + ord(self.pattern[i])) % self.prime_number
            self.hash_text = (self.text_length * self.hash_text + ord(self.text[i])) % self.prime_number

        
        for i in range(self.text_length - self.pattern_length + 1):
            iterator_outter_loop += 1
            if self.hash_pattern == self.hash_text:

                for j in range(self.pattern_length):
                    iterator_inner_loop += 1
                    if self.text[i+j]  != self.pattern[j]:
                        break
                    else:
                        j += 1
                if j == self.pattern_length:
                    counter += 1
                    location.append(i)
            if i < self.text_length-self.pattern_length:
                self.hash_text = (self.text_length *(self.hash_text - ord(self.text[i])*h) + ord(self.text[i+self.pattern_length])) % self.prime_number

                if self.hash_text < 0:
                    self.hash_text = self.hash_text + self.prime_number

        return (counter,iterator_inner_loop+iterator_outter_loop,self.pattern_length + self.text_length,self.pattern_length * self.text_length,location)
        




if __name__ == '__main__':
    
    file = open("The Complete Works of William Shakespeare.txt", "r", encoding='UTF-8')
    doc = file.readlines() 
    text = "".join(doc)

    pattern = "Book"
    q = 11
    SM = RabinKarp(text,pattern,q)
    out = SM.search()
    print(f"Pattern found {out[0]:,} times.")
    print(f"Pattern found on loactions: {out[4]}.")
    print(f"Total number of loop iterations: {out[1]:,}.")
    print(f"Expected Best or Average case time complexity:{out[2]:,}.")
    print(f"Expected Worst case time complexity:{out[3]:,}.")