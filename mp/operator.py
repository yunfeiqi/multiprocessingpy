#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :Define base class for operators
@Time           :2020/08/28 13:47:19
@Author         :sam.qi
@Version        :1.0
'''

from multiprocessing import Process

class Operator(Process):

    def __init__(self):
        super().__init__()
        self.input_queue = None
        self.output_queue = None
        self.daemon = True
        # 设置后继个数
        self.tail_num = 1

    def get_input_queue(self):
        return self.input_queue

    def get_output_queue(self):
        return self.output_queue

    def set_input_queue(self, queue):
        self.input_queue = queue

    def set_output_queue(self, queue):
        self.output_queue = queue

    def set_tail_num(self,n):
        self.tail_num = n 

    def work(self, **params):
        raise

    def send_msg(self, queue, msg):
        if queue is None:
            raise RuntimeError("The function send_msg error: queue is None")
        queue.put(msg)

    def done(self):
        if self.output_queue is not None:
            for i in range(self.tail_num):
                self.output_queue.put(None)


    def pre_processing(self):
        pass
        
    def post_processing(self):
        pass

    def run(self):
        self.pre_processing()
        self.work()
        self.post_processing()
        self.done()