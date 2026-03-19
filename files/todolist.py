task = []
print("to do list")
try:
    while True:
        a = int(input("1.Add a task\n2.Remove last task\n3.show tasks\n4.Exit\n"))
        if a == 1:
            q = str(input("Name of task:\n"))
            task.append(q)
            print("task added\n")
        elif a == 2:
            if len(task) > 0:
                e = len(task) - 1
                print("task", task[e], "has removed")
                task.pop(-1)
            else:
                print("There is no task in list")
        elif a == 3:
            for i in task:
                print(i)
            
        elif a == 4:
            break
except ValueError:
    pass