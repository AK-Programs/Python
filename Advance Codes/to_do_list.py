# Before running the code you need to create a txt file named as (to_do_list_data.txt) in the same folder where python file is located.

def to_do_list():
    print("Welcome to the To-Do List Manager!")

    while True:

        work = input(
            "What do you want to do? "
            "'Create a To-Do (A)', 'View your To-Do List (Q)', 'Clear your To-Do List or Delete a To-Do (S)', 'Edit your To-Do (W)', 'Exit (D)' : ") .strip() .lower()

        if work == "a":
            to_do = input("What do you want to add to your list? ")
            confirm = input(f"Are you sure you want to add '{to_do}' to your list? Type 'Yes' to confirm: ").strip().lower()
            if confirm == "yes":
                with open("to_do_list_data.txt", "r") as f:
                    data = f.readlines()
                    if to_do + "\n" in data:
                        print(f"'{to_do}' is already in your To-Do List.")
                    else:
                        with open("to_do_list_data.txt", "a") as f:
                            f.write(to_do + "\n")
                        print(f"'{to_do}' has been added to your list.")
            else:
                print(f"'{to_do}' has not been added to your list.")                

        elif work == "q":
            f = open("to_do_list_data.txt", "r")
            to_do_manage = f.readlines()
            if to_do_manage:
                index = 1  
                for task in to_do_manage:
                    print(f"{index}. {task.strip()}")
                    index += 1  
            else:
                print("Your To-Do List is empty.")
            f.close()
        
        elif work == "s":
            f = open("to_do_list_data.txt", "r")
            to_do_manage = f.readlines()
            f.close()
            delete_line = input("You want to clear your To-Do List or delete a To-Do? Type 'Clear' to clear your To-Do List or 'Delete' to delete a To-Do: ").strip().lower()
            if delete_line == "clear":
                confirm = input("Are you sure you want to clear your To-Do List? Type 'Yes' to confirm: ").strip().lower()
                if confirm == "yes":
                    f = open("to_do_list_data.txt", "w")
                    f.close()
                    print("Your To-Do List has been cleared.")
                else:
                    print("Your To-Do List has not been cleared.")
                    
            elif delete_line == "delete":
                    f = open("to_do_list_data.txt", "r")
                    to_do_manage = f.readlines()
                    if to_do_manage:
                        index = 1  
                        for task in to_do_manage:
                            print(f"{index}. {task.strip()}")
                            index += 1  
                    else:
                        print("Your To-Do List is empty.")
                        return
                    f.close()
                
                    f = open("to_do_list_data.txt", "r")
                    print("Which task do you want to delete (Type the exact tast to delete): ") 
                    data_delete = input("Enter the task you want to delete: ").strip()
                    data = f.read()
                    if data.find(data_delete) != -1:
                        confirm = input(f"Are you sure you want to delete '{data_delete}'? Type 'Yes' to confirm: ").strip().lower()
                        if confirm == "yes":
                            with open("to_do_list_data.txt", "r") as f:
                                tasks = f.readlines()
                                tasks.remove(data_delete + "\n")
                                f = open("to_do_list_data.txt", "w")
                                f.writelines(tasks) 
                                f.close()
                            print(f"'{data_delete}' has been deleted.")
                                
                        else:
                            print(f"'{data_delete}' has not been deleted.")
                    else:
                        print(f"'{data_delete}' is not in your To-Do List.")
                        return
                
                
        elif work == "w":
            f = open("to_do_list_data.txt", "r")
            data = f.readlines()
            if data:
                index = 1  
                for task in data:
                    print(f"{index}. {task.strip("\n")}")
                    index += 1  
            else:
                print("Your To-Do List is empty.")
                return
            f.close()
            with open("to_do_list_data.txt", "r") as f:
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
                        with open("to_do_list_data.txt", "w") as f:
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
        
        elif work == "d":
            print("Exiting the To-Do List Manager. Goodbye!")
            break  

        else:
            print("Error: Invalid choice! Please select 'A', 'Q', 'S', 'W' or 'D'.")

to_do_list()
