#!/usr/bin/env python

import re
import os
from subprocess import check_output

os.chdir('/etc/ssh')

sshd_config = check_output(['sshd', '-T'])
with open('sshd_config', 'w') as fp:
    # Convert `usepam 1` to `usepam yes` because of this [bug][1].
    #
    # [1]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=767648
    usepam_pattern = re.compile('(?i)^(\s*usepam\s+)(.*)$')
    for line in sshd_config.splitlines():
        match = usepam_pattern.match(line)
        if match:
            usepam = match.group(2)
            if usepam == '1':
                usepam = 'yes'
            elif usepam == '0':
                usepam = 'no'
            line = usepam_pattern.sub(r'\1' + usepam, line)
        fp.write(line + os.linesep)
