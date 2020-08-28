#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :
@Time           :2020/08/27 15:33:27
@Author         :sam.qi
@Version        :1.0
'''

from mp.utils.queueutil import create_queue_list
from mp.datasource.filedatasource import FileDatasource
from test.mp.mpTest import BaseTest


class TestFileDatasource(BaseTest):

    def setUp(self):
        filePath = "test/mp/datasource/test.csv"
        self.ds = FileDatasource(filePath, ",", 3)

    def test_work_Error(self):
        self.assertRaises(RuntimeError, self.ds.work)

    def test_work(self):
        queue = create_queue_list(4, 10)[0]
        self.ds.set_output_queue(queue)
        self.ds.work()

        # show values
        value = queue.get()
        while value is not None:
            print(value)
            value = queue.get()
