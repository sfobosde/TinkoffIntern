# Интерфейс для отношений валют.
class ICurrency:
    sender: object
    handler: object

    def calc_currency_amount(self):
        pass

    def check_options(self, options: list):
        pass

    def calc_remainder_options(self, sum_amount: int):
        pass


class Currency(ICurrency):
    cost: int

    def __init__(self, cost):
        self.cost = cost
        self.sender = None
        self.handler = None

    def determine_handlers(self, handler: ICurrency):
        self.handler = handler
        handler.sender = self

    def has_handler(self):
        return True if self.handler else False

    def get_total_convert(self, amount):
        return amount // self.cost

    def calc_remainder_options(self, sum_amount: int):
        options = []
        amount = 0

        max_currency_amount = self.get_total_convert(sum_amount)

        options.append((max_currency_amount, sum_amount - max_currency_amount * self.cost))
        max_currency_amount -= 1

        while max_currency_amount > 0:
            options.append((max_currency_amount, sum_amount - max_currency_amount * self.cost))
            max_currency_amount -= 1

        amount += self.check_options(options)
        return amount

    def check_options(self, options: list):
        option_amount = 0

        if self.has_handler():
            for option in options:
                option_amount += self.handler.calc_remainder_options(option[1])
        else:
            for option in options:
                if option[1] % self.cost == 0:
                    option_amount += 1
        return option_amount


a = Currency(1)
b = Currency(2)
c = Currency(3)

opt = {}

a.determine_handlers(b)
b.determine_handlers(c)

print(a.calc_remainder_options(25))
