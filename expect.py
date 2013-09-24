#!/usr/bin/env python

import pexpect
import sys

cmd = "ssh -x -o StrictHostKeyChecking=no 192.168.23.101 ls"
child = pexpect.spawn(cmd)
child.expect('.ssword:*')
child.sendline('abc123')
child.expect(pexpect.EOF)
print child.before
