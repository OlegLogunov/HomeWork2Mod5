class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Мы на {self.numberOfFloors} этаже")

floors = 0
print("Введите номер этажа ")
floors = input(int(floors))

floorsOfHouse = House()
floorsOfHouse.setNewNumberOfFloors(floors)
