class KMP:
    def __init__(self,text,pattern):
        self.text = text
        self.pattern = pattern
        self.pattern_length = len(self.pattern)
        self.text_length = len(self.text)

    def compute_prefix_fun(self):
        k=0
        prefix = [0]*self.pattern_length
        for i in range(1,self.pattern_length):
            while k and self.pattern[k]!=self.pattern[i]:
                k=prefix[k-1]
            if self.pattern[k]==self.pattern[i]:
                k=k+1 
            prefix[i]=k
        return prefix


    def search(self):
        prefix=self.compute_prefix_fun()
        q=0
        match_loc = []
        for i in range(self.text_length):
            while q and self.pattern[q]!=self.text[i]:
                q=prefix[q-1]
            if self.pattern[q]==self.text[i]:
                if q==self.pattern_length-1:
                    match_loc.append(i-q)
                    q = prefix[q]
                else:
                    q=q+1
        return match_loc


if __name__ == '__main__':        
    text="aaaaaaaa"
    pattern="aa"
    k=KMP(text,pattern)
    print(k.search())s