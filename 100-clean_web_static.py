#!/usr/bin/python3
"""Delete outdated archives and keeps the specified number"""
from fabric.api import local, env, run, lcd
import os
env.hosts = ['18.235.243.105', '34.203.38.189']


def do_clean(number=0):
    """Delete outdated archives"""
    if int(number) < 1:
        number = 1
    number = int(number) + 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number))
