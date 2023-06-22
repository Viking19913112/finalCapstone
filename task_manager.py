# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# ======Def functions================

def check_user():
    # Reads the user.txt file and returns a list of usernames
    with open("user.txt", "r") as f:
        user_list = []
        for line in f:
            user_list.append(line.split(";")[0])
    return user_list

def reg_user():
    # Add a new user to the user.txt file  
    user_list = check_user()
    
    with open("user.txt", "a") as f :
        new_username = input("Please enter the username you would like to add, or 'e' to exit:\n")
        
        # Check that username does not exist
        if new_username in user_list:
            print("That username is already taken, please try a different username.\n")
            reg_user()
        elif new_username == "e":
            print("Returning to main menu.\n")
            
        else :
            password = input(f"Please enter a password for {new_username}:\n")
            print()
            confirmation = input("Please confirm the password entered:\n")

            if password == confirmation :
                f.write(f"\n{new_username};{password}\n")
                print(f"new user {new_username} has been added!")
                print()

            else :
                print("Your password and confirmation do not match, please try again.\n")

def add_task():
    # Add a new task to the task.txt file
    task_username = input("Name of person assigned to task: ")

    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": "No"
    }
    task_list.append(new_task)
    print("Task added!")
    print()

def view_all():
    # View all tasks
    print("All Tasks:")
    for task in task_list:
        print(f"Username: {task['username']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Completed: {task['completed']}")
        print()

def view_mine():
    # View all tasks assigned to the user that is currently logged-in.
    print("My Tasks:")
    for index, task in enumerate(task_list):
        if task['username'] == curr_user:
            print("-"*50)
            print(f"Task indicator number: {index+1}")
            print(f"Task: {task['title']}")
            print(f"Assigned to: {task['username']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            if task['completed'] == "Yes":
                print("Task completed")
            else:
                print("Task not completed")
    print("-"*50)

    # Allow the user that is currently logged-in to select a task to edit or mark as complete.
    while True:
        try:
            task_num = int(input("Enter the number of the task you would like to edit or -1 to return to the main menu: "))
            if task_num == -1:
                break
            elif task_num > len(task_list) or task_num <= 0:
                print("Invalid task number. Please enter a valid task number")
            else:
                break
        except ValueError:
            print("Invalid task number. Please enter a valid task number")

    if task_num != -1:
        task = task_list[task_num-1]
        print("-"*50)
        print(f"Task: {task['title']}")
        print(f"Assigned to: {task['username']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        if task['completed'] == "Yes":
            print("Task completed")
        else:
            print("Task not completed")
        print("-"*50)
        
        # Mark the task as complete or edit the task (edit thinks: description , due date)
        while True:
            try:
                edit_task = int(input(" 1- To mark the task as complete\n 2- To edit the task\n\n Enter your option: "))
                print("-"*50)
                if edit_task == 1:
                    task['completed'] = "Yes"
                    break
                elif edit_task == 2:
                    if task['completed'] == "Yes":
                        print("This task has already been completed and cannot be edited")
                        break
                    else:
                        while True:
                            try:
                                edit_task_detail = int(input("\n 1- To edit the due date\n 2- To edit the description\n\n Enter your option: "))
                                print("-"*50)
                                if edit_task_detail == 1:
                                    while True:
                                        try:
                                            new_due_date = input("\n Enter the new due date (YYYY-MM-DD): ")
                                            due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                            break
                                        except ValueError:
                                            print("Invalid datetime format. Please use the format specified")
                                    task['due_date'] = due_date_time
                                    break
                                elif edit_task_detail == 2:
                                    new_description = input("\n Enter the new description: ")
                                    task['description'] = new_description
                                    break
                                else:
                                    print("Invalid option. Please enter a valid option")
                            except ValueError:
                                print("Invalid option. Please enter a valid option")
                    break
                else:
                    print("Invalid option. Please enter a valid option")
            except ValueError:
                print("Invalid option. Please enter a valid option")

        # Updat selekted task in tasks.txt
        task_list[task_num-1] = task
        
        with open("tasks.txt", 'w') as task_file:
            for task in task_list:
                task_file.write(f"{task['username']};{task['title']};{task['description']};{task['due_date'].strftime(DATETIME_STRING_FORMAT)};{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{task['completed']}\n")
        
        print("\n Task updated!")
        print("-"*50)

def generate_reports():

    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
        user_data = [u for u in user_data if u != ""]

    task_list = []

    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = task_components[5]

        task_list.append(curr_t)

    user_list = []

    for u_str in user_data:
        curr_u = {}
        user_components = u_str.split(";")
        curr_u['username'] = user_components[0]
        curr_u['password'] = user_components[1]
        user_list.append(curr_u)

    # task_overview.txt
    total_tasks = len(task_list)
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    total_overdue_tasks = 0

    for task in task_list:
        if task['completed'] == "Yes":
            total_completed_tasks += 1

        else:
            total_uncompleted_tasks += 1

            if task['due_date'] < datetime.now():
                total_overdue_tasks += 1

    total_incomplete_percentage = round(total_uncompleted_tasks / total_tasks * 100, 2)
    total_overdue_percentage = round(total_overdue_tasks / total_tasks * 100, 2)
    
    with open("task_overview.txt", 'w') as task_overview_file:
        task_overview_file.write("Task overview File\n\n")
        task_overview_file.write("-"*50 + "\n")
        task_overview_file.write(f"Total tasks: {total_tasks}\n")
        task_overview_file.write(f"Total completed tasks: {total_completed_tasks}\n")
        task_overview_file.write(f"Total uncompleted tasks: {total_uncompleted_tasks}\n")
        task_overview_file.write(f"Total overdue tasks: {total_overdue_tasks}\n")
        task_overview_file.write(f"Total incomplete percentage: {total_incomplete_percentage}%\n")
        task_overview_file.write(f"Total overdue percentage: {total_overdue_percentage}%\n")
        task_overview_file.write("-"*50 + "\n")    
    
    # user_overview.txt
    total_users = len(user_list)
    total_tasks = len(task_list)
    
    with open("user_overview.txt", 'w') as user_overview_file:
        user_overview_file.write("User overview File\n\n")
        user_overview_file.write("-"*50 + "\n")
        user_overview_file.write(f"Total users: {total_users}\n")
        user_overview_file.write(f"Total tasks: {total_tasks}\n")
        user_overview_file.write("-"*50 + "\n")
        
        for user in user_list:
            total_tasks_assigned = 0
            total_tasks_completed = 0
            total_tasks_uncompleted = 0
            total_tasks_overdue = 0

            for task in task_list:
                if task['username'] == user['username']:
                    total_tasks_assigned += 1
                    if task['completed'] == "Yes":
                        total_tasks_completed += 1
                    else:
                        total_tasks_uncompleted += 1
                        if task['due_date'] < datetime.now():
                            total_tasks_overdue += 1
                            
            if total_tasks_assigned == 0:
                total_tasks_assigned_percentage = 0
                total_tasks_completed_percentage = 0
                total_tasks_uncompleted_percentage = 0
                total_tasks_overdue_percentage = 0
            
            else:
                total_tasks_assigned_percentage = round(total_tasks_assigned / total_tasks * 100, 2)
                total_tasks_completed_percentage = round(total_tasks_completed / total_tasks_assigned * 100, 2)
                total_tasks_uncompleted_percentage = round(total_tasks_uncompleted / total_tasks_assigned * 100, 2)
                total_tasks_overdue_percentage = round(total_tasks_overdue / total_tasks_assigned * 100, 2)

            user_overview_file.write(f"User: {user['username']}\n\n")
            user_overview_file.write(f"Total tasks assigned: {total_tasks_assigned}\n")
            user_overview_file.write(f"Total tasks assigned percentage: {total_tasks_assigned_percentage}%\n")
            user_overview_file.write(f"Total tasks completed percentage: {total_tasks_completed_percentage}%\n")
            user_overview_file.write(f"Total tasks uncompleted percentage: {total_tasks_uncompleted_percentage}%\n")
            user_overview_file.write(f"Total tasks overdue percentage: {total_tasks_overdue_percentage}%\n")
            user_overview_file.write("-" * 50)
            user_overview_file.write("\n")

    print("Task and user overview files have been generated.")
    input("Press enter to continue...")
    return


#=====Main Program=====

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []

for t_str in task_data:
    
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = task_components[5]

    task_list.append(curr_t)


#====Login Section====
# This code reads usernames and password from the user.txt file to 
# allow a user to login.


# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}

for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False

while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue

    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        
    else:
        print("Login Successful!")
        logged_in = True

#====Main Menu====

# main menu for admin
if curr_user == 'admin':
    while True:
        print()
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate reports
        ds - Display statistics
        e - Exit
        : ''').lower()

        if menu == 'r':
            # Allow a user to the user.txt file'''
            reg_user()

        elif menu == 'a':
            # Allow a user to add a new task to task.txt file
            # Prompt a user for the following: 
            # - A username of the person whom the task is assigned to,
            # - A title of a task,
            # - A description of the task and 
            # - the due date of the task.
            add_task()

        elif menu == 'va':
            # Reads the task from task.txt file and prints to the console in the 
            # format of Output 2 presented in the task pdf (i.e. includes spacing
            # and labelling) 
            view_all()

        elif menu == 'vm':
            # Reads the task from task.txt file and prints to the console in the 
            # format of Output 2 presented in the task pdf (i.e. includes spacing
            # and labelling)
            view_mine()

        elif menu == 'gr' and curr_user == 'admin':
            # Generate reports
            generate_reports()

        elif menu == 'ds' and curr_user == 'admin': 
            # If the user is an admin they can display statistics about number of users
            # and tasks.
            num_users = len(username_password.keys())
            num_tasks = len(task_list)

            print("-----------------------------------")
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("-----------------------------------")    

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
            
# main menu for user
else:
    while True:
        print()
        menu = input('''Select one of the following Options below:
        a - Add a task
        va - View all tasks
        vm - View my task
        e - Exit
        : ''').lower()

        if menu == 'a':
            # Allow a user to add a new task to task.txt file
            # Prompt a user for the following: 
            #  - A title of a task,
            #  - A description of the task and 
            #  - the due date of the task.'''
            add_task()

        elif menu == 'va':
            # Reads the task from task.txt file and prints to the console in the 
            # format of Output 2 presented in the task pdf (i.e. includes spacing
            # and labelling)  
            view_all()

        elif menu == 'vm':
            # Reads the task from task.txt file and prints to the console in the 
            # format of Output 2 presented in the task pdf (i.e. includes spacing
            # and labelling)
            view_mine()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")