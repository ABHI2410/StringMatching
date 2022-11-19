## String matching Algorithms
## Robin-Karp ALgorithm
## Knuth-Morris-Pratt Algorithm


class StringMatching:
    def __init__(self,text,pattern, prime_number = 13):
        self.text = text
        self.pattern = pattern
        
        self.prime_number = prime_number ## default 13 

        self.pattern_length = len(self.pattern)
        self.text_length = len(self.text)

        self.hash_pattern = 0    # hash value for pattern
        self.hash_text = 0    # hash value for txt

    
    def RobinKarp(self):

        i = 0
        j = 0
        h = 1
        counter = 0
        for i in range(self.pattern_length-1):
            h = (h*self.text_length)

        #Calculate hash of pattern and text

        for i in range(self.pattern_length):
            self.hash_pattern = (self.text_length * self.hash_pattern + ord(self.pattern[i])) % self.prime_number
            self.hash_text = (self.text_length * self.hash_text + ord(self.text[i])) % self.prime_number


        for i in range(self.text_length - self.pattern_length + 1):
            if self.hash_pattern == self.hash_text:

                for j in range(self.pattern_length):
                    if self.text[i+j]  != self.pattern[j]:
                        break
                    else:
                        j += 1
                if j == self.pattern_length:
                    counter += 1
                    print("Pattern found at index " + str(i))
            if i < self.text_length-self.pattern_length:
                self.hash_text = (self.text_length *(self.hash_text - ord(self.text[i])*h) + ord(self.text[i+self.pattern_length])) % self.prime_number

                if self.hash_text < 0:
                    self.hash_text = self.hash_text + self.prime_number
        
        print(f"Pattern found {counter} times.")



if __name__ == '__main__':

    file = open("./1960-09-26.txt").readlines()
    data = []
    for s in file:
        data.append(s.rstrip('\n')) 
    text = "".join(data)

    pattern = "President"
    q = 11
    SM = StringMatching(text,pattern)
    SM.RobinKarp()