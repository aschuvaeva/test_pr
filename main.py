s = input()
words = s.split()


def stat(words):
    if len(words) != 0:
        counts = dict()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        sorted_counts = dict(sorted(counts.items()))
        for k, v in sorted_counts.items():
            print(k, ':', v)
        most_common = max(sorted_counts, key=sorted_counts.get)
        least_common = min(sorted_counts, key=sorted_counts.get)
        print('Most common:', most_common)
        print('Least common:', least_common)
        pal = 0
        for word in words:
            if word == word[::-1]:
                pal += 1
        print('Palindroms:', pal)
    else:
        print("-1")


stat(words)
