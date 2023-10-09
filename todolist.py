"""Command line interface project of To-do list
                 CodSoft internship"""
def add():
    """This function is for adding a new task in the To-Do list"""
    task=input("Add new task to the To-Do list")
    list.append(task)
    display()
def delete():
    """This function is for delete an existing task in the To-Do list"""
    index=int(input("Enter the number of the task to be deleted"))
    del list[index-1]
    display()
def display():
    """This function is to Display the List"""
    for i in range(len(list)):
        print("---------------")
        print('|',i+1,'|',list[i],'|')

"""initializing an empty list"""
list=[]
print("TO-DO LIST PROJECT FOR CodSoft internship (by Command line interface)")
choice=0
print("1.Add a new task\n2.Delete a task from below\n3.Quit")
while  choice!=3:
    """Taking choice of the user"""
    choice=int(input("Enter your choice (1 or 2 or 3) "))
    if choice==1:
        add()
    elif choice==2:
        delete()
    else:
        print("Please enter valid choice ")
