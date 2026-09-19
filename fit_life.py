# Проект FitLife - MVP версия 1.0
print('Здравствуйте!')
print('Я бот который:')
print('- поможет вам рассчитать Ваш индекс массы тела (ИМТ);')
print('- даст рекомендацию по потреблению воды.')
print('Давайте познакомимся!')

user_name = input('Как вас зовут? ')
user_name = user_name.capitalize()
user_age = input('Сколько вам полных лет? ')
int_user_age = int(user_age)

weight = input('Какой у вас вес? (в кг.) ')
height = input('Какой у вас рост? (в м.) ')

float_weight = float(weight)
float_height = float(height)

bmi = float_weight / (float_height ** 2)
water_ml = float_weight * 30
water_l = water_ml / 1000

print(f'{user_name} , вам {int_user_age}.')
print(f'Ваш ИМТ равен: {round(bmi, 1)}.')
print(f'Рекомендованное количество воды в день: {round(water_l, 2)} литров.')
print('\nРасчёт окончен. Будьте здоровы!')
