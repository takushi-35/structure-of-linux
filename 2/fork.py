#!/usr/bin/python3

import os, sys
#親プロセスの時は子プロセスのプロセスIDが返却される。子プロセスの場合は０が返却
ret = os.fork()

if ret == 0:
    print("子プロセス:pid={}, 親プロセスのPid{}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
          print("親プロセス:pid={}, 子プロセスのpid={}".format(os.getpid(), ret))
          exit()
sys.exit(1)
