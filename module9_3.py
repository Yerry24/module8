first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = []
for nf, ns in zip(first, second):
    if len(nf) == len(ns):
        continue
    else:
        first_result.append (len(nf)-len(ns))

second_result = []
for i in range(len(first)):
    second_result.append(len(first[i]) == len(second[i]))

print(list(first_result))
print(list(second_result))