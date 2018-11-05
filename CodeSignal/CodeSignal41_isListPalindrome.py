def isListPalindrome(l):
    p = []
    while l != None:
        p.append(l.value)
        l = l.next
    return all([p[x:x+1] == p[-1-x:len(p)-x] for x in range(len(p)//2)]) # or p == p[::-1]
