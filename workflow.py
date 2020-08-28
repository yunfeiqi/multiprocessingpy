#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :Definit workflow of multi-processing task
@Time           :2020/08/27 16:00:44
@Author         :sam.qi
@Version        :1.0
'''
from mp.utils.queueutil import create_queue_list


class Workflow(object):
    def __init__(self):
        super().__init__()

    def create_datasource(self):
        '''
        @Description    : Return Datasource
        @Time    		 :2020/08/27 18:05:34
        @Author         :sam.qi
        @Param          :
        @Return         :
        '''

        raise NotImplementedError("Function create_datasource not implement")

    def create_processor(self):
        '''
        @Description    : The logical for each data 
        @Time    		 :2020/08/27 18:10:42
        @Author         :sam.qi
        @Param          :
        @Return         :
        '''

        raise NotImplementedError("Function create_processor not implement")

    def create_dump(self):
        '''
        @Description    :
        @Time    		 :2020/08/27 18:14:47
        @Author         :sam.qi
        @Param          :
        @Return         :
        '''

        raise NotImplementedError("Function create_dump not implement")

    def queues_constract_mapping(self, left_cnt, right_cnt):
        '''
        @Description    : Establish a mapping relationship between two queue list
        @Time    		 :2020/08/28 11:23:35
        @Author         :sam.qi
        @Param          :
        @Return         :
        '''

        if left_cnt > right_cnt:
            raise RuntimeError(
                "Error has occurred in [queues_constract_mapping] that in class of Workflow: the variable left_cnt is bigger right_cnt")

        right_ids = list(range(right_cnt))
        mappting_ids = [r_id % left_cnt for r_id in right_ids]
        return list(zip(right_ids, mappting_ids))

    def work(self, parallel_ds, parallel_processor, parallel_dump):
        # create message queues to connecting data source ,processors and dumps

        ds_output_qs = create_queue_list(parallel_ds)
        proc_output_qs = create_queue_list(parallel_processor)
        dump_output_qs = create_queue_list(parallel_dump)

        # Establish mapping for all queues
        ds_proc_queue_mapping = self.queues_constract_mapping(
            parallel_ds, parallel_processor)
        proc_dump_mapping = self.queues_constract_mapping(
            parallel_processor, parallel_dump)

        # create data source instance
        for ds_id in range(parallel_ds):
            ds_queue = ds_output_qs[ds_id]
            self.create_datasource(ds_id, ds_queue)

        # create processors
        for proc_id in range(parallel_processor):
            mapping = ds_proc_queue_mapping[proc_id]
            ds_queue = ds_output_qs[mapping[0]]
            proc_quue = proc_output_qs[mapping[1]]
            processors = self.create_processor(ds_queue, proc_quue)

        # create dumps
        for dump_id in range(parallel_processor):
            mapping = ds_proc_queue_mapping[dump_id]

        datasources = self.create_datasource()
        processors = self.create_processor()
        dumps = self.create_dump()

        # ------start-------
        for ds in datasources:
            ds.start()

        for processor in processors:
            processor.start()

        for dump in dumps:
            dump.start()

        # ------wait-------
        for ds in datasources:
            ds.json()

        for processor in processors:
            processor.json()

        for dump in dumps:
            dump.json()
