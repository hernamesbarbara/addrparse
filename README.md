# addrparse

Small command line program to parse email addresses for quick copy and paste.


```
$ addrparse "Austin Ogilvie <a@yhathq.com>"
a@yhathq.com

$ addrparse "Austin Ogilvie <a@yhathq.com>" -w
http://www.yhathq.com

$ addrparse "Austin Ogilvie <a@yhathq.com>" -A
{"website": "http://www.yhathq.com", "display_name": "Austin Ogilvie", "raw_input": "Austin Ogilvie <a@yhathq.com>", "mailbox": "A", "outfile": null, "iswebmail": "False", "validated": "True", "email": "a@yhathq.com"}

$ addrparse "Austin Ogilvie <a@yhathq.com>" -n
Austin Ogilvie
```
