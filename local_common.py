import sys, os
import time
import signal
import time
import params as pa

class Command(object):
    """Run a command and capture it's output string, error string and exit status"""
    def __init__(self, command):
        self.command = command
    def run(self, shell=True):
        import subprocess as sp
        process = sp.Popen(self.command, shell = shell, stdout = sp.PIPE, stderr = sp.PIPE)
        self.pid = process.pid
        self.output, self.error = process.communicate()
        self.failed = process.returncode
        return self
    @property
    def returncode(self):
        return self.failed

def signal_handler(signal, frame):
    pa.run
    print "exiting"
    pa.run = False

signal.signal(signal.SIGINT, signal_handler)

def fetch(os_type):
    if os_type is 'osx':
        #os.system('./shell/osxRSSI.sh') #mac osx
        com = Command("./shell/osxRSSI.sh").run()
        print 'in pyton' + com.output
        #print com.error
