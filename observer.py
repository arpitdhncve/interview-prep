from cgitb import text


class Subject:

    def __init__(self):
        self.observers = []

    
    def add_observer(self, observer):
        self.observers.append(observer)

    
    def remove_observer(self, observer):
        self.observers.remove(observer)

    
    def update(self, update_text):
        for observer in self.observers:
            observer.observer_update(update_text)



class Observer:

    def __init__(self, name):
        self.name = name

    def observer_update(self, text):
        print(f"observer observed {text}")



def run_observer_pattern():

    subject1 = Subject()

    observer1 = Observer("abc")
    observer2 = Observer("def")

    subject1.add_observer(observer1)
    subject1.add_observer(observer2)

    subject1.update("Text changed")


if __name__ == "__main__":
    run_observer_pattern()