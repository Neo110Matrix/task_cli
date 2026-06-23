import json
from pathlib import Path
from datetime import datetime


#relative  path for json file

JSON_FILE = Path(__file__).parent/"task.json"

#global function to save tasks
def save_task(tasks):    
    with open(JSON_FILE, 'w') as file:
            json.dump(tasks, file, indent = 4)
#global for loading json data
def load_task():
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def get_existing_id(tasks):
    return [task["id"] for task in tasks] 




#Add a new task 
def add(description):
    
    #checking validation for description
    #print("unpacking values ")
    #a, b = args
    
    status = "todo"
    created_at = datetime.now().strftime("%d %B %Y , %I:%M %p")
    updated_at = datetime.now().strftime("%d %B %Y , %I:%M %p")
    
    with open(JSON_FILE, 'r') as file:
        tasks = json.load(file)
        
    #print(tasks)
    
    
    if len(tasks) == 0:
        new_id = 1
    else:
        max_id = 0
    
        for task in tasks:
            current_id = task.get("id")
            
            if current_id > max_id:
                max_id = current_id
        new_id = max_id + 1
        
    new_task = {
        "id": new_id,
        "description": description ,
        "status": status,
        "created_at" : created_at,
        "updated_at" : updated_at
    }

    tasks.append(new_task)
    save_task(tasks)
    print(f"Task added successfully id:- {new_id}")
 

    
#FOR UPDATING EXISTING TASK

def update(description, update_description):
    
    tasks = load_task() #getting list of tasks from load tasks from json file
    
    
    #print(tasks)
    #print(description)
    
    #existing_id = [task["id"] for task in tasks]
    existing_id = get_existing_id(tasks)
    #print(existing_id)
        #description in in str type so need to change it to int to validatie further
    task_id = int(description)
    
    if task_id in existing_id:
        #print("valid id")
        for i in tasks:
            if task_id == i.get("id"):
                i["description"] = update_description
                i["updated_at"] = datetime.now().strftime("%d %B %Y , %I:%M %p")
                #print(i["description"] , update_description, i["updated_at"])
                save_task(tasks)
                print(f"Task successfully updated:-{task_id}")
    else:
        print(f"Task not found for :-{task_id}")
        
        
def delete(description):
    #delete_id we get is in form of str so we need to change it to in to work with it
    delete_id = int(description)
    
    tasks = load_task()
    existing_id = [task["id"] for task in tasks]
    
    if delete_id in existing_id:
        """print(existing_id)
        for i in tasks:
            if delete_id == i.get("id"):
                tasks.pop(i)"""
        
        #taking the data which is != delete_id so that:
        # delete_id data will not be included thus not be saved
        tasks = [task for task in tasks if task.get("id") != delete_id]
        
        save_task(tasks)
        print(f"task deleted successfully:- {delete_id}")  
    else:
        print("Invalid id !!!!!!!!!!!!")              
   
   
   
def mark_in_progress(mark_id):
    #print(mark_id)
    
    tasks = load_task()
    existing_id = get_existing_id(tasks)
    
    mark_id = int(mark_id)
    if mark_id in existing_id:
        print("inside loop")
        for i in tasks:
            if mark_id == i.get("id"):
                #updating status from todo to in-progress
                i["status"] = "in-progress"
                i["updated_at"] = datetime.now().strftime("%d %B %y %I:%M %p")
                
                save_task(tasks)
                print(f"status changed successfully {mark_id}")
                
      
def done(mark_done_id):
    
    mark_done_id = int(mark_done_id)
    tasks = load_task()
    existing_id = get_existing_id(tasks)
    
    if mark_done_id in existing_id:
        for i in tasks:
            if mark_done_id == i.get("id"):
                i["status"]  = "done" 
                i["updated_at"] = datetime.now().strftime("%d %B %y %I:%M %p")
                
                save_task(tasks)
                print(f"Task marked as Done successfully {mark_done_id}") 
 
 
    
def task_list():
    tasks = load_task()
    
    for task in tasks:
        print(f"""
                    ID          : {task['id']}
                    Description : {task['description']}
                    Status      : {task['status']}
                    Created At  : {task['created_at']}
                    Updated At  : {task['updated_at']}
                    """)
    
    
def done():
    
    tasks = load_task()
    print("\n\nTask which are Done!!!!!!!!!!!\n")
    for i in tasks:
        stat = i.get("status")
        if i.get("status") == "done":
            
            print(f"""
                    ID          : {i['id']}
                    Description : {i['description']}
                    Status      : {i['status']}
                    Created At  : {i['created_at']}
                    Updated At  : {i['updated_at']}
                    """)
        

    
def todo():
    tasks = load_task()
    
    for i in tasks:
        if i.get("status") == "todo":
            print(f"""
                    ID          : {i['id']}
                    Description : {i['description']}
                    Status      : {i['status']}
                    Created At  : {i['created_at']}
                    Updated At  : {i['updated_at']}
                    """)
    

def in_progress():
    tasks = load_task()
    
    for i in tasks:
        if i.get("status") == "in-progress":
            print(f"""
                    ID          : {i['id']}
                    Description : {i['description']}
                    Status      : {i['status']}
                    Created At  : {i['created_at']}
                    Updated At  : {i['updated_at']}
                    """)