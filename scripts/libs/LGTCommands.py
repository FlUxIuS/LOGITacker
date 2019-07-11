# -*- coding: utf-8 -*-
from __future__ import print_function
import serial

#
# LOGITacker commands helper by @FlUxIuS
#

class LGTCommands(object):
    _ser = None

    def __init__(self, tty):
        self._ser = serial.Serial(tty)        
    
    def __cleanline(self):
        """
            Cleaning command prompt from bad characters in the beginning
        """
        self._ser.write("\n")

    def __output(self, tto="", tfrom="", _stdout=False):
        """
            Manage serial output and text return
            in(1) tto: String start of text to output (default => empty to print all from the beginning)
            in(2) tfrom: String to end printing (default => empty => no end)
            out: String to output
        """
        stop = False
        startprint = False
        str_out = ""
        while stop is False:
            line = self._ser.readline()
            if tfrom is not None and tto is not None:
                if tfrom in line:
                    startprint = True
            elif tfrom is None:
                startprint = True
            if tto != "" and tto in line:
                stop = True
            if startprint is True:
                str_out += line
                if _stdout is True:
                    print (str_out)
        return str_out

    def executeCommand(self, string, output=False, tto="", tfrom=""):
        """
            in(1): String command to type
            in(2..4): see at __output
            out: String output of the command if needed
        """
        self.__cleanline()
        self._ser.write(string+"\n")
        if output is True:
            return self.__output(tto, tfrom)

    def close(self):
        self._ser.close()

if __name__ == "__main__":
    c = LGTCommands("/dev/ttyACM1")
    c.executeCommand("script show", output=True, tfrom="script start", tto="script end")
    c.close()
