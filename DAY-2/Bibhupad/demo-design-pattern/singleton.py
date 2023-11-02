class  Singleton():
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(cls):
        cls.data = None

if __name__ == "__main__":
    instance1 = Singleton()
    instacne2 = Singleton()
    instance1.data = "data from instance 1"
    instacne2.data = "data from instance 2"

    print(instance1)
    print(instacne2)

    print(instance1.data)
    print(instacne2.data)

    print(instacne2 is instance1)