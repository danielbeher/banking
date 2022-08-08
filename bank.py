from datetime import datetime, date, time


class A:
    def __init__(self,pin, balans):
        self.pin = pin
        self.balans = balans
        self.i = 0
        self.sproba = 3
        print(f'Пін-{pin} Баналс-{balans}')
        self.func_for_record()

    def func_for_record(self):
        with open('money.txt', 'w') as file:
            file.write(str(self.balans))
        with open('pin.txt', 'w') as file:
            file.write(str(self.pin))
        self.func_for_login(self.sproba)

    def func_for_login(self,pin):
        file = open('data.txt', 'r+')
        file.truncate(0)
        pin_vhid = int(input('pin vhid: '))
        if self.pin == pin_vhid:
            self.func_for_removal()
        elif self.i == 2:
            print('Ви використали всі спроби!')
        else:
            self.sproba = self.sproba -1
            print(f'пароль не правильний у вас {self.sproba} спроби')
            self.i = self.i + 1
            self.func_for_login(self)

class B(A):
    def __init__(self,pin, balans):
        A.__init__(self,pin, balans)
    def func_for_removal(self):
        print('---------------------------------')
        with open('money.txt') as file:
            for what_money in file:
                what_money = int(what_money)
        print(f'Баланс {what_money}')
        removal = int(input('Ліміт зняття 500 грн\nСкільки бажаєте вивести? '))
        if removal >= 500:
            print('Ви не можете перевищувати ліміт!')
            self.func_for_removal()

        else:
            what_money = what_money - removal
            data = datetime.now()
            if what_money < 0:
                print('Недостаньо коштів!')
                self.func_for_removal()
            with open('money.txt', 'w') as file:
                file.write(str(f'{what_money}'))
            with open('data.txt', 'a') as file:
                file.write(str(f'{data}\n'))
            print(f'Ви вивели {removal} грн ({data})')
            ex_con = int(input('Continue - 1\nExit - 2\n'))
            if ex_con == 2:
                print('Вихід')
            elif ex_con == 1:
                self.func_for_removal()


object = B(1111, 800)
