# Проект FitLife - MVP версия 1.0
print('Здравствуйте!')
print('Я бот который:')
print('- поможет вам рассчитать Ваш индекс массы тела (ИМТ);')
print('- даст рекомендацию по потреблению воды.')
print('Давайте познакомимся!')

ZERO = 0
RECOMEMD_L_ON_KG = 30
ML_IN_L = 1000

while True:
    user_name = input('Как вас зовут? ')
    if not user_name:
        print('Ошибка: вы не ввели имя.')
        continue
    else:
        user_name = user_name.capitalize()
        break

while True:
    try:
        user_age = input('Сколько вам полных лет? ')
        if not user_age:
            print('Ошибка: вы не ввели возраст.')
            continue
        user_age = int(user_age)
        if user_age <= ZERO:
            print('Ошибка: возраст не может быть отрицательным или равен 0.')
            continue
        else:
            break
    except ValueError:
        print('Ошибка: возраст должен быть целым числом')

while True:
    try:
        weight = input('Какой у вас вес? (в кг.) ')
        if not weight:
            print('Ошибка: вы не ввели вес.')
            continue
        weight = float(weight)
        if weight <= ZERO:
            print('Ошибка: вес не может быть отрицательным или равен 0.')
            continue
        else:
            break
    except ValueError:
        print('Ошибка: вес должен быть числом')

while True:
    try:
        height = input('Какой у вас рост? (в м.) ')
        if not height:
            print('Ошибка: вы не ввели рост.')
            continue
        height = float(height)
        if height <= ZERO:
            print('Ошибка: рост не может быть отрицательным или равен 0.')
            continue
        else:
            break
    except ValueError:
        print('Ошибка: рост должен быть числом')

bmi = weight / (height ** 2)
water_ml = weight * RECOMEMD_L_ON_KG
water_l = water_ml / ML_IN_L

print(f'{user_name}, вам {user_age}.')
print(f'Ваш ИМТ равен: {round(bmi, 1)}.')
print(f'Рекомендованное количество воды в день: {round(water_l, 2)} литров.')
print('\nРасчёт окончен. Будьте здоровы!')
