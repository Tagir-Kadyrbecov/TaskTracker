import json
from logging import raiseExceptions

"""Импортирую энумсы"""
from enums import Status
"""по идее я мог бы и тут сервис написать но я хотел по солиду сделать, но получилось как получилось)"""
from service import Service
"""к сожалению я не сделал валидацию поверки на дуьликат ключа при создании записи"""
service = Service()
expense_tracker_list = []
while True:
    """если что это строка нужна чтобы читать jsonчики и работы с ним как с объектом """
    with open("data.json", "r") as read_file:
        expense_tracker_list = json.load(read_file)
    print("1.добавить расходы")
    print("2.обновлять информацию")
    print("3.удалить расходы")
    print("4.просмотреть все расходы")
    choice = int(input("Введите номер меню: "))
    match choice:
        case 1:
            id_menu = int(input("Введите айди записи: "))
            name_menu = str(input("Введите имя записи: "))
            description_menu = str(input("Введите описание записи: "))
            print("1.todo")
            print("2.in-progress")
            print("3.done")
            status_choice = int(input("Введите status записи: "))
            match status_choice:
                case 1:
                    status_menu = Status.TODO.value
                case 2:
                    status_menu = Status.IN_PROGRESS.value
                case 3:
                    status_menu = Status.DONE.value
            save_data = service.create_expense(id_menu, name_menu, description_menu, status_menu)
            expense_tracker_list.append(save_data)
            with open("data.json", "w") as file:
                json.dump(expense_tracker_list, file)
        case 2:
            choice_id = int(input("Введите id записи: "))
            for expense in expense_tracker_list:
                if expense["id"] == choice_id:
                    print("Такая запись найдена")
                    print("1.name: ")
                    print("2.description: ")
                    print("3.status: ")
                    update_choice = int(input("Введите номер меню что хотите изменить: "))
                    match update_choice:
                        case 1:
                            update_name = str(input("Введите name записи: "))
                            expense["name"] = update_name
                        case 2:
                            update_description = str(input("Введите description записи: "))
                            expense["description"] = update_description
                        case 3:
                            print("1.Todo")
                            print("2.In-progress")
                            print("3.Done")
                            status_choice = int(input("Введите status записи: "))
                            match status_choice:
                                case 1:
                                    status_menu = Status.TODO.value
                                case 2:
                                    status_menu = Status.IN_PROGRESS.value
                                case 3:
                                    status_menu = Status.DONE.value
                            expense["status"] = status_menu
                    with open("data.json", "w") as file:
                        json.dump(expense_tracker_list, file)
        case 3:
            choice_id = int(input("Введите id записи: "))
            for expense in expense_tracker_list:
                if expense["id"] == choice_id:
                    print("Такая запись найдена и успешно удалена")
                    expense_tracker_list.remove(expense)
                    with open("data.json", "w") as file:
                        json.dump(expense_tracker_list, file)
                else:
                    print("Такой записи нет")
        case 4:
            with open("data.json", "r", ) as file:
                data_check = json.load(file)
                print(data_check)
