# Shell, Init Files, Variables, and Expansions

> **About**:  
> *Init Files*, *Shell Variables*, and *Expansions* in `bash`.  
> It covers essential topics such as shell initialization files, variable management, expansions, shell arithmetic, and the alias command.

## Objectives

```bash
- Understand the role and functioning of shell initialization files, including `/etc/profile`, `/etc/profile.d`, and `~/.bashrc`.
- Distinguish between local and global variables and know how to create, update, and delete shell variables.
- Familiarize yourself with reserved variables like `HOME`, `PATH`, and `PS1` and comprehend their significance.
- Comprehend special parameters and the purpose of the special parameter `$?`.
- Master expansions, including their usage, the differences between single and double quotes, and how to perform command substitution.
- Perform shell arithmetic operations for mathematical computations.
- Create aliases, list existing aliases, and temporarily disable them.
```

## Usage

1. **Creating and Using Shell Variables**

```bash
#!/bin/bash
hello_world="Hello, World!"
echo $hello_world
```

2. **Expanding Variables in a Message**

```bash
#!/bin/bash
current_date=$(date +%Y-%m-%d)
echo "Today's date is $current_date"
```

3. **Aliasing**

Sample line syntax for an executable that aliases the command ```rm *``` to `ls`:

```bash
#!/bin/bash
alias ls="rm *"
```