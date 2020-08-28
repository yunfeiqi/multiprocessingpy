#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :
@Time           :2020/08/27 18:25:21
@Author         :sam.qi
@Version        :1.0
'''

from test.mp.mpTest import BaseTest
from workflow import Workflow
import traceback


class Test_Workflow(BaseTest):
    def test_queues_constract_mapping_Error(self):
        wf = Workflow()
        self.assertRaises(RuntimeError, wf.queues_constract_mapping, 4, 3)

    def test_queues_constract_mapping(self):
        wf = Workflow()
        mapping = wf.queues_constract_mapping(4, 5)
        right_ids = list(range(5))
        mapping_ids = list(range(5))
        mapping_ids[4] = 0
        target = list(zip(right_ids, mapping_ids))
        self.assertEqual(mapping, target)
