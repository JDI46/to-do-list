class ToDoList:
    list = []

    
    def __init__(self, new_task):
        self.new_task = new_task

    def remove_task(self):
        list.remove(self.new_task)

    def view_task(self):
        print(list)


def create_task(new_task):
    print(new_task)


create_task(str(input(" ")))