#!/usr/bin/env python
# coding:utf-8

import os
import sys
import glob
import shutil
import subprocess

__author__ = 'coderzh'

GIT_HUB_REPO = 'git@github.com:coderzh/hugo-blog-deployed.git'
GIT_CAFE_REPO = 'git@gitcafe.com:coderzh/coderzh-hugo-blog.git'


class ChDir:
    """Context manager for changing the current working directory"""
    def __init__(self, new_path):
        self.newPath = os.path.expanduser(new_path)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.savedPath)


def deploy():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    commit_msg = ''

    with ChDir(current_dir):
        # step1 clean
        os.system('git fetch origin')
        os.system('git checkout master')
        os.system('git reset --hard origin/master')
        os.system('git clean -fdx')
        # on windows set TERM=msys
        s = subprocess.Popen('git log -1 --pretty=format:"%s"',
                             shell=True, stdout=subprocess.PIPE)
        commit_msg = s.communicate()[0]
        # step2 build
        os.system('hugo -v  --cacheDir="./cache"')

    gh_pages_dir = os.path.join(parent_dir, 'gh-pages')

    # step3 clone if not exists
    if not os.path.exists(gh_pages_dir):
        with ChDir(parent_dir):
            os.system('git clone %s gh-pages' % GIT_HUB_REPO)
        with ChDir(gh_pages_dir):
            os.system('git remote add gitcafe %s' % GIT_CAFE_REPO)

    with ChDir(gh_pages_dir):
        # step4 clean and pull
        os.system('git fetch origin')
        os.system('git checkout gh-pages')
        os.system('git reset --hard origin/gh-pages')
        os.system('git clean -fdx')

        # step5 remove all files
        for f in os.listdir('.'):
            if f != '.git':
                if os.path.isfile(f):
                    os.remove(f)
                elif os.path.isdir(f):
                    shutil.rmtree(f)

        # step6 copy new files
        from_dir = os.path.join(current_dir, 'public')
        for f in os.listdir(from_dir):
            file_path = os.path.join(from_dir, f)
            if os.path.isfile(file_path):
                shutil.copy(file_path, '.')
            elif os.path.isdir(file_path):
                shutil.copytree(file_path, f)

        # step7 commit and push
        os.system('git add --all')
        os.system('git commit -a -m "%s"' % commit_msg)
        os.system('git push origin gh-pages:gh-pages')
        os.system('git push gitcafe gh-pages:gh-pages')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        deploy()
    else:
        print 'please use --auto flag.'

