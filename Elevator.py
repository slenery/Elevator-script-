class Elevator:
    def __init__(self, current = 1, max = None, min = None):
        self.current = int(current)
        self.max = int(max)
        self.min = int(min)
    def go_up(self):
        if self.current == self.max:
            print("Подняться выше нельзя")
            return
        else:
            self.current += 1
            print(f"Вы на {self.current} этаже")

    def go_down(self):
        if self.current == self.min:
            print("Ниже нельзя")
            return
        self.current -=1
        print(f"Вы на {self.current} этаже")
    def call_to_floor(self):
        while True:
            try: 
                target_floor = int(input("Введите этаж, на который должен приехать лифт"))
                if target_floor > self.max or target_floor < self.min:
                    print(f"Лифт не может ехать выше {self.max} этажа, и ниже {self.min}")
                    continue
                self.current = target_floor
                print(f"Лифт приехал на {target_floor} этаж")
                break
            except ValueError:
                print("Можно вводить только числа")
                continue
el1 = Elevator(1, 10, -1)
el1.go_up()
el1.go_up()
el1.go_up()
el1.go_down()
el1.call_to_floor()
el1.go_down()