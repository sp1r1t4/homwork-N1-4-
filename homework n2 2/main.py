# входные данные
s =  "Я люблю кушать (при этом в данный момент я не хотел кушать) и я пошел кушать."
# с помощью первого слайса вырезаем все, что находится до скобки, склеиваем это со вторым слайсом, где мы отрезали значение после скобки и добавили +2 для того что бы не было разрыва
print(s[0:s.find("(")] + s[s.find(")")+2:])