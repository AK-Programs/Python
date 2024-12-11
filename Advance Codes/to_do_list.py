def to_do_list():
    to_do_manage = []  
    print("Welcome to the To-Do List Manager!")

    while True:

        work = input(
            "What do you want to do? "
            "'Create a To-Do (R)', 'View To-Do List (P)', 'Exit (T)': ")

        if work == "R" or work == "r":
            to_do = input("What do you want to add to your list? ")
            if to_do:
                to_do_manage.append(to_do)
                print(f"'{to_do}' has been added to your list.")
            else:
                print("Error: You cannot add an empty task to the list.")

        elif work == "P" or work == "p":
            if to_do_manage:
                print("Your To-Do List:")
                index = 1  
                for task in to_do_manage:
                    print(f"{index}. {task}")
                    index += 1  
            else:
                print("Your To-Do List is empty.")

        elif work == "T" or work == "t":
            print("Exiting the To-Do List Manager. Goodbye!")
            break  

        else:
            print("Error: Invalid choice! Please select 'R', 'P', or 'T'.")

to_do_list()