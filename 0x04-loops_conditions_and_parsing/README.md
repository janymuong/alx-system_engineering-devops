## `bash` - Loops, conditions and parsing

> `loops`, `conditions`, `parsing`, `shell scripting`

### Loops:
In programming, loops are used to repeat a set of instructions *multiple times until a particular condition is met*. In GNU/Linux, there are various types of loops used in *scripting*, such as `for loop`, `while loop`, and `until loop`.
For example, a "**for**" loop in **GNU/Linux** is used to iterate over a series of **values**, such as a list of files, and perform the same set of instructions on each value. Here's an example of a for loop in bash:
```bash
for file in *.txt
do
    echo "Processing $file"
    # more instructions here
done
```
This loop will iterate over all the files in the current directory that have the ".txt" extension and print a message for each file.


### Conditions:
In `GNU/Linux programming`, `conditions` are used to perform actions based on a particular condition being `true` or `false`. The most commonly used conditionals in **GNU/Linux scripting** are `if` statements and `case` statements.
For example, an "**if**" statement in bash can be used to check if a particular file exists and perform different actions based on whether or not it does. Example:
```bash
if [ -f myfile.txt ]
then
    echo "myfile.txt exists"
else
    echo "myfile.txt does not exist"
fi
```
This script checks if the file "myfile.txt" exists in the current directory and prints a message based on the result.


### Parsing:
Parsing refers to the process of analyzing a `string` of **text** or **data** and breaking it down into its constituent parts. In `GNU/Linux`, parsing is often used to *extract* information from **command output** or **configuration files**.
For example, the "grep" command in **GNU/Linux** can be used to search for a specific pattern in a file or output.

Here's an example:
```bash
$ ps aux | grep nginx
root      2345  0.0  0.1  12345  6789 ?        Ss   Mar01   0:00 nginx: master process /usr/sbin/nginx
www-data  3456  0.0  0.2  23456  7890 ?        S    Mar01   0:01 nginx: worker process
```
This command searches for the pattern "nginx" in the output of the "ps aux" command, which lists all the running processes on the system. Pipe into the `grep` program. The output shows two processes related to nginx, along with their process IDs and other information.

---
<div aligin="center">
 <img src="./img/such_awk.jpg" />
</div>
