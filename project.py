import numpy as np
class tasks:
    def __init__(self,task_number,task_deadline,users_required,resources_required):
        self.task_number = task_number
        self.task_deadline = task_deadline
        self.users_required = users_required                   #users_required[user_type] = count_required
        self.resources_required = resources_required           #resources_required[resource_type] = count_required

    def schedule(start_date = 0):
        return task_completion_date       
            
class users:
    def __init__(self,user_type,users_available,users_engaged,users_engaged_for_days):
        self.user_type = user_type
        self.users_available = users_available
        self.users_engaged = users_engaged
        self.users_engaged_for_days = users_engaged_for_days
    def get_user_summary():
        return 
        
    def count_available_users(user_type,required_count):
        return date_when_count_available


class resources:
    def __init__(self,resource_type,resources_available,resources_engaged,resources_engaged_for_days):
        self.resource_type = resource_type
        self.resources_available = resources_available
        self.resources_engaged = resources_engaged
        self.resources_engaged_for_days = resources_engaged_for_day
        
    def count_available_resources(resource_type,required_count):
        return date_when_count_available


class project_manager:
    def __init__(self,tasks_list,task_dependencies,users_list,resources_list):
        self.tasks_list = tasks_list                   #list of instances of task
        self.task_dependencies = task_dependencies     #task_dependencies[task_number] = [list of task_numbers]
        self.users_list = users_list                   #list of instances of users
        self.resources_list = resources_list           #list of instances of resources 

    def create_matrix(task_dependencies):
        return matrix_of_dependencies             

    def task_completion_date(tasks_list[i]):
        return task_completion_date

    def get_schedule(task_number,start_date = 0):
        return task_completion_date 
