#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder"""

from datetime import datetime
from fabric.api import local as lcl

def do_pack():
    """Create a .tgz archive from web_static folder"""
    try:
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        lcl("mkdir -p versions")
        lcl("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None

