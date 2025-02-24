def task_manager():
    while True:
        
        work = input("What would you like to do? 'Add a task (A), View your tasks (Q), Delete a task (D), Clear your list (W), Edit a task (E) or Edit (S)': ").strip().lower()

        if work == "a":
            task = input("What task would you like to add? : ")
            confirm = input(f"Are you sure you want to add '{task}' to your list? Type 'Yes' to confirm: ").strip().lower()
            if confirm == "yes":
                with open("task_manager_data.txt", "r") as f:
                    data = f.readlines()
                    if task + "\n" in data:
                        print(f"'{task}' is already in your list.")
                    else:
                        with open("task_manager_data.txt", "a") as f:
                            f.write(task + "\n")
                        print(f"'{task}' has been added to your list.")
            else:
                print(f"'{task}' has not been added to your list.")    
                
        elif work == "q":
            f = open("task_manager_data.txt", "r")
            tasks = f.readlines()
            if tasks:
                index = 1  
                for task in tasks:
                    print(f"{index}. {task.strip()}")
                    index += 1  
            else:
                print("Your Task List is empty.")
                f.close()
                
        elif work == "d":
            f = open("task_manager_data.txt", "r")
            tasks = f.readlines()
            if tasks:
                index = 1  
                for task in tasks:
                    print(f"{index}. {task.strip()}")
                    index += 1  
            else:
                print("Your To-Do List is empty.")
                return
                    
            f = open("task_manager_data.txt", "r")
            print("Which task do you want to delete (Type the exact tast to delete): ") 
            data_delete = input("Enter the task you want to delete: ").strip()
            data = f.read()
            if data.find(data_delete) != -1:
                confirm = input(f"Are you sure you want to delete '{data_delete}'? Type 'Yes' to confirm: ").strip().lower()
                if confirm == "yes":
                    with open("task_manager_data.txt", "r") as f:
                        tasks = f.readlines()
                        tasks.remove(data_delete + "\n")
                        f = open("task_manager_data.txt", "w")
                        f.writelines(tasks) 
                        f.close()
                        print(f"'{data_delete}' has been deleted.")
                                    
                else:
                    print(f"'{data_delete}' has not been deleted.")
            else:
                print(f"'{data_delete}' is not in your To-Do List.")
                return
            
        elif work == "w":
            confirm = input("Are you sure you want to clear your list? Type 'Yes' to confirm: ").strip().lower()
            if confirm == "yes":
                f = open("task_manager_data.txt", "w")
                f.close()
                print("Your Task List has been cleared.")
            else:
                print("Your Task List has not been cleared.")
            
        elif work == "e":
            f = open("task_manager_data.txt", "r")
            tasks = f.readlines()
            if tasks:
                index = 1  
                for task in tasks:
                    print(f"{index}. {task.strip()}")
                    index += 1  
            else:
                print("Your Task List is empty.")
                return
            f.close()
            with open("task_manager_data.txt", "r") as f:
                data = f.read()
                print("Which task do you want to edit (Type the exact tast to edit): ") 
                data_replace = input("Enter the task you want to edit: ").strip()
                if data.find(data_replace) != -1:
                    new_data = input("Enter the new task: ")
                    confirm = input(f"Are you sure you want to change '{data_replace}' to '{new_data}'? Type 'Yes' to confirm: ").strip().lower()
                    if confirm == "yes":
                        str_replace_data = str(data_replace)
                        str_new_data = str(new_data)
                        changed_data = data.replace(str_replace_data, str_new_data)
                        with open("task_manager_data.txt", "w") as f:
                            f.write(changed_data)
                        print(f"'{data_replace}' has been changed to '{new_data}'.")
                        
                    elif data_replace == new_data:
                        print(f"'{data_replace}' is the same as '{new_data}'.")
                        return
                    
                    else:
                        print(f"'{data_replace}' has not been changed to '{new_data}'.")
                        return
                else:
                    print(f"'{data_replace}' is not in your To-Do List.")
                    return        
                
        elif work == "s":
            print("Goodbye!")
            return
        
        else:
            print("Invalid input. Please try again.")
            return
    
task_manager()
