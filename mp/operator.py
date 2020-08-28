#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :Define base class for operators
@Time           :2020/08/28 13:47:19
@Author         :sam.qi
@Version        :1.0
'''

import threading


class Operator(threading.Thread):
    def __init__(self):
        self.input_queue = None
        self.output_queue = None

    def get_input_queue(self):
        return self.input_queue

    def get_output_queue(self):
        return self.output_queue

    def set_input_queue(self, queue):
        self.input_queue = queue

    def set_output_queue(self, queue):
        self.output_queue = queue

    def work(self, **params):
        raise

    def send_msg(self, queue, msg):
        if queue is None:
            raise RuntimeError("The function send_msg error: queue is None")
        queue.put(msg)

    def run(self):
        self.work()
