from apps.various.models import Car

from typing import List


def get_all_cars() -> List[Car]:
    cars: List[Car] = Car.objects.all()

    return cars

def get_car_byId(id) -> Car:
    car: Car = Car.objects.get(id=id)

    return car


def create_Car(data) -> Car:
    newCar: Car = Car.objects.create(name=data['name'], model=data['model'])

    return newCar; 


def delete_Car(id) -> Car:
    pass


def change_Car(id) -> Car:
    pass
