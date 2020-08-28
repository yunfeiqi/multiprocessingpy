#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :Definit workflow of multi-processing task
@Time           :2020/08/27 16:00:44
@Author         :sam.qi
@Version        :1.0
'''
from mp.utils.queueutil import create_queue_list
from mp.tasknet.net import Net

class Workflow(Net):
    def __init__(self):
        super().__init__()
        # Define Task net structure

    
    def check_net(self):
        return len(self.layes) <=0


    def start(self):
        
        if self.check_net():
            # start 
            for layer in self.layes:
                for ope in layer:
                    ope.start()
                
            # wait
            for layer in self.layes:
                for ope in layer:
                    ope.join()
        else:
            print("No define Task net")
        
        print("Task Finished")