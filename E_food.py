import io
main_iter = io.open('food.csv')
print("Игра \"Съедобное - несъедобное\".")
print("Вам будут по очереди выводиться названия предметов.")
print("Вводите 0 если предмет не съедобный и 1 - если съедобный.")
print("Для начала нажмите Enter.")
input()
score = 0
for line in main_iter:
    cells = line.split(';')
    print(cells[0])
    inbuf = input()
    if inbuf == cells[1][0]:
        print ("Правильно!")
        score += 1
    else:
        print("Неправильно!")
print("Вы набрали " + str(score) + " очков")
print("Конец.")