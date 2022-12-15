import csv
from random import randint
name = input("Введите ваше имя: ")
vopros = ['Как называется птица, которая не умеет летать, но прекрасно плавает?',
    'Какая птица любит стучать по дереву?',
    'Арбуз - это фрукт или ягода?',
    'Как называется спутник Земли?',
    'Это животное называют “царём зверей”',
    'Назовите самую близкую к Земле звезду:'
]
r1 = randint(0, 5)
print(vopros[r1])
vopros1 = input('Ваш ответ - ')
r2 = randint(0, 100)
r3 = randint(0, 100)
a =f"{str(r2)} + {str(r3)}"
vopros2 = int(input(f"{str(r2)} + {str(r3)} = "))
lst = []
lst.extend([name, vopros[r1], vopros1, a, vopros2])

with open('Game.csv', 'a', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(lst)