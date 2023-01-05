#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
import time
import os
from fabric.api import *
from fabric.operations import run, put

env.use_ssh_config = True
env.hosts = ['100.26.219.114', '35.175.129.54']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{:s}.tgz".\
            format(time.strftime("%Y%m%d%H%M%S"))
    except BaseException:
        return None


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        # Upload archive
        put(archive_path, '/tmp/')

        # Create a target dir without the file extension
        timestamp = time.strftime("%Y%m%d%H%M%S")
        run('mkdir -p /data/web_static/releases/web_static_{:s}/'.
            format(timestamp))

        # uncompress archive to the targed dir
        run('tar xzvf /tmp/web_static_{:s}.tgz --directory\
            /data/web_static/releases/web_static_{:s}/'.
            format(timestamp, timestamp))

        # delete the archive from the web server
        run('rm /tmp/web_static_{:s}.tgz'.format(timestamp))

        # move contents into host web_static
        run('mv /data/web_static/releases/web_static_{:s}/web_static/*\
            /data/web_static/releases/web_static_{}/'.format(
            timestamp, timestamp))

        # remove irrelevant web_static dir
        run('rm -rf /data/web_static/releases/web_static_{}/web_static'.
            format(timestamp))

        # delete the initial symbolic link from the web server
        run('rm -rf /data/web_static/current')

        # create a new symbolic link
        run('ln -s /data/web_static/releases/web_static_{:s}/ \
            /data/web_static/current'.format(
            timestamp))
    except BaseException:
        return False
    # if all that succeeded, return True
    return True
