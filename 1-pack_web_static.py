#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static"""


def do_pack():
    """Generates a .tgz archive"""
    from fabric.api import local
    from datetime import datetime

    local("mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(date)
    ret = local('tar -cvzf {} web_static'.format(path))
    if ret.succeeded:
        return path
    else:
        return None
