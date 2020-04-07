import io
import numpy

load_iter = io.open('food2.csv')
lines = []
isFood = []

for line in load_iter:
    cells = line.split(';')
    lines += [cells[0]]
    isFood += [cells[1]]

main_iter = numpy.random.permutation(len(lines))

print("Игра \"Съедобное-несъедобное\".")
print("Вам будут по очереди выводится названия предметов.")
print("Вводите 0 если предмет несъедобный и 1 - если несъедобный.")
print("Для начала нажмите Enter.")

input()
score = 0

for num in main_iter:
    print(lines[num])
    inbuf = input()
    if inbuf == isFood[num][0]:
        print("Приавильно!")
        score += 1
    else:
        print("Неправильно!")

print("Вы набрали " + str(score) + " очков.")
print("Конец.")