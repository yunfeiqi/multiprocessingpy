#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :The Definition of base data source 
@Time           :2020/08/27 14:56:02
@Author         :sam.qi
@Version        :1.0
'''

import abc
from abc import abstractmethod

import logging

class Datasource(abc.ABC):
    '''
    @Description    : The base class of data source
    @Time    		 :2020/08/27 14:57:36
    @Author         :sam.qi
    @Param          :
    @Return         :
    '''
    
    def __init__(self,out_queues):        
        
        self.logger = logging.getLogger(__name__)
        self.out_queues = out_queues
        self.queue_size = len(out_queues)

    def send_msg(self,msgId,msg):
        if msgId >= self.queue_size:
            raise IndexError("msqId out of the size of the set of queue")
        
        queue = self.out_queues[msgId]
        if queue is None:
            raise NotImplementedError("The Queue with index {} is None ".format(msgId))
        queue.put(msg)

    def get_hash_msgId(self,num):
        return num % self.queue_size

    def done(self):
        '''
        @Description    :Send Finished Single
        @Time    		 :2020/08/27 15:14:48
        @Author         :sam.qi
        @Param          :
        @Return         :
        '''

        for queue in self.out_queues:
            queue.put(None)

    @abstractmethod
    def work(self, **params):
        pass
