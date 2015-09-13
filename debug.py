#!/usr/bin/env python
# coding:utf-8

import os
import shutil


def main():
    if os.path.exists('public'):
        shutil.rmtree('public')

    os.system('hugo server -w -v -b="http://127.0.0.1"')


if __name__ == '__main__':
    main()
