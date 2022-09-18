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
    def __init__(self,user_type,users_available,users_engaged):
        self.user_type = user_type
        self.users_available = users_available
        self.users_engaged = users_engaged

    def get_user_summary():
        return 
        
    def count_available_users(user_type,required_count):
        return date_when_count_available


class resources:
    def __init__(self,resource_type,resources_available,resources_engaged):
        self.resource_type = resource_type
        self.resources_available = resources_available
        self.resources_engaged = resources_engaged
        
    def count_available_resources(resource_type,required_count):
        return date_when_count_available
    
    
class schedule:
    def __init__(self,task_deadlines,dependencies):
        self.task_deadlines = task_deadlines      #task_deadlines[task_name] = deadline
        self.dependencies = dependencies
        
    def sort_deadlines(task_deadlines):                    #tasks_sorted_by_deadlines[task_name] = index of eadline in sorted_deadlines
        sorted_deadlines = sorted(list(task_deadlines.values()))
        tasks_sorted_by_deadlines = {}
        for i in range(task_deadlines.keys()):
            tasks_sorted_by_deadlines[i] = sorted_deadlines.index(task_deadlines[i])
        return tasks_sorted_by_deadlines
        
    def topsortlist(AMat):
	return topsortlist
           
            
                
    
    
    
        
        
        
def project_allocate(end_date,project):
	if j.schedule() < j.deadline:
                
            else:
                return "fail"
