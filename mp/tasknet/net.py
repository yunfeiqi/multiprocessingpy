'''
@Description    :Set of function to construct tasknet
@Time           :2020/08/28 13:41:23
@Author         :sam.qi
@Version        :1.0
'''

from mp.utils.queueutil import create_queue_list


class Net(object):
    def __init__(self):
        super().__init__()
        self.layes = []
        self.relations = []

    def reserve(self, left, right, mapping):
        # reserve structure of net

        # only first
        if len(self.layes) <= 0:
            self.layes.append(left)
        self.layes.append(right)

        # reserve relations
        self.relations.append(mapping)

    def display_net(self):
        for mapping in self.relations:
            print(mapping)

    def hash_relation(self, left: list, right: list, capacity=50):
        left_cnt = len(left)
        right_cnt = len(right)

        queue_cnt = min(left_cnt, right_cnt)
        queues = create_queue_list(left_cnt, capacity)

        # mapping
        left_mapping = [id % queue_cnt for id in range(left_cnt)]
        right_mapping = [id % queue_cnt for id in range(right_cnt)]

        # set left side queue
        for id, ope in enumerate(left):
            q_id = left_mapping[id]
            queue = queues[q_id]
            ope.set_output_queue(queue)
            ope.set_tail_num(right_cnt)

        # set right side queue
        for id, ope in enumerate(right):
            q_id = right_mapping[id]
            queue = queues[q_id]
            ope.set_input_queue(queue)

        self.reserve(left, right, left_mapping)
