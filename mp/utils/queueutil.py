#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :The util function for queue
@Time           :2020/08/27 15:39:38
@Author         :sam.qi
@Version        :1.0
'''

from multiprocessing import Queue


def create_queue_list(n, capacity_q):
    '''
    @Description    : To create a set of queue
    @Time    		 :2020/08/27 15:40:19
    @Author         :sam.qi
    @Param          :
    @Return         :
    '''
    queue = Queue(capacity_q)
    return [queue] * n
