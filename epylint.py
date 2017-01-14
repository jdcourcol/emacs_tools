#!/usr/bin/env python
''' pylint wrapper for emacs '''
import re
import sys
import subprocess

p = subprocess.Popen("%s/bin/pylint -f parseable -d I0011 --rcfile=%s -r n  %s" %
                     (sys.argv[3], sys.argv[2], sys.argv[1]), shell=True, stdout=subprocess.PIPE).stdout
for line in p:
    match = re.search("\\[([WE])(, (.+?))?\\]", line)
    if match:
        kind = match.group(1)
        func = match.group(3)

        if kind == "W":
            msg = "Warning"
        else:
            msg = "Error"

        if func:
            line = re.sub("\\[([WE])(, (.+?))?\\]",
                          "%s (%s):" % (msg, func), line)
        else:
            line = re.sub("\\[([WE])?\\]", "%s:" % msg, line)
    print line,

p.close()
