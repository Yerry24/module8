def all_variants(text):
    for j in range(0, 3):
        yield text[j]
    for k in range(0, 2):
        yield text[k] + text[k+1]
    for l in range(0, 1):
        yield text

a = all_variants("abc")
for i in a:
    print(i)