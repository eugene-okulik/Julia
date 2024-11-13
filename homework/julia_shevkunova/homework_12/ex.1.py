
class Flowers:
    def __init__(self, price, time_of_life, freshness, color):
        self.price = price
        self.time_of_life = time_of_life
        self.freshness = freshness
        self.color = color

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
total_lifetime = early_rose.time_of_life + late_rose.time_of_life + early_lotus.time_of_life + late_lotus.time_of_life
number_of_list_of_flowers = len(list_of_flowers)

class CollectBouquet:
    def __init(self, list_flowers):
        self.list_flowers = list_flowers

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
        sort_list = [17, 15, 16, 11]
        sort_list.sort()
        return sort_list

    @staticmethod
    def sort_by_freshness():
        sort_list = [10, 4, 5, 6]
        sort_list.sort()
        return sort_list

    @staticmethod
    def sort_by_color():
        sort_list = ['white', 'yellow', 'red']
        return sorted(sort_list)

    @staticmethod
    def search_average_lifetime():
        lifetime = [(early_rose.time_of_life + late_rose.time_of_life +
                     early_lotus.time_of_life + late_lotus.time_of_life)]
        average = sum(lifetime) / len(lifetime)
        return average
