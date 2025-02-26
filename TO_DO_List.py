task=[]

def add_task():
    task.append(input("Enter the task to be added:"))
    print("Task added successfully\n\n")

def remove_task():
    if len(task)==0:
        print("No task to remove\n\n")
    else:
       idx=int(input(" Enter the task number to be removed "))
       task.pop(idx-1)
       print("Task removed successfully\n\n")

def show_tasks():
    if len(task)==0:
        print("No task to Display\n\n")
    else:
      print("Your TO - Do -list is as follows:")
      for i in range(len(task)):
         print(f"\n{i+1}. {task[i]}")
      print("\n\n")



print("welcome to TO-Do-LIST:")
while True:
    print("1️⃣  Add Task  \n2️⃣  Remove Task  \n3️⃣  Show Tasks  \n4️⃣  Exit")
    ch=int(input("Enter your choose:"))
    if(ch==1):
         print("    Add Task:\n")
         add_task()
    elif(ch==2):
        print("    Remove Task:\n")
        remove_task()
    elif(ch==3):
        print("    Showing  Task:\n")
        show_tasks()
    elif(ch==4):
        print("    Thank you for using TO-Do-List")
        break
    else:
        print("Invalid choice")

