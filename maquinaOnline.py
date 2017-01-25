#!/usr/bin/env python

import subprocess
import os
with open(os.devnull, "wb") as limbo:
	for n in xrange(100, 199):
		ip="192.168.0.{0}".format(n)
		r=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
			stdout=limbo, stderr=limbo).wait()
		if r:
			print ip, "Off"
		else:
			print ip, "Online"

