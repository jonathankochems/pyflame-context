# -*- coding: utf-8 -*-
"""pyflame-context.

Profile code with pyflame directly from code as a context manager.

Example:

        with pyflame("profile.svg", duration=360):
            for n in range(10000):
                # expensive loop body


"""
from contextlib import contextmanager

PYFLAME_PATH='/current/pyflame/src/pyflame'
FLAMEGRAPH_PATH='/current/FlameGraph/flamegraph.pl'

@contextmanager
def pyflame(output_file, duration = 10, pid = None):
    from subprocess import Popen , PIPE
    import os
    if pid is None:
        pid = os.getpid()
    f = open(output_file, "w")
    pyflame = Popen([PYFLAME_PATH, '-p', str(pid), '-s', str(duration)], stdout=PIPE)
    flame   = Popen([FLAMEGRAPH_PATH], stdin=pyflame.stdout, stdout=f)
    yield f
    ret_code = flame.wait()
    f.flush()
    f.close()

