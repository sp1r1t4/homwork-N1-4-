def generator(s:str):
    for word in s.split():
        yield word

for word in generator('Hello World!'):
    print(word)






