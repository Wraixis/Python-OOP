class Employee:
    standart_number_of_vacation = 28

    def __init__(self, first_name, last_name, position, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.experience = experience

    def calculate_vacation(self):
        add_days = 0
        if self.position == 'преподаватель':
            add_days += 15
        elif self.experience > 10:
            add_days += 2 * (self.experience - 10)

        return Employee.standart_number_of_vacation + add_days

    def info(self):

        vacation_days = self.calculate_vacation()

        print(f'ФИО: {self.first_name} {self.last_name}')
        print(f'ДОЛЖНОСТЬ: {self.position}')
        print(f'СТАЖ РАБОТЫ: {self.experience}')
        print(f'ОТПУСКНЫЕ: {self.standart_number_of_vacation} дней + БОНУС {vacation_days - Employee.standart_number_of_vacation} дня = {vacation_days} дня')

teacher = Employee("Иван", "Иванов", "преподаватель", 10)
designer = Employee("Петр", "Петров", "дизайнер", 15)
accountant = Employee("Сидор", "Сидоров", "бухгалтер", 4)

teacher.info()
designer.info()
accountant.info()