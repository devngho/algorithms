def solve(x):
    chars = []
    texts = []

    for txt in x:
        words = txt.split()
        found = False
        for i, w in enumerate(words):
            if w[0].lower() not in chars:
                found = True
                chars.append(w[0].lower())
                texts.append((' '.join(words[:i]) + ' [' + w[0] + ']' + w[1:] + ' ' + ' '.join(words[(i + 1):])).strip())
                break

        if found:
            continue

        chars2 = list(txt)
        for i, w in enumerate(chars2):
            if w.lower() not in chars and w != ' ':
                found = True
                chars.append(w.lower())
                texts.append(''.join(chars2[:i]) + '[' + w + ']' + ''.join(chars2[(i + 1):]))
                break

        if found:
            continue

        texts.append(txt)

    return '\n'.join(texts)


inp = int(input())
inp = [input() for _ in range(inp)]
res = solve(inp)
print(res)
