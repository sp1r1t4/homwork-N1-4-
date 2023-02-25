# окрываем файл
with open('file.txt', 'r') as f:
    lines = f.readlines()

# выводим генератор списка
result = [line[line.find("a"):-1].title() for line in lines if line.find('a') != -1]
# выводим результат
print(result)


