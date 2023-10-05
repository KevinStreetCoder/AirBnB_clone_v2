#!/usr/bin/python3
"""Fabric script for full deployment"""

from fabric.api import task, execute, env
from datetime import datetime
import os

env.hosts = ['18.210.18.151', '54.157.150.240']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your server username

@task
def deploy():
    """Full deployment of the web application"""
    try:
        archive_path = do_pack()
        if archive_path:
            result = do_deploy(archive_path)
            return result
        else:
            return False
    except Exception:
        return False

@task
def do_pack():
    """Create a .tgz archive from web_static folder"""
    try:
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        os.makedirs("versions", exist_ok=True)
        os.system("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None

@task
def do_deploy(archive_path):
    """Distribute and deploy the archive to web servers"""
    if not os.path.exists(archive_path):
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

if __name__ == "__main__":
    execute(deploy)

