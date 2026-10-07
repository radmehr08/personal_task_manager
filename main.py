from tasks import tasks
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
    if user_tasks == "done":
        with open("tasks.txt", "a") as file:
            file.write(f"name is {name} the tasks are {tasks}\n")
            break
    tasks.append(user_tasks)
    print(f"your tasks are {tasks}")