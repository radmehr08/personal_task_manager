from tasks import tasks
from tasks import priority
import os
from dotenv import load_dotenv

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")

name = input("what is your name? ")
print("Welcome " + name)

while True:
    user_tasks = input("put a task: ")
    number = 1
    
    if user_tasks == "done":
    
                for i in range(len(tasks)):
                    a = tasks[i]
                    b = priority[i]
                    print(f"task {number} : {a} and priority for task {number} : {b}")
                    with open("tasks.txt", "a") as file:
                        file.write(f"task {number} : {a} and priority for task {number} : {b}\n")
                    number += 1
                break

    user_priority = input("How high is the priority of this task?(low, medium, high): ") 

    

    if user_priority == "low" or user_priority == "medium" or user_priority == "high":
        print(f"your new task is {user_tasks} and your priority of your task is {user_priority}")
    else:
        while True:
            user_priority = input("error please enter (low, medium, high): ") 

            if user_priority == "low" or user_priority == "medium" or user_priority == "high":
                print(f"your new task is {user_tasks} and your priority of your task is {user_priority}")
                break
            else:
                continue
    
    tasks.append(user_tasks)
    priority.append(user_priority)