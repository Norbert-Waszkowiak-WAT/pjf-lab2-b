class FoodProduct:
    def __init__(self):
        self.product_type = "FoodProduct"
        self.name = self.get_name()

    def get_name(self):
        return "FoodProduct"

    def get_product_type(self):
        return self.product_type


class Bread(FoodProduct):
    def __init__(self):
        super().__init__()
        self.product_type = "Bread"
        self.name = self.get_name()

    def get_name(self):
        return "Bread"


class MineralWater(FoodProduct):
    def __init__(self):
        super().__init__()
        self.product_type = "MineralWater"
        self.name = self.get_name()

    def get_name(self):
        return "MineralWater"


class PaperProduct:
    def __init__(self):
        self.product_type = "PaperProduct"
        self.name = self.get_name()

    def get_name(self):
        return "PaperProduct"

    def get_product_type(self):
        return self.product_type


class Pen(PaperProduct):
    def __init__(self):
        super().__init__()
        self.product_type = "Pen"
        self.name = self.get_name()

    def get_name(self):
        return "Pen"


class Notebook(PaperProduct):
    def __init__(self):
        super().__init__()
        self.product_type = "Notebook"
        self.name = self.get_name()

    def get_name(self):
        return "Notebook"


class Shop:
    def __init__(self):
        self.food_products = []
        self.paper_products = []

    def sell_food_product(self, name):
        for product in self.food_products:
            if product.name == name:
                self.food_products.remove(product)
                return product
        return None

    def sell_paper_product(self, name):
        for product in self.paper_products:
            if product.name == name:
                self.paper_products.remove(product)
                return product
        return None

    def check_availability(self, name):
        for product in self.food_products + self.paper_products:
            if product.name == name:
                return True
        return False

    def add_to_store(self, product):
        # Rozpoznaj typ produktu po klasie
        if isinstance(product, FoodProduct):
            if product not in self.food_products:
                self.food_products.append(product)
        elif isinstance(product, PaperProduct):
            if product not in self.paper_products:
                self.paper_products.append(product)

    def print_product_list(self):
        # Najpierw produkty papiernicze, potem spożywcze, zgodnie z testem
        names = [p.name for p in self.paper_products] + [f.name for f in self.food_products]
        print('\n'.join(names))


class Supplier:
    def __init__(self, shop):
        self.shop = shop

    def deliver_product(self, product):
        self.shop.add_to_store(product)



