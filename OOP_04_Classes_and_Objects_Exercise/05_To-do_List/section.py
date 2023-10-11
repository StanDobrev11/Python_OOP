"""
The Section class should receive a name (string) upon initialization. The task also has one instance attribute:
tasks (empty list)
The Section class should also have four methods:
- add_task(new_task: Task)
o Adds a new task to the collection and returns "Task {task details} is added to the
section"
o If the task is already in the collection, returns "Task is already in the section
{section_name}"
- complete_task(task_name: str)
o Changes the task to completed (True) and returns "Completed task {task_name}"
o If the task is not found, returns "Could not find task with the name {task_name}"
- clean_section()
o Removes all the completed tasks and returns "Cleared {amount of removed tasks}
tasks."
- view_section()
o Returns information about the section and its tasks in this format:
 "Section {section_name}:
 {details of the first task}
 {details of the second task}
 …
 {details of the n task}"

"""


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: task_name == t.name, self.tasks))
            task.completed = True
            return f"Completed task {task.name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        return (f"Section {self.name}:\n" +
                '\n'.join(task.details() for task in self.tasks))
