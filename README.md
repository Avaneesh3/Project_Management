# Project_Management

The object model design for the project management application is done as follows:

Assumptions:
If the sum of total days required for all tasks to get completed is less than the total number of days given,
then the project can completed even if an individual task exceedes it's deadline.  
 
Problem Statement:
Given the tasks,dependencies,users,resources and the time taken for each task we need to find 
whether the project can be completed within the total number of days.
 
Classes:
(1)Class tasks
(2)Class users
(3)Class resources
(4)Class project_manager


Algorithm:

Here the tasks have dependencies and can only be implemented in a particular order.
Therefore, the tasks must be first topologically sorted.
However, we also want to minimise the time taken to complete all the tasks.
Therefore, at every step of toplogical sort, when we get the list of tasks having no dependencies, 
we choose the task having the nearest deadline to minimise the total time required to complete a project.
