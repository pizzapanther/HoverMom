#!/usr/bin/env python

import os
import socket
import subprocess

def run_gae ():
  mydir = os.path.dirname(__file__)
  basedir = os.path.join(mydir, '..')
  os.chdir(basedir)
  
  kwargs = {
    'host': socket.getfqdn(),
    'sdk': '~/lib/google_appengine/'
  }
  cmd = "{sdk}dev_appserver.py --enable_sendmail --host {host} --port 8080 --admin_host {host} --admin_port 8888 hovermom/".format(**kwargs)
  status = subprocess.call(cmd, shell=True)
  
if __name__ == "__main__":
  run_gae()
  