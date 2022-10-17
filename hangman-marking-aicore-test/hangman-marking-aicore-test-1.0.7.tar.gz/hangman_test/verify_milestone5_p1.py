from .verify import get_errors_fails, mark_incomplete, mark_complete
import os
task1_id = '6abbafb7-59a3-481a-9b1f-837e37b5826c' # Code the logic of the game
task2_id = 'f9464de6-74a0-43f7-aa62-91f2677b267f' # Document your experience

task_list = [
    task1_id,
    task2_id,
]

if 'milestone_5_p1.txt' in os.listdir('.'):
    errors = get_errors_fails('milestone_5_p1.txt')
    if len(errors) != 0:
        mark_incomplete(task1_id, errors['test_presence_milestone_5'])
        mark_incomplete(task2_id)
else:
    for task in task_list:
        mark_incomplete(task)
