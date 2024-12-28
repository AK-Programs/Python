def to_do_list():
    print("Welcome to the To-Do List Manager!")

    while True:

        work = input(
            "What do you want to do? "
            "'Create a To-Do (R)', 'View your To-Do List (P)', 'Clear your To-Do List (C)', 'Exit (T)': ") .strip() .lower()

        if work == "r":
            to_do = input("What do you want to add to your list? ")
            confirm = input(f"Are you sure you want to add '{to_do}' to your list? Type 'Yes' to confirm: ").strip().lower()
            if confirm == "yes":
                f = open("to_do_list_data.txt", "a")
                f.write(to_do + "\n")
                f.close()
                print(f"'{to_do}' has been added to your list.")
            else:
                print(f"'{to_do}' has not been added to your list.")
                

        elif work == "p":
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
        
        elif work == "c":
            f = open("to_do_list_data.txt", "r")
            to_do_manage = f.readlines()
            f.close()
            if to_do_manage:
                print("Are you sure you want to clear your To-Do List?")
                confirm = input("Type 'Yes' to confirm: ").strip().lower()
                if confirm == "yes":
                    f = open("to_do_list_data.txt", "w")
                    f.close()
                    print("Your To-Do List has been cleared.")
                else:
                    print("Your To-Do List has not been cleared.")
                    
                f = open("to_do_list_data.txt", "w")
                f.close()
            else:
                print("Your To-Do List is already empty.")
        
        elif work == "t":
            print("Exiting the To-Do List Manager. Goodbye!")
            break  

        else:
            print("Error: Invalid choice! Please select 'R', 'P', 'C' or 'T'.")

to_do_list()
