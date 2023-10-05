#!/usr/bin/python3
"""Fabric script to clean archives"""

from fabric.api import run, env, lcd
from fabric.operations import put, local
from datetime import datetime
import os

env.hosts = ['18.210.18.151', '54.157.150.240']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your server username

def do_clean(number=0):
    """Clean up old archives"""
    try:
        number = int(number)
        if number < 0:
            number = 0

        # Clean local archives
        local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))

        # Clean remote archives
        archives = run("ls -1t /data/web_static/releases/").split()
        archives_to_keep = archives[:number + 1]
        for archive in archives:
            if archive not in archives_to_keep:
                run("rm -rf /data/web_static/releases/{}".format(archive))
        return True
    except Exception:
        return False

if __name__ == "__main__":
    execute(do_clean)

