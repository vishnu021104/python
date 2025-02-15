def task():
    tasks=[]
    print("---------welcome to task management-----------")

    print("="*50)

    total_task=int(input("enter how many tasks are you want to add : "))

    for i in range(1,total_task+1):

        task_name=input(f"enter task {i} = ")
        tasks.append(task_name)
    print(f"today's tasks are : \n {tasks} ")    

    print("="*50) 
    
    
    print("*"*50)
    while True:
        operation=int(input(" 1.add \n 2.update \n 3.delete \n 4.view \n 5.exit \n enter to choose the operation(1-5) : "))

        if operation == 1:
            add=input("enter task you want to add : ")
            tasks.append(add)

            print("-"*50)
            print(f"the task {add} has been successfully added......")
            print("-"*50)


        elif operation == 2:
            updated_task=input("enter the task name of you want update : ")
            if updated_task in tasks:
                new_task=input("enter the new task for update : ")
                ind=tasks.index(updated_task)
                tasks[ind]=new_task

                print("-"*50)
                print("the updated task is ",new_task)
                print(f"the task {updated_task} has been updated to the task {new_task} successfully......")
                print("-"*50)

            else:
                print("-"*50)
                print("The task is Invalid ")   
                print("-"*50) 


        elif operation == 3:
            deleted_task=input("enter the deleted task : ")
            if deleted_task in tasks:
                ind=tasks.index(deleted_task)
                del tasks[ind] 

                print("-"*50)
                print(f"the {deleted_task} task has been deleted successfully.......")
                print("-"*50)

            else:
                print("-"*50)
                print("The task is Invalid ")   
                print("-"*50)     

        elif operation ==4:
            print("-"*50)
            print("the total tasks are ",tasks) 
            print("-"*50)

        else:
            print("-"*50)
            print("closing the program......")
            print("-"*50)
            exit()                  

    
        print("*"*50)
task()