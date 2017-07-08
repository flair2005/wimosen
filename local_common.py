import sys, os
import time
import signal
import time
import params as pa
import collections

class Command(object):
    """Run a command and capture it's output string, error string and exit status"""
    def __init__(self, command):
        self.command = command
    def run(self, shell=True):
        import subprocess as sp
        process = sp.Popen(self.command, shell = shell, stdout = sp.PIPE,
        stderr = sp.PIPE)
        self.pid = process.pid
        self.output, self.error = process.communicate()
        self.failed = process.returncode
        return self
    @property
    def returncode(self):
        return self.failed

def signal_handler(signal, frame):
    print "exiting"
    pa.run = False

signal.signal(signal.SIGINT, signal_handler)

class Sample(object):
    def __init__(self, id, rssi, label):
        self.id_ = id_
        self.rssi = rssi
        self.label = label

samples = []
id_ = 0

def fetch():
    if pa.os_type is 'osx':
        #os.system('./shell/osxRSSI.sh') #mac osx
        com = Command("./shell/osxRSSI.sh").run()
        rssi = com.output.replace('agrCtlRSSI:', '')
        label = 1;  #todo label generator
        global id_
        id_ = id_ + 1
        #print(id_)
        #print (len(samples))
        return Sample(int(id_), int(rssi), int(label))
