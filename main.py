

#class takes new task and adds to list


class ToDoList:
  
  list = []

  @classmethod
  def add_task(cls):
    while True:
      add = input("New Task: ")
      if add.lower() == 'stop':
          break
      cls.list.append(add)
      

  @classmethod
  def remove_task(cls):
    remove_prompt = input("Delete: ")
    if remove_prompt.isdigit():
      cls.list.remove(remove_prompt)


  @classmethod
  def view_tasks(cls):
    for i in cls.list:
      print(i)


ToDoList.add_task()
# ToDoList.remove_task()
ToDoList.view_tasks()


    
    