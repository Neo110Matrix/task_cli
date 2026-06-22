import sys


if len(sys.argv) < 3:
	print("usage: python test.py add description")
	sys.exit(
)

command = sys.argv[1]
description = sys.argv[2]

if command == "add" and  description is not None:
	print(f"valid command :-{command}- and\n description is :- {description}")
else:
	print("invalid command")
