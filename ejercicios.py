def staircase(n):
    espacios_num = n-1
    caracteres_num = 1
    if n < 0 or n >100:
        print("N debe ser un numero mayor que 0 y menor o igual a 100")
    else:
        for i in range(n):
            print((" "*espacios_num)+("#"*caracteres_num))
            espacios_num-=1
            caracteres_num+=1

staircase(7)


def sherlockAndAnagrams(s):
    contador = 0
    for i in range(1, len(s)):
        d={}
        for j in range(len(s)-i+1):
            ss = "".join(sorted(s[j:j+i]))
            if ss not in d:
                d[ss]=1
            else:
                d[ss]+=1
            contador += d[ss]-1
    return contador

print(sherlockAndAnagrams("mom"))


def shortPalindrome(s):
    contador = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[j] == s[k]:
                    contador += s[k+1:].count(s[i])
    return contador%((10**9)+7)

print(shortPalindrome("kkkkkkz"))