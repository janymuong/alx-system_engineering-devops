# Basic `shell` Scripting

Example syntax: script.sh a bash script that prints directories, one per line without duplicates that contain one or more files with a '`.tf`' extension.
```bash
$ cat script.sh
#!/bin/bash
find . -type f -name '*.tf' -printf '%h\n' | sort -u
$
```