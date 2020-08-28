#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :To Definition data source for Files
@Time           :2020/08/27 15:17:17
@Author         :sam.qi
@Version        :1.0
'''

import pandas as pd
from tqdm import tqdm

from mp.datasource.datasource import Datasource


class FileDatasource(Datasource):

    def __init__(self, filepath, splitor, block_size):
        super().__init__()
        self.filepath = filepath
        self.splitor = splitor
        self.block_size = block_size

    def validation_check(self, filepath):
        return True

    def work(self):

        # validation check
        self.validation_check(self.filepath)
        # read data source
        reader = pd.read_csv(self.filepath, sep=self.splitor,
                             chunksize=self.block_size, encoding='utf-8')

        # read data and processing
        for i, chunk in enumerate(tqdm(reader, "FileDatasource Reader")):
            self.send_msg(self.get_output_queue(), chunk)

        # done
        self.send_msg(self.get_output_queue(), None)
