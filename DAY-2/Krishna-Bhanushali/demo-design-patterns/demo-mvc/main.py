from controller import Controller
from model import Model
from view import View

if __name__ == "__main__":
    model = Model()
    view = View()

    controller = Controller(model, view)

    controller.set_data("Hello, MVC Design")
    controller.update_view()

