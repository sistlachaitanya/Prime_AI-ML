class Laptop:
    storage_type = "ssd"

    def __init__(self, ram, storage):
        self.storage = storage
        self.ram = ram

    def get_laptop_specs(self):
        return [self.ram, self.storage, self.storage_type]

    @classmethod
    def get_storage_type(cls):
        return cls.storage_type

    @staticmethod
    def cal_discount(price, discount):
        final_price = price - price * discount / 100
        return final_price


l1 = Laptop(16, 256)

print(l1.get_laptop_specs())

print(l1.cal_discount(25000, 10))
