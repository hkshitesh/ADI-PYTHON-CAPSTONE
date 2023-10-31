
class ProductA:

    def action(self):
        return "Action from Product A"

class ProductB:

    def action(self):
        return  "Action from Product B"


class ProductFactory:
    def create_product(self,product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
        else:
            raise ValueError("invalid object asked")

product_factory = ProductFactory()

ob = product_factory.create_product("A")
print(ob.action())

ob2 = product_factory.create_product("B")
print(ob2.action())