# Shell, I/O Redirections and Filters

This project focuses on `I/O redirections` and f`ilters` in Bash. It covers topics such as redirecting standard input/output, combining commands with filters, and utilizing special characters. Meant to enhance knowledge of shell scripting techniques for efficient input/output manipulation and filtering.

## About:

| Premise                                                |
|-------------------------------------------------------------------|
| Redirect standard input and output to files                        |
| Get input from files instead of the keyboard                       |
| Chain commands together, utilizing the output of one command as the input for another |
| Employ filters to process and manipulate data                      |
| Understand and utilize special characters for effective command execution |


## Usage

1. **Redirecting Output to a File**

```bash
#!/bin/bash
echo "Hello, World!" > output.txt
```

The `echo` command outputs 'Hello, World!' text to the file `output.txt` using redirection.

2. **Reading Input from a File**

```bash
#!/bin/bash
while read -r line; do
    echo "Line: $line"
done < input.txt
```

This script reads input from the file `input.txt` line by line using the `<` redirection and then echoes each line with a prefix.

3. **Chaining Commands with Filters**

```bash
#!/bin/bash
cat file.txt | grep "keyword" | sort | uniq > output.txt
```

Here, the `cat` command reads the contents of `file.txt`, which is then piped to `grep` for filtering lines containing the keyword. The resulting output is sorted using `sort` and passed to `uniq` to remove duplicate lines. Finally, the output is redirected to `output.txt`.
