class BankAccount:
    def __init__(self, name, bank_balence):
        self.name = name
        self.__bank_balence = bank_balence

    def get_bank_balence(self):
        return self.__bank_balence

    def set_bank_balence(self, new_balence):
        self.__bank_balence = new_balence

 
b1 = BankAccount("Rama", 40_000)


print(b1._BankAccount__bank_balence)
