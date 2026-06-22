import json
from pathlib import Path
from datetime import datetime

#relative  path for json file

JSON_FILE = Path(__file__).parent/"task.json"

#Add a new task 
def add(description):
    #print("unpacking values ")
    #a, b = args
    status = "todo"
    created_at = datetime.now().isoformat()
    updated_at = datetime.now().isoformat()
    
    #print("after unpacking")
    #print(f"command is :-{a}\nDescription is :- {b}")
    
    with open(JSON_FILE, 'r') as file:
        tasks = json.load(file)
        
    print(tasks)
    
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
    
    with open(JSON_FILE, 'w') as file:
        json.dump(tasks, file, indent = 4)
        
    print(f"Task added successfully id:- {new_id}")