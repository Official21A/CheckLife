# CheckLife
A program to check a list of URL addresses and see if they are working correctly and neigher they are active connections or not.

# Introduction
This script is a consol program which can get internet domain names and check their activity, then it will show the results of requests.

It uses multithreading for having a better speed in long lists.

Also it has a timeout which you can set manually to put a limit time for requests in case of any delation.

# How it works
Simply run the program:
```

python3 script.py

```
For adding a new url:
```

python3 script.py -add "Domain Name"

```
For removing a url:
```

python3 script.py -rmv "Domain Name"

```
And for seeing all the existing urls:
```

python3 script.py -viw

```
# Tools
This program only needs python "requests" library. Other libraries in the program are installed in python standard libraries. Its a lightwight program
that can easily be change by you.

It stores data in a "DATA.sc" file. If you want you can manually edit the urls in that file (Which I don not recommend). And if you remove this file, program
will give you errors in executing.



Contact ma at : najafizadeh21@gmail.com or officialamirhossein21@gmail.com
