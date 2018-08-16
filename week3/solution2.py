import csv
import os

class BaseCar:

    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        path_parts = os.path.splitext(self.photo_file_name)
        return path_parts[-1]


class Car(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        if len(body_whl) > 0:
            self.body_width, self.body_height, self.body_length = list(map(lambda x: float(x), body_whl.split('x')))
        else:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                try:
                    if len(row) > 0 and row[0] in ['car', 'truck', 'spec_machine']:
                        car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row

                        car = None
                        if car_type == 'car':
                            car = Car(brand, photo_file_name, carrying, passenger_seats_count)
                        elif car_type == 'truck':
                            car = Truck(brand, photo_file_name, carrying, body_whl)
                        elif car_type == 'spec_machine':
                            car = SpecMachine(brand, photo_file_name, carrying, extra)
                        else:
                            continue

                        car_list.append(car)
                    else:
                        continue
                except BaseException as err:
                    continue
    except BaseException as err:
        return []

    return car_list