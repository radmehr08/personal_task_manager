from tasks import tasks


name = input("What's your name? ")
print("Welcome " + name)
while True:
    user_tasks = input("Put a task : ")
    tasks.append(user_tasks)
    print(f"Your first task is {user_tasks}")