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

from mp.datasource.datasource  import Datasource

class FileDatasource(Datasource):
    def __init__(self, out_queues):
        super().__init__(out_queues)


    def validation_check(self,filepath):
        return True

    def work(self, filepath,splitor,block_size):

        # validation check 
        self.validation_check(filepath)
        # read data source 
        reader = pd.read_csv(filepath, sep=splitor,
                             chunksize=block_size, encoding='utf-8')
        
        # read data and processing  
        for i, chunk in enumerate(tqdm(reader, "FileDatasource Reader")):
            chunk_data = chunk.tolist()
            msg_id = self.get_hash_msgId(i)
            self.send_msg(msg_id,chunk_data)
        
        # done 
        self.done()