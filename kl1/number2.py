class Engine:
    def start(self):
        print("Заведён")

    def stop(self):
        print("Заглушен")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start_engine(self):
        self.engine.start()
    def stop_engine(self):
        self.engine.stop()
car = Car()
car.start_engine()  
car.stop_engine()  