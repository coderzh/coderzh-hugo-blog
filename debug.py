#!/usr/bin/env python
# coding:utf-8

import os
import shutil


def main():
    shutil.rmtree('public')
    shutil.copytree('copy_to_public', 'public')

    os.system('hugo server -w -v')


if __name__ == '__main__':
    main()
