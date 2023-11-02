
class Singleton():
    instance = None
    def __new__(cls):
        if not cls.instance:
            cls.instance =  super().__new__(cls)
            print(cls.instance)
        return cls.instance
    def __init__(cls):
        cls.data= None

if __name__ == '__main__':
    instance1 = Singleton()
    instance2 = Singleton()
    print(instance1)
    print(instance2)
    instance1.data = "Data from instance 1"
    instance2.data = "Data from instance 2"

    print(instance1.data)
    print(instance2.data)

    print(instance2 is instance1)
    #print(instance1.data)