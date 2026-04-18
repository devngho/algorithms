word = input()
words = []

for i in range(1, len(word)-1):
    left = word[:i]
    for j in range(i+1, len(word)):
        mid = word[i:j]
        right = word[j:]

        words.append(''.join(reversed(left))+''.join(reversed(mid))+''.join(reversed(right)))

print(min(words))
