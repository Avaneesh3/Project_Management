#                    ---------------------------------Object Model--------------------------
class tasks:
    def __init__(self,task_number,task_deadline,users_required,resources_required):
        self.task_number = task_number                   
        self.task_deadline = task_deadline               #int deadline in days after counting from the starting day of the task  
        self.users_required = users_required             #dict users_required[user_type] = count_required
        self.resources_required = resources_required     #dict resources_required[resource_type] = count_required
 
            
class users:
    def __init__(self,user_type,users_available,users_engaged,users_engaged_for_days):
        self.user_type = user_type                       
        self.users_available = users_available           #int count of users available of given user type
        self.users_engaged = users_engaged               #int count of users engaged of given user type
        self.users_engaged_for_days = users_engaged_for_days    #int number of days engaged users will remain engaged

class resources:
    def __init__(self,resource_type,resources_available,resources_engaged,resources_engaged_for_days):
        self.resource_type = resource_type               
        self.resources_available = resources_available   #int count of resources available of given user type
        self.resources_engaged = resources_engaged       #int count of resources engaged of given user type
        self.resources_engaged_for_days = resources_engaged_for_days  #int number of days engaged resources will remain engaged

    
class project_manager:
    def __init__(self,tasks_list,task_dependencies,users_list,resources_list,time_taken_for_tasks):
        self.tasks_list = tasks_list                   #list of instances of tasks
        self.task_dependencies = task_dependencies     #dict task_dependencies[task name] = [list of task names which must be completed before given task ]
        self.users_list = users_list                   #list of instances of users
        self.resources_list = resources_list           #list of instances of resources  
        self.time_taken_for_tasks = time_taken_for_tasks  #dict time_taken_for_tasks[task name] = time taken to complete the task in days       

    def users_waiting_time(self,user_type,  required_count):
        for i in range(len(self.users_list)):
            if (i.user_type == user_type) and (i.users_available > required_count):
                return 0
            else:
                return i.users_engaged_for_days   #returns waiting time to obtain required number of user_type in days

    def resources_waiting_time(self,resource_type,required_count):
        for i in range(len(self.resources_list)):
            if (i.resource_type == resource_type) and (i.resources_available > required_count):
                return 0
            else:
                return i.resources_engaged_for_days  #returns waiting time to obtain required number of resource_type in days

    def task_completion(self,task_name):                     
        l=[]
        for i in task_name.users_required.keys():
            usr_days = self.users_waiting_time(i,task_name.users_required[i])
            l.append(usr_days)
        for j in task_name.resources_required.keys():
            rscr_days = self.resources_waiting_time(i,task_name.resources_required[i])
            l.append(rscr_days)                                 # returns time taken to complete a task including
        return max(l) + self.time_taken_for_tasks[task_name]    # the waiting time of users & resources in days. 


    def nearest_deadline(self, l):
        k = [i.task_deadline for i in l]
        for i in range(len(l)):
            if l[i].task_deadline == min(k):                    # returns task from list of tasks 
                return l[i]                                     # which has the nearest deadline.
        
def topological_sort(obj,task_dependencies):
    (indegree,topsortlist) = ({},[])
    for i in task_dependencies.keys():
        indegree[i] = 0
    for u in task_dependencies.keys():
        for v in task_dependencies[u]:
            indegree[v] = indegree[v] + 1
                
    l = []
    for i in task_dependencies.keys():
        if indegree[u] == 0: 
            l.append(u)
    
    while(len(l) != 0):
        t = obj.nearest_deadline(l)
        print(indegree[0])
        topsortlist.append(t)
        indegree[t] = indegree[t] - 1
        for k in task_dependencies[t]:
            indegree[k] = indegree[k] - 1                   #returns a topologically sorted list of tasks in which  
            if indegree[k] == 0:                            #at each iteration of sort where tasks having no dependencies are obtained   
                l.append(k)                                 #the task having the nearest deadline is chosen first.       
    return topsortlist

def fit_schedule(obj,topsortlist):                       
    time_available = 0                                      #checks whether the project can be completed after implementing tasks 
    time_taken = 0                                          #in the given topological order.
    for i in range(len(topsortlist)):
        time_available += topsortlist[i].task_deadline
        time_taken += obj.task_completion(topsortlist[i])         
    if time_available > time_taken :
        return "The project can be completed with the required schedule"
    else:
        return "The project cannot be completed with the required schedule"

#                                ----------------------Test Case-------------------------------        
    
#tasks
t0 = tasks(task_number=0,
            task_deadline=34,
                users_required={'sde':6,'ds':1,'analyst':4,'manager':1},
                        resources_required={'tables':14,'chairs':12,'meeting room':2})

t1 = tasks(task_number=1,
            task_deadline=8,
                users_required={'ds':1,'analyst':3,'manager':2},
                        resources_required={'tables':4,'chairs':6,'meeting room':1})

t2 = tasks(task_number=2,
            task_deadline=18,
                users_required={'sde':2,'analyst':6,'manager':3},
                        resources_required={'tables':8,'chairs':11,'meeting room':2})

#users
sde = users(user_type="sde", users_available=2, users_engaged=6, users_engaged_for_days=7)
ds = users(user_type="ds", users_available=0, users_engaged=2, users_engaged_for_days=18)
analyst = users(user_type="analyst", users_available=4, users_engaged=8, users_engaged_for_days=12)
manager = users(user_type="manager", users_available=2, users_engaged=2, users_engaged_for_days=14)

#resources
tables = resources(resource_type="tables", resources_available=2, resources_engaged=4, resources_engaged_for_days=13)
chairs = resources(resource_type="chairs", resources_available=14, resources_engaged=16, resources_engaged_for_days=16)
meeting_room = resources(resource_type="meeting room", resources_available=1, resources_engaged=2, resources_engaged_for_days=5)

task_dependencies = {t0:[t1],t1:[],t2:[t1]}
tasks_list = [t0,t1,t2]
users_list = [sde,ds,analyst,manager]
resources_list = [tables,chairs,meeting_room]
time_taken_for_tasks = {t0:24,t1:6,t2:16}

proj_mgr = project_manager(tasks_list,task_dependencies,users_list,resources_list,time_taken_for_tasks)


topsortlist = topological_sort(proj_mgr,task_dependencies)
print(fit_schedule(proj_mgr,topsortlist))
