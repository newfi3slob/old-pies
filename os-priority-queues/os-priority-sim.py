import random
from queues import CircularQueue

class Job:
    def __init__(self, priority = 0, process_name = None):
        '''
        Object for  job description of various types
        :param priority: 0 for low and 1 for high priority
        :param process_name: Description of the process (optional)
        '''
        self.__id = random.randint(1,1000)
        self.__priority = priority
        if process_name  is None:
            if self.high_priority():
                self.__process_name = random.choice(['[OS] File Write', '[OS] File Read', '[OS] Display'])
            else:
                self.__process_name = random.choice(['[USER] Browser', '[USER] Music', '[USER] Calculator'])

    def high_priority(self):
        '''
        Priority of the job
        :return: True if process of high priority
        '''
        return self.__priority == 1

    def process_name(self):
        '''
        Process name of the job
        :return: returns the process name for the job
        '''
        return self.__process_name

    def __str__(self):
        return  '{:<15} : {:<20}\n{:<15} : {:<20}\n{:<15} : {:<20}'.format('ID',self.__id, 'Process Name',self.__process_name, 'Priority','HIGH' if self.__priority ==1 else 'LOW' )

def get_job():
    '''
    Return a job type , trying to simulate a queueing process for the CPU
    :return: Returns the Job Object or none
    '''
    if random.random() < .5:
        return Job(priority=1)
    if random.random() < .9:
        return Job(priority=0)
    return None # the no job

def process_complete():
    '''
    Returns a  boolean value telling if the current process is complete executing or not
    :return: True/False depending the process is complete or not
    '''
    if random.random() < 0.5:
        return True
    return False

def main():
    process_running = False # tells the state of the processor True if a process  is running
    current_job = None
    high_priority_queue = CircularQueue(1000)
    low_priority_queue = CircularQueue(1000)
    # we will run our computer for 10 time steps
    time_steps = 10
    for t in range(time_steps):
        print("######## RUN : {} ########\n".format(t+1))
        job = get_job() # get a  job
        if job:
            print("Job {} generated\n".format(job.process_name()))

        # Put the job in the appropriate queue
        
        # if a job exists (i.e. is NOT none)
        if job is not None:  
            
            # if job is high priority - enqueue to high priority queue
            if job.high_priority() == True:
                high_priority_queue.enqueue(job)
            
            # elif job is low priority - enqueue to low priority queue        
            elif job.high_priority() == False:
                low_priority_queue.enqueue(job)
              
        ###################################
        ## Get the status of current job ##
        ###################################
        if process_running:
            current_process_status = process_complete()
            if current_process_status:
                process_running = False
                print("JOB COMPLETED\n{}".format(current_job))
                current_job = None

        #######################
        # depending on the  status fo current job
        # get the next job and load on the processer
        ########################
        if not process_running:
           
            ## Remove the pass
            ## Check the status of queue , and dequeue the appropriate job
            ## set the job to current_job
            ## set process_running to True if job dequeued
            
            # if high priority queue is not empty - dequeue job from it
            if high_priority_queue.is_empty() is not True:
                current_job = high_priority_queue.dequeue() 
                
            # else - dequeue job from low priority queue
            elif low_priority_queue.is_empty is not True:
                current_job = low_priority_queue.dequeue()
                
            # when job is dequeued - process_running is set to TRUE
            process_running = True

        if not process_running:
            print("\n[PROCESSOR] Idle")
        else:
            print("\n[PROCESSOR] Busy")
        # status of queues
        print("Jobs waiting in High Priority Queue :{}".format(high_priority_queue.size()))
        print("Jobs waiting in Low Priority Queue :{}\n".format(low_priority_queue.size()))

if __name__ == '__main__':
    main()
