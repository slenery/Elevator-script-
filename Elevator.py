class Elevator:
    def __init__(self, current = 1, max = None, min = None):
        self.current = int(current)
        self.max = int(max)
        self.min = int(min)
        
        
        #ФУНКЦИИ КЛАССА
        
        
    def go_up(self):                                   #ВВЕРХ
        if self.current >= self.max:    
            print("Подняться выше нельзя")
            return
        self.current += 1
        if self.current == 0:   
                self.current = 1  
        print(f"Вы на {self.current} этаже")
    def go_down(self):                                #ВНИЗ
        if self.current == self.min:
            print("Ниже нельзя")
            return
        self.current -= 1
        if self.current == 0:
            self.current = -1
        print(f"Вы на {self.current} этаже")
    def call_to_floor(self):                           #ВЫЗВАТЬ НА ЭТАЖ
        while True:
            try: 
                target_floor = int(input("Введите этаж, на который должен приехать лифт: ").strip())
                if not target_floor:
                    print("Лифт ждёт вашей команды")
                    continue
                if target_floor > int(self.max):
                    print(f"Лифт не может ехать выше {self.max} этажа")
                    continue
                if target_floor < self.min:
                    print(f"Лифт не может ехать ниже {self.min} этажа")
                    continue
                self.current = target_floor
                print(f"Лифт приехал на {target_floor} этаж")
                break
            except ValueError:
                print("Можно вводить только числа")
                continue       
    def elevator_settings(self):                          #НАСТРОЙКА ЛИФТА
        accept_chars = "0123456789"
        print("Максимум этажей - 200, минимум - -200, 0 за этаж не считается")
        while True:
            max = input("Введите максимум этажей").strip()
            if not max:
                print("Поле должно быть заполненно")
                continue
            if not any(char in max for char in accept_chars):
                print("Вводить можно только целые числа")
            if int(max) > 200:
                print("Максимальное количество этажей не может быть больше 200")
                continue
            if int(max) < 2:
                print("Минимальное количество этажей: 2")
                continue
            self.max = int(max)
            print(f"Теперь всего {self.max} этажей")
            break
        while True:
            min = int(input("Введите минимум этажей: ").strip())
            if not min:
                print("Поле должно быть заполненно")
                continue
            if not any(char in str(min) for char in accept_chars):
                print("Вводить можно только целые числа")
            if int(min) < -200:
                print("Минимальное количество этажей не может быть меньше 200")
                continue
            if int(min) > -1:
                print("Максимально количество этажей - 1, пропуская 0. ")
                continue
            self.min = int(min)
            print(f"Теперь всего {self.min} этажей вниз")
            break
        while True:
            current = input("Введите, на каком этаже вы бы хотели начать, либо нажмите enter и применится значение по умолчанию(1): ").strip()
            if not current:
                break
            if not any(char in current for char in accept_chars):
                print("Вводить можно только целые числа")
            if int(current) > int(self.max) or int(current) < int(self.min):
                print(f"Значение может быть меньше {self.max} и больше {self.min}")
                continue
            self.current = int(current)
            print(f'Вы начинаете на {current} этаже')
            return      
    def el_info(self):
        print(f"Максимальный этаж: {self.max}, минимальный: {self.min}, вы находитесь на {self.current}")
        
        
        
        #ГЛАВНАЯ ФУНКЦИЯ РАБОТЫ
def work():
    el1 = Elevator(1, 10, -1)
    while True:
        user = input("Нажмите 'u' чтобы ехать вверх, 'd' вниз, указать этаж: 'e', информация о лифте: 'i', настроить лифт 's' для остановки скрипта: 'q': " ).strip().lower()
        accept_chars = "uidseq"
        if not user:
            print("Лифт ожидает команды")
            continue
        if not any(char in user for char in accept_chars):
            print("У лифта нет такой кнопки")
            continue
        if len(user) > 1:
            print("Не нажимайте несколько кнопок")
            continue
        if user == "q":
            break
        if user == "u":
            el1.go_up()
        if user == "d":
            el1.go_down()
        if user == "e":
            el1.call_to_floor()
        if user == "i":
            el1.el_info()
        if user == "s":
            el1.elevator_settings()       
            
            
            
            ##### САМ КОД #####
work()
