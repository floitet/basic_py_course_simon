# Task 6.4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car has started moving.')

    def stop(self):
        print('The car has stopped.')

    def turn(self, direction):
        print(f'Tha car has turned in {direction} direction.')

    def show_speed(self):
        print(f'You are driving at {self.speed} km/h.')


parent_car = Car(60, 'red', 'Renault Logan', False)
print(parent_car.color)
print(parent_car.name)
print(parent_car.is_police)
print(parent_car.speed)
parent_car.go()
parent_car.show_speed()
parent_car.turn('left')
parent_car.stop()



class TownCar(Car):
    def __init__(self, speed, color, name, body_type, fuel_flow, is_police):
        super().__init__(speed, color, name, is_police)
        self.body_type = body_type
        self.fuel_flow = fuel_flow

    def show_speed(self):
        print(f'You are driving at {self.speed} km/h.')
        if self.speed > 60:
            print('You are speeding. Please, slow down.')


random_town_car = TownCar(70, 'blue', 'Toyota Corolla', 'hatchback', '7-10 l/100km', False)
print(random_town_car.name)
print(random_town_car.color)
print(random_town_car.fuel_flow)
print(random_town_car.body_type)
print(random_town_car.is_police)
random_town_car.go()
random_town_car.show_speed()
random_town_car.stop()

class SportCar(Car):
    def __init__(self, speed, color, name, engine_power, max_speed, is_police):
        super().__init__(speed, color, name, is_police)
        self.engine_power = engine_power
        self.max_speed = max_speed

cool_sp_car = SportCar(350, 'red', 'Ferrari', '450 hp', '600 km/h', False)

print(cool_sp_car.name)
print(cool_sp_car.color)
print(cool_sp_car.engine_power)
print(cool_sp_car.max_speed)
print(cool_sp_car.is_police)
cool_sp_car.go()
cool_sp_car.show_speed()
cool_sp_car.stop()


class WorkCar(Car):
    def __init__(self, speed, color, name, lift_capacity, passability, is_police):
        super().__init__(speed, color, name, is_police)
        self.lift_capacity = lift_capacity
        self.passability = passability

    def show_speed(self):
        print(f'You are driving at {self.speed} km/h.')
        if self.speed > 40:
            print('You are speeding. Please, slow down.')

dump_truck = WorkCar(55, 'dirt', 'Dirty Lifter', '25000 kg', 'high', False)
print(dump_truck.passability)
print(dump_truck.lift_capacity)
dump_truck.show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, patrol_district, armory):
        super().__init__(speed, color, name, is_police)
        self.patrol_disctrict = patrol_district
        self.armory = armory

dist_45_car = PoliceCar(100, 'blue', 'Ford', True, 45, 'heavy')
dist_45_car.go()
dist_45_car.turn('to South')
