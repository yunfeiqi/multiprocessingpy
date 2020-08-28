#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :
@Time           :2020/08/27 17:40:37
@Author         :sam.qi
@Version        :1.0
'''

from mp.utils.filtutils import remove_file, check_exist
from mp.utils.queueutil import create_queue_list
from mp.dump.filedump import FileDump
from test.mp.mpTest import BaseTest


class Test_FileDump(BaseTest):
    def test_work(self):
        queue = create_queue_list(1, 10)
        dump = FileDump(queue[0], "test.txt")
        for i in range(5):
            queue[0].put(i)

        queue[0].put(None)
        dump.work()
        self.assertTrue(check_exist("test.txt"))
        remove_file("test.txt")
