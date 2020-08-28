#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :The base class for Dump operators
@Time           :2020/08/28 13:49:03
@Author         :sam.qi
@Version        :1.0
'''

from mp.operator import Operator


class Dump(Operator):

    def post_processing(self):
        print("{} Dump Finished".format(self.name))

    def work(self):
        raise NotImplementedError("")
