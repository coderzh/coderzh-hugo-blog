#!/usr/bin/env python
# coding:utf-8

__author__ = 'coderzh'

import os
import re
import subprocess
from datetime import datetime
import sys

# replace to vim or others if your like
# EDITOR = ['MarkdownPad2.exe']
EDITOR = ['code']

if __name__ == '__main__':
    if len(sys.argv) > 1:
        post_name = sys.argv[1]
    else:
        post_name = input("Post'title: ")

    post_path = 'post/{year}/{date_format}-{post_name}.md'.format(
        year=datetime.now().year,
        date_format=datetime.now().strftime('%Y-%m-%d'),
        post_name=post_name
    )

    subprocess.call(['hugo', 'new', post_path])

    # replace template value
    post_rel_path = os.path.join('content', post_path)
    with open(post_rel_path, 'r', encoding='utf-8') as f:
        content = f.read()

    url = '/{date_format}/{post_name}'.format(
        date_format=datetime.now().strftime('%Y/%m/%d'),
        post_name=post_name
    )

    replace_patterns =[
        (re.compile(r'title:(.*)'), 'title: "%s"' % post_name),
        (re.compile(r'url:(.*)'), 'url: "%s/"' % url),
        (re.compile(r'\n---'), r'\n---'),
    ]

    for regex, replace_with in replace_patterns:
        content = regex.sub(replace_with, content)

    with open(post_rel_path, 'w', encoding='utf-8') as f:
        f.write(content)

    subprocess.Popen(' '.join(EDITOR + [post_rel_path]), shell=True)

