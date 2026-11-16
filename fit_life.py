# Проект FitLife - MVP версия 1.0
print('Здравствуйте!')
print('Я бот который:')
print('- поможет вам рассчитать Ваш индекс массы тела (ИМТ);')
print('- даст рекомендацию по потреблению воды.')
print('Давайте познакомимся!')

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
        if user_age < 0:
            print('Ошибка: возраст не может быть отрицательным.')
            continue
        elif user_age == 0:
            print('Ошибка: возраст не может быть равен 0.')
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
        if weight < 0:
            print('Ошибка: вес не может быть отрицательным.')
            continue
        elif weight == 0:
            print('Ошибка: вес не может быть равен 0.')
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
        if height < 0:
            print('Ошибка: рост не может быть отрицательным.')
            continue
        elif height == 0:
            print('Ошибка: рост не может быть равен 0.')
            continue
        else:
            break
    except ValueError:
        print('Ошибка: рост должен быть числом')


Recomend_l_on_kg = 30
Ml_in_l = 1000

bmi = weight / (height ** 2)
water_ml = weight * Recomend_l_on_kg
water_l = water_ml / Ml_in_l

print(f'{user_name}, вам {user_age}.')
print(f'Ваш ИМТ равен: {round(bmi, 1)}.')
print(f'Рекомендованное количество воды в день: {round(water_l, 2)} литров.')
print('\nРасчёт окончен. Будьте здоровы!')
