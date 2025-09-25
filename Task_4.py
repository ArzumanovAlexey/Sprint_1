new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop())
new_tasks.remove('task_007')
priority_task = new_tasks[-1]

print(new_tasks)
print(completed_tasks)
print(priority_task)