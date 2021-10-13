s = input()
words = s.split()
def stat(words):
    str = len(words)
    if str == 0:
        print("-1")
    else:
        n = 1
        povt = [None] * str
        povt[0] = words[0]
        count = [0] * str
        count[0] = 1
        i = 1
        j = 0
        while (i < str):
            if (j < n) and (words[i] != povt[j]):
                j += 1
            elif (j == n):
                povt[j] = words[i]
                n += 1
                count[j] = 1
                j = 0
                i += 1
            else:
                count[j] += 1
                i += 1
        c = str - n
        if (c != 0):
            del povt[-c:]
            del count[-c:]
        m = max(count)
        l = min(count)
        p = 0
        pol = 0
        while (p < n):
            if (count[p] == m):
                most = povt[p]
            if (count[p] == l):
                least = povt[p]
            p += 1
        number = sorted(povt)
        for k in range(n):
            bool = False
            i = 0
            while(bool == False):
                if (number[k] == povt[i]):
                    bool = True
                else:
                    i += 1
            print(number [k], ": ", count[i])
            if (povt[k] == povt[k][::-1]):
                pol += count[k]
        print("Most common: ", most)
        print("Least common: ", least)
        print("Palindroms: ", pol)

stat(words)