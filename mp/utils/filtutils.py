#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description    :The Help functions for file's operation
@Time           :2020/08/27 15:22:10
@Author         :sam.qi
@Version        :1.0
'''

import os


def check_exist(path):
    return os.path.exists(path)


def is_file(path):
    return os.path.isfile(path)


def remove_file(path):
    if check_exist(path) and is_file(path):
        os.remove(path)
