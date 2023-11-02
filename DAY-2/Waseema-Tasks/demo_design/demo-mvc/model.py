class Model:

    def __init__(self):
        self._data = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

#ob = Model()
#ob.set_data("Wasee")
#print(ob.get_data())