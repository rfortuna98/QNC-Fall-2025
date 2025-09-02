Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #if 1000 people are tested, and 2% are correct positvies
... 1000*.02
20.0
>>> #than we have 20 correct postive cases
... #but if we have a 5% of false positive, then we have#
... 1000*(100-2)/100*.05
49.0
>>> #So out of the 1000 people, 69 will have a positve#
...        
... 49/(49+20)
0.7101449275362319
