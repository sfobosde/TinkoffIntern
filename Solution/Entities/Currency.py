# Интерфейс для отношений валют.
class ICurrency:
    sender: object
    handler: object

    def calc_currency_amount(self):
        pass


class Currency(ICurrency):
    cost: int

    def __init__(self, cost):
        self.cost = cost
        self.sender: ICurrency = None
        self.handler: ICurrency = None

    def determine_handlers(self, handler: ICurrency):
        self.handler = handler
        handler.sender = self

    def has_handler(self):
        return True if self.handler else False

    def get_total_convert(self, amount):
        return amount // self.cost

    def calc_remainder_options(self, sum_amount):
        options = []

        max_currency_amount = self.get_total_convert(sum_amount)

        while max_currency_amount > 0:
            options.append((max_currency_amount, sum_amount - max_currency_amount * self.cost))
            max_currency_amount -= 1



a = Currency(1)
b = Currency(2)
c = Currency(3)

a.determine_handlers(b)
b.determine_handlers(c)

print(a.is_sender())
print(b.is_sender())
print(c.is_sender())
