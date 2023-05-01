# `GNU/Linux` programming and `Shell` Scripting


<div align="center">
 <img src="./0x05-processes_and_signals/gnu_linux/gnu.svg" width="150" height="150" />
 <img src="./0x05-processes_and_signals/gnu_linux/linux.svg" width="150" height="150" />
</div>


```bash
$ cat script.sh
#!/usr/bin/env bash

# bash: a script that prints directories
# 	one per line without duplicates
# 	that contain one or more files with a '`.tf`' extension.

find . -type f -name '*.tf' -printf '%h\n' | sort -u
$
```