class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавление новой задачи с описанием и сроком."""
        self.tasks.append({
            'description': description,
            'deadline': deadline,
            'status': False  # По умолчанию задача не выполнена
        })
        print(f"Задача добавлена: '{description}', срок выполнения до {deadline}.")

    def mark_task_as_done(self, task_index):
        """Отметка задачи как выполненной по индексу."""
        if 0 <= task_index < len(self.tasks) and not self.tasks[task_index]['status']:
            self.tasks[task_index]['status'] = True
            print(f"Задача '{self.tasks[task_index]['description']}' отмечена как выполненная.")
        else:
            print("Ошибка: Задача с данным индексом не найдена или уже выполнена.")

    def list_pending_tasks(self):
        """Вывод списка невыполненных задач."""
        print("Текущие задачи:")
        has_pending = False
        for task in self.tasks:
            if not task['status']:
                has_pending = True
                print(f"- {task['description']} (срок: {task['deadline']})")
        if not has_pending:
            print("Нет невыполненных задач.")

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Закончить отчет", "2023-04-30")
task_manager.add_task("Подготовить презентацию", "2023-05-05")
task_manager.mark_task_as_done(0)
task_manager.list_pending_tasks()
