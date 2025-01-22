class House:
    counter = 0

    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1
        House.quality = 'low'
        self.quality = 'lower'

    def present(self):
        return f'The house at {self.address} has an area of {self.area} and costs {self.price}'