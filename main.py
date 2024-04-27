class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # Задача не выполнена по умолчанию

    def mark_as_done(self):
        """Отмечает задачу как выполненную."""
        self.status = True
        print(f"Задача '{self.description}' отмечена как выполненная.")

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "выполнена" if self.status else "не выполнена"
        return f"{self.description} (срок: {self.deadline}), статус: {status}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавление новой задачи с описанием и сроком."""
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: '{description}', срок выполнения до {deadline}.")

    def mark_task_as_done(self, task_index):
        """Отметка задачи как выполненной по индексу."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()
        else:
            print("Ошибка: Задача с данным индексом не найдена.")

    def list_pending_tasks(self):
        """Вывод списка невыполненных задач."""
        print("Текущие задачи:")
        has_pending = False
        for task in self.tasks:
            if not task.status:
                has_pending = True
                print(task)
        if not has_pending:
            print("Нет невыполненных задач.")
# Пример использования
task_manager = TaskManager()
task_manager.add_task("Закончить отчет", "2023-04-30")
task_manager.add_task("Подготовить презентацию", "2023-05-05")
task_manager.mark_task_as_done(0)
task_manager.list_pending_tasks()
