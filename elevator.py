import random

queue_lst = []


class Building():
    """Class for building"""
    passenger_lst = []
    num_of_floors = 0
    elevator = 0

    def __init__(self, floors, passengers):
        self.num_of_floors = floors
        global queue_lst

        for _id in range(1, passengers + 1):
            new_passenger = Elevator_passenger(_id, self.num_of_floors)
            self.passenger_lst.append(new_passenger)

        queue_lst = self.passenger_lst
        self.elevator = Elevator(floors)
        self.run()

    def run(self):
        passenger_nums = len(self.passenger_lst)
        while self.elevator.passenger_reached != passenger_nums:
            self.elevator.move()


class Elevator:
    """class for Elevator"""
    door_opened = True
    totalFloorNum = 0
    direction = 1
    stop_flr = 1
    passenger_reached = 0
    max_floor = 0

    def __init__(self, totalFloorNum):
        self.totalFloorNum = totalFloorNum
        self.register_list = []

    def move(self):
        global queue_lst

        if self.stop_flr == self.totalFloorNum:
            self.direction = -1
        if self.stop_flr == 1:
            self.direction = 1

        print("\t\tЭтаж:", self.stop_flr)

        for passenger in self.register_list:
            if passenger.end_floor == self.stop_flr:
                self.remove_passenger(passenger)

        for passenger in queue_lst:
            if passenger.start_floor == self.stop_flr:
                self.register_passenger(passenger)

        self.get_max_floor()
        if self.max_floor < self.stop_flr:
            self.direction = -1
        else:
            self.direction = 1

        if self.direction == 1:
            self.stop_flr = self.stop_flr + 1
        else:
            self.stop_flr = self.stop_flr - 1
        self.output()

    def output(self):
        if self.door_opened:
            print('\t\tДвери закрываются')
            self.door_opened = False
        if self.direction == 1:
            print("\t\t Направление движения: вверх_1")
        else:
            print('\t\t Направление движения: вниз_1')
        print("\n\t\t___________________")

    def register_passenger(self, passenger):
        global queue_lst
        self.register_list.append(passenger)
        queue_lst.remove(passenger)

        if not self.door_opened:
            print("\t\tДвери открываются")
            self.door_opened = True
        print("\t\tПассажир лифта с id = ",
              passenger.id,
              "вошел в лифт")


    def remove_passenger(self, passenger):
        global queue_lst
        passenger.finished = True
        self.register_list.remove(passenger)
        self.passenger_reached = self.passenger_reached + 1


        if not self.door_opened:
            print("\t\tДвери открываются")
            self.door_opened = True
        print("\t\tПассажир лифта с id = ",
              passenger.id,
              "вышел из лифта")

    def get_max_floor(self):
        self.max_floor = 0
        global queue_lst
        for passenger in self.register_list:
            if passenger.end_floor > self.max_floor:
                self.max_floor = passenger.end_floor
        for passenger in queue_lst:
            if passenger.start_floor > self.max_floor:
                self.max_floor = passenger.start_floor


class Elevator_passenger:
    """Class for passenger of elevator"""
    id = 0
    start_floor = 1
    end_floor = 1
    finished = False

    def __init__(self, id, number_of_floor):
        self.id = id
        for i in range(len(str(number_of_floor))):
            self.start_floor = random.randint(i, number_of_floor)
        self.end_floor = random.randint(1, number_of_floor)
        while self.end_floor == self.start_floor:
            self.end_floor = random.randint(1, number_of_floor)
        print(
            "Пассажир лифта с id = ",
            self.id,
            "\tНачальный этаж: ",
            self.start_floor,
            "\t Конечный этаж: ",
            self.end_floor,
        )






