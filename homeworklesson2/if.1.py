

def user_stage(age):
    if  0 < age < 3:
        return ' '
    if 3 <= age < 6:
        return 'Ходит в детский сад'
    elif 6 <= age < 17:
        return 'Ходит в школу'
    elif 17 <= age <= 23:
        return 'Учиться в Вузе'
    else:
        return 'Работает'
age = int(input('Your age: '))
print(user_stage(age))