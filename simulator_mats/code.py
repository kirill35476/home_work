from random import randint
#код

user_pass = 123
admin_pass = 123
user_login = 'admin'
admin_login = 'admin'
if user_pass == admin_pass and user_login == admin_login:
    print('Доступ получен')
else:
    print('доступ запрещен')

# операция или

dice = randint(1, 6)
survived = dice == 1 or dice == 5
survived

# операция не

age = int(input('Введите свой возраст'))
adult = age >= 18
lives = 2
if not adult:
    lives = 30

# тренажер для Марьиванны

student = input('представтесь,пожалуйста:')
level = int(input('Выберете уровень сложности 1-5:'))
if level < 1 or level > 5:
    level = 1
    print('установлен первый уровень сложности.')
print(f'Хорошо,{student}.Тебе задачка')

min = 1**(level - 1)
max = 10**(level - 1)

a = randint(min, max)
b = randint(min, max)

print(f'{student},сколько будет {a} + {b}?', end='')

correct_answer = a + b
student_answer = input()
print(type(correct_answer), type(student_answer))

if student_answer == str(correct_answer):
    print(f'Ах, ну какой умница,{student}.')
else:
    print(f'Два, {student},можешь садтьбся! Правельны ответ {correct_answer}')
