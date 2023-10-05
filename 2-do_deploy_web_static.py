#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run, local
from os.path import exists
import os

env.hosts = ['18.210.18.151', '54.157.150.240']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your server username

def do_deploy(archive_path):
    """Distribute and deploy the archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_no_ext = archive_name.split('.')[0]

        # Upload the archive to /tmp/
        put(archive_path, "/tmp/{}".format(archive_name))

        # Create a folder for the archive on the server
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_name, archive_no_ext))

        # Delete the archive from /tmp/
        run("rm /tmp/{}".format(archive_name))

        # Move the contents to the current symlink
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_no_ext, archive_no_ext))

        # Remove the empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))

        # Update the symbolic link
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_no_ext))

        return True
    except Exception:
        return False

