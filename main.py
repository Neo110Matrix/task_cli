import sys
from task_manager.task_service import add
 
command = sys.argv[1]
description = sys.argv[2]

if len(sys.argv) < 3:
	print(f"Usage Error: Add  descrption with -{command}")


#command = sys.argv[1]
#description = sys.argv[2]

if command == "add" and  description is not None:
	add(description)	
	
else:
	print("invalid command")