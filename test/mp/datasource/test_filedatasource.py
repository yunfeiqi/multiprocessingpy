#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :
@Time           :2020/08/27 15:33:27
@Author         :sam.qi
@Version        :1.0
'''

from mp.utils.queueutil import * 
from mp.datasource.filedatasource import * 

class TestFileDatasource(BaseTest):

    def test_work(self):
        # varibles definition 
        filePath = "test/mp/datasource/test.csv"

        queues = create_queue_list(4,10)
        ds = FileDatasource(queues)
        ds.work(filePath,splitor= ",",block_size=2)