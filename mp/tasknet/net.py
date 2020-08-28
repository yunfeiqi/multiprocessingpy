'''
@Description    :Set of function to construct tasknet
@Time           :2020/08/28 13:41:23
@Author         :sam.qi
@Version        :1.0
'''

from mp.operator import Operator
from mp.utils.queueutil import create_queue_list

class Net(object):
    def __init__(self):
        super().__init__()
        self.layes = []

    def hash_relation(self,left: list, right: list,capacity=50):
        left_cnt = len(left)
        right_cnt = len(right)
        if left_cnt > right_cnt:
            raise RuntimeError("The size of left cant't greater than right side to hash relation")

        # mapping
        right_ids = range(right_cnt)
        mappint_id = [r_id % left_cnt for r_id in right_ids]

        queues = create_queue_list(left_cnt)

        # set left side queue
        for id,ope in enumerate(left):
            ope.set_output_queue(queues[id])

        # set right side queue
        for id,ope in enumerate(right):
            m_left_id = mappint_id[id]
            ope.set_input_queue(queues[m_left_id])

        # reserve structure of net
        self.layes.append(left)
        self.layes.append(right)

