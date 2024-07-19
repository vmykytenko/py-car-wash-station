class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

   def calculate_washing_price(self, car: Car) -> float:
        cost_for_a_single_car = round(
            (
                car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center
            ), 1
        )
        return cost_for_a_single_car

