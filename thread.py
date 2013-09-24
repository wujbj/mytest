#!/usr/bin/env python

import os
import threading

class CreateServer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.out = []

    def run(self):
        pipe = os.popen("ls")
        self.out = pipe.readlines()

    def stop(self):
        return self.out


t1 = CreateServer(1)
t2 = CreateServer(2)
t1.start()
t2.start()
t1.join()
t2.join()
print t1.stop()
print t2.stop()
