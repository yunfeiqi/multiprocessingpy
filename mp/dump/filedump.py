#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :Dump data to file
@Time           :2020/08/27 16:01:59
@Author         :sam.qi
@Version        :1.0
'''
import traceback
from mp.dump.dump import Dump


class FileDump(Dump):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def work(self):

        with open(self.filepath, 'w', encoding="utf-8") as f:
            while True:
                try:
                    msg = self.get_input_queue().get()
                    if msg is None:
                        break
                    f.write(str(msg))
                    f.write("\n")
                except Exception as identifier:
                    traceback.print_exc()
                    print(identifier)
                    break
