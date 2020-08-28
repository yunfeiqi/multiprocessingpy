#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :
@Time           :2020/08/27 18:25:21
@Author         :sam.qi
@Version        :1.0
'''

from mp.datasource.filedatasource import FileDatasource
from mp.processor.processor import Processor
from mp.dump.filedump import FileDump

from workflow import Workflow
from test.mp.mpTest import BaseTest

import traceback


class MyProcessor(Processor):
    def work(self):
        while True:
            data = self.input_queue.get()
            self.output_queue.put(data)

class MyWorkflow(Workflow):
    def __init__(self):
        super().__init__()
        
        # datasrouce 
        ds = FileDatasource("test/test.csv",",",10)
        dss = [ds]

        # processor 
        processors = [MyProcessor() for i in range(3)]

        # dump
        dumps = [FileDump("test.csv")]

        self.hash_relation(dss,processors)
        self.hash_relation(processors,dumps)




class Test_Workflow(BaseTest):
    
    def test_work(self):
        m_wf  = MyWorkflow()
        m_wf.start()
