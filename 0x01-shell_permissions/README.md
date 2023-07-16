# Shell Permissions

> Shell permission theory, and bash scripting

This project focuses on shell scripting and understanding file permissions in the context of Bash. It covers *managing permissions, changing ownership* and *group*, and *running commands with root privileges*. The project aims to enhance your knowledge of Linux file permissions and user management.

`Usage in Bash :`

1. **Change Permission**: A script to change the permissions of a file to read, write, and execute for the owner, read-only for the group, and no permissions for others.

```bash
#!/bin/bash
chmod 750 file.txt
```

2. **Create User**: A script to create a new user with specified username and home directory.

```bash
#!/bin/bash
useradd -m -d /home/newuser -s /bin/bash newuser
```

3. **Run Command with Root Privileges**: A script to execute a command with root privileges using `sudo`.

```bash
#!/bin/bash
sudo apt-get update
```
