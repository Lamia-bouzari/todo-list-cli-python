import csv


TODOS_FILE = "todos.csv"
todos = []


def add_one_task(title):
	"""Add one task title to the in-memory todo list."""
	todos.append(title)


def print_list():
	"""Display every task with a one-based position."""
	if not todos:
		print("No tasks found.")
		return

	for position, title in enumerate(todos, start=1):
		print(f"{position}. {title}")


def delete_task(number_to_delete):
	"""Delete a task by its one-based position, if the position is valid."""
	try:
		position = int(number_to_delete)
	except (TypeError, ValueError):
		print("Please enter a valid task number.")
		return

	if position < 1 or position > len(todos):
		print("That task number does not exist.")
		return

	removed_task = todos.pop(position - 1)
	print(f"Deleted: {removed_task}")


def save_todos():
	"""Save the current todo list to a CSV file."""
	with open(TODOS_FILE, "w", newline="", encoding="utf-8") as todo_file:
		writer = csv.writer(todo_file)
		for title in todos:
			writer.writerow([title])
	print("Tasks saved.")


def load_todos():
	"""Load todo titles from the CSV file, if it exists."""
	todos.clear()

	try:
		with open(TODOS_FILE, "r", newline="", encoding="utf-8") as todo_file:
			reader = csv.reader(todo_file)
			for row in reader:
				if row:
					todos.append(row[0])
	except FileNotFoundError:
		print("No saved todo file found.")
		return

	print("Tasks loaded.")


def main():
	"""Run the command-line todo menu."""
	while True:
		print("\nTodo List")
		print("add | list | delete | save | load | exit")
		command = input("Choose an option: ").strip().lower()

		if command == "add":
			title = input("Enter a task: ").strip()
			if title:
				add_one_task(title)
				print("Task added.")
			else:
				print("Task cannot be empty.")
		elif command == "list":
			print_list()
		elif command == "delete":
			number = input("Enter the task number to delete: ").strip()
			delete_task(number)
		elif command == "save":
			save_todos()
		elif command == "load":
			load_todos()
		elif command == "exit":
			print("Goodbye!")
			break
		else:
			print("Unknown option. Please choose from the menu.")


if __name__ == "__main__":
	main()