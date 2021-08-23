## bork-sauls

**Flag: ctf{d8194ce78a6c555adae9c14fe56674e97ba1afd88609c99dcb95fc599dcbc9f5}**

I opened the file in Ghidra and saw that the file which contains the flag is
shown if -1 >= (int) (100000 + 1999999 * num_times_3_is_inputted).
Therefore I created the script [borksauls.py](borksauls.py) which generates a large number of
3s (2000) and I saved the output in [borksauls.txt](borksauls.txt):
```
cat borksauls.txt | nc 35.234.117.20 30158
```

[Back](../unbreakable.md)
