# Web-stack Debugging

> `Series #2`  
> Builds up on:  
> [0x0D-web_stack_debugging_0](../0x0D-web_stack_debugging_0)  
> [0x0E-web_stack_debugging_1](../0x0E-web_stack_debugging_1)


In this debugging series, broken/bugged webstacks are assessed. The motivation is to come up with Bash scripts that once executed, will bring the webstacks to a working state.

Web stack debugging involves identifying and resolving errors, performance bottlenecks, and misconfigurations in the components that make up a web application's infrastructure. You can get useful info from logs, and shell commands meant to analyze server state, system status, appliaction status etc.

In this context, we're figuring out a way to run stuff under certain privileges:
- run Nginx as nginx
- run with `sudo` privileges etc
