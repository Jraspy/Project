# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_input_info = ("Имя", "Фамилия", "Дата рождения",
                   "Город проживания", "Эл.адрес", "Телефон")


def get_user_data(name: str, surname: str, born_date: str,
                  city: str, email: str, tel: str):
    user_data = {user_input_info[0]: name.title(), user_input_info[1]: surname.title(),
                 user_input_info[2]: born_date, user_input_info[3]: city.title(),
                 user_input_info[4]: email, user_input_info[5]: tel}
    print(f"Данные пользователя: {user_data}")


usr_name = input(f"Введите {user_input_info[0]}: ")
usr_surname = input(f"Введите {user_input_info[1]}: ")
usr_born_date = input(f"Введите {user_input_info[2]}: ")
usr_city = input(f"Введите {user_input_info[3]}: ")
usr_email = input(f"Введите {user_input_info[4]}: ")
usr_tel = input(f"Введите {user_input_info[5]}: ")

get_user_data(name=usr_name, surname=usr_surname, born_date=usr_born_date,
              city=usr_city, email=usr_email, tel=usr_tel)


# Output
# Введите Имя: евгений
# Введите Фамилия: волохОв
# Введите Дата рождения: 01-01-2005
# Введите Город проживания: городБ
# Введите Эл.адрес: фывв@fl.ru
# Введите Телефон: 483583538
# Данные пользователя: {'Имя': 'Евгений', 'Фамилия': 'Волохов', 'Дата рождения': '01-01-2005', 'Город проживания': 'Городб', 'Эл.адрес': 'фывв@fl.ru', 'Телефон': '483583538'}
#
# Process finished with exit code 0