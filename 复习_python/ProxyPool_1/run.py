# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 15:55
# @Author  : Mqz
# @FileName: run.py
from proxypool.scheduler import Scheduler
import argparse

parser = argparse.ArgumentParser(description="Proxypool_1")

parser.add_argument('--processor', type=str, help='processor to run')
args = parser.parse_args()

if __name__ == '__main__':
    if args.processor:
        getattr(Scheduler(), f'num_({args.processor})')
    else:
        Scheduler().run()


