# Processes and Signals 
> in GNU/Linux <br/>
> **Processes** and **signals** allow programs to communicate with each other and the **operating system** itself.

<div align="center">
 <img src="./gnu_linux/gnu.svg" width="150" height="150" />
 <img src="./gnu_linux/linux.svg" width="150" height="150" />
</div>

---
## Processes
A `process` is an *instance of a program that is currently running* on the system. Each process has a unique identifier called a process ID - `PID` that is used to manage and monitor the process. To view a list of currently running processes, you can use the `ps`/`top`/`pstree` commands with options.

```bash
# ps command
ps -aux
```
> this will display a list of all processes running on the system, including their PIDs, user, CPU and memory usage, and other details.


```bash
# top command
top
```
> view a dynamic, real-time list of processes sorted by CPU usage

To terminate a process, you can use the `kill` command with the PID of the process and the signal to send. For example, to terminate a process with PID 1234, you can use:

```bash
# kill command
kill 1234
# or `kill -9 1234` to forcibly terminate
```
> this will send the default signal `SIGTERM` (termination signal) to the process, requesting that it terminate gracefully. if the process does not respond to SIGTERM, you can send a `SIGKILL` (kill signal) to forcefully terminate the process.

---
## `process` Signals
> system-specific signals: `man 7 signal`, **system library** `signal.h`

`Signals` are ***software interrupts*** that are sent to processes to notify them of an event or to request a specific action. There are a number of `standard signals`/posix in GNU/Linux. Examples:

| Signal   | Description                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------- |
| SIGINT   | Interrupt signal, usually sent by the user pressing Ctrl+C on the command line.                         |
| SIGTERM  | Termination signal, used to request that a process terminate gracefully.                                 |
| SIGKILL  | Kill signal, used to forcefully terminate a process.                                                    |
| SIGHUP   | Hang-up signal, usually used to notify a process that the controlling terminal has been closed.          |
| SIGSTOP  | Stop signal, used to suspend a process temporarily.                                                      |
| SIGCONT  | Continue signal, used to resume a suspended process.                                                     |


---
## Signal Handlers - `trap`
Processes can also handle signals by registering signal handlers. A signal handler is a function that is called when a specific signal is received by the process. The signal handler can then perform a specific action or ignore the signal.

Here's an example shell script that registers a signal handler for the `SIGINT` signal and prints a message when the signal is received:

```bash
#!/bin/bash

function handle_sigint {
    echo "Received SIGINT signal"
}

trap handle_sigint INT

while true; do
    echo "Press Ctrl+C to send SIGINT signal"
    sleep 1
done
```
> (script) the `trap` command is used to register the `handle_sigint` **function** as the signal handler for SIGINT. a **while loop** is used to keep the script running until a signal is received. when the script is run, it will print a message every second, and you can send a SIGINT signal by pressing `Ctrl+C`. when the signal is received, the `handle_sigint` function will be called and print a message to the console.