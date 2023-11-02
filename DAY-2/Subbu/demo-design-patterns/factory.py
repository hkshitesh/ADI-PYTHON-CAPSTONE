class ProductA:
    def action(self):
        return "Action from ProductA"

class ProductB:
    def action(self):
        return "Action from ProductB"

class ProductFactory:
    def create_product(self, product_type):
        if product_type == 'A':
            return ProductA()
        elif product_type == 'B':
            return ProductB()
        else:
            raise ValueError("Invalid Object Requested")

product_factory = ProductFactory()
ob = product_factory.create_product('A')
print(ob.action())
