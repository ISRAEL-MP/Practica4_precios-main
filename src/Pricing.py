class Pricing:
    def calculate(self, price, tax=0, discount=0):
        return round((price - discount) * (1+tax),2)