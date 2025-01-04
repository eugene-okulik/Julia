class Flowers:
    def __init__(self, price, time_of_life, freshness, color):
        self.price = price
        self.time_of_life = time_of_life
        self.freshness = freshness
        self.color = color

    def __repr__(self):
        return (f"{self.__class__.__name__}(price={self.price}, freshness={self.freshness}, color='{self.color}, "
                f"time_of_life='{self.time_of_life}')")


class Rose(Flowers):
    def __init__(self, price, time_of_life, freshness, color):
        super().__init__(price, time_of_life, freshness, color)


early_rose = Rose(15, 5, freshness=1, color='white')
late_rose = Rose(16, 10, freshness=2, color='red')


class Lotus(Flowers):
    def __init__(self, price, time_of_life, freshness, color):
        super().__init__(price, time_of_life, freshness, color)


early_lotus = Lotus(11, 5, freshness=4, color='white')
late_lotus = Lotus(17, 7, freshness=5, color='yellow')

list_of_flowers = [early_rose, late_rose, early_lotus, late_lotus]


class Bouquet:
    def __init__(self):
        self.list_flowers = []

    def bouquet_price(self):
        prices_sum = 0
        for flower in self.list_flowers:
            prices_sum += flower.price
        return prices_sum

    @staticmethod
    def time_of_fading():
        time_fading = total_lifetime / number_of_list_of_flowers
        return time_fading

    @staticmethod
    def sort_by_price():
        sorted_list = sorted(list_of_flowers, key=lambda flower: flower.price)
        return sorted_list

    @staticmethod
    def sort_by_freshness():
        sorted_list = sorted(list_of_flowers, key=lambda flower: flower.freshness)
        return sorted_list

    @staticmethod
    def sort_by_color():
        sorted_list = sorted(list_of_flowers, key=lambda flower: flower.color)
        return sorted_list

    @staticmethod
    def search_by_lifetime(lifetime):
        flowers = list(sorted(list_of_flowers, key=lambda flower: flower.time_of_life == lifetime))
        return flowers


number_of_list_of_flowers = len(list_of_flowers)
total_lifetime = early_rose.time_of_life + late_rose.time_of_life + early_lotus.time_of_life + late_lotus.time_of_life

print(Bouquet.sort_by_color())
print(Bouquet.sort_by_price())
print(Bouquet.sort_by_freshness())
print(Bouquet.time_of_fading())
print(Bouquet.search_by_lifetime(5))



