def compute_prefix_fun(pattern):
    m=len(pattern)
    pre=[0]*m
    k=0
    for q in range(1,m):
        while k and pattern[k]!=pattern[q]:
            k=pre[k-1]
        if pattern[k]==pattern[q]:
            k=k+1 
        pre[q]=k
    return pre


def kmp(pattern,text):
    n= len(text)
    m=len(pattern)
    pre=compute_prefix_fun(pattern)
    q=0
    match_loc = []
    for i in range(n):
        # print("match locations: ",match_loc)
        while q and pattern[q]!=text[i]:
            q=pre[q-1]
        if pattern[q]==text[i]:
            if q==m-1:
                match_loc.append(i-q)
                q = pre[q]
            else:
                q=q+1
    return match_loc

            
text="aaaaaaaa"
pattern="aa"
k=kmp(pattern,text)
print(k)