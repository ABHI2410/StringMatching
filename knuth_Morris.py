def compute_prefix_fun(pattern):
    m=len(pattern)
    pre=["0"]*10
    pre[1]=0
    k=0
    for q in range(2,m):
        while k>0 and pattern[k+1]!=pattern[q]:
            k=pre[k]
        if pattern[k+1]==pattern[q]:
            k=k+1 
        pre[q]=k
    return pre


def kmp(pattern,text):
    n= len(text)
    m=len(pattern)
    pre=compute_prefix_fun(pattern)
    q=0
    for i in range(0,n):
        while q>0 and pattern[q+1]!=text[i]:
            q=pre[q]
        if pattern[q+1]==text[i]:
            q=q+1 
        if q==m:
            return i-m
            q=pre[q]

            
text=input("Enter the text: ")
pattern=input("Enter the Pattern: ")
k=kmp(pattern,text)
print(k)