class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Preschooler(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def get_average_income(self):
        return "У дошкольников нет среднего дохода"

    def get_average_expenses(self):
        return "У дошкольников нет среднего расхода"


class Schoolkid(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def get_average_income(self):
        return "У школьников нет среднего дохода"

    def get_average_expenses(self):
        return "У школьников нет среднего расхода"


class Student(Person):
    def __init__(self, name, age, gender, scholarship):
        super().__init__(name, age, gender)
        self.scholarship = scholarship

    def get_average_income(self):
        return f"Средний доход студента: {self.scholarship}"

    def get_average_expenses(self):
        return "Расходы студента зависят от его личных предпочтений"


class Worker(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def get_average_income(self):
        return f"Средний доход работающего: {self.salary}"

    def get_average_expenses(self):
        return "Расходы работающего зависят от его личных потребностей"


# Демонстрация работы классов
while True:
    print("Выберите тип человека:")
    print("1. Дошкольник")
    print("2. Школьник")
    print("3. Студент")
    print("4. Работающий")
    print("0. Выход")

    choice = input("Введите номер: ")

    if choice == "1":
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        gender = input("Введите пол: ")
        preschooler = Preschooler(name, age, gender)
        print("Средний доход:", preschooler.get_average_income())
        print("Средние расходы:", preschooler.get_average_expenses())
    elif choice == "2":
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        gender = input("Введите пол: ")
        schoolkid = Schoolkid(name, age, gender)
        print("Средний доход:", schoolkid.get_average_income())
        print("Средние расходы:", schoolkid.get_average_expenses())
    elif choice == "3":
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        gender = input("Введите пол: ")
        scholarship = input("Введите размер стипендии: ")
        student = Student(name, age, gender, scholarship)
        print("Средний доход:", student.get_average_income())
        print("Средние расходы:", student.get_average_expenses())
    elif choice == "4":
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        gender = input("Введите пол: ")
        salary = input("Введите размер зарплаты: ")
        worker = Worker(name, age, gender, salary)
        print("Средний доход:", worker.get_average_income())
        print("Средние расходы:", worker.get_average_expenses())
    elif choice == "0":
        break
    else:
        print("Неверный выбор")