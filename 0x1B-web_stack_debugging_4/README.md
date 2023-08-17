# Web-stack Debugging

> `Series #4`  
> **Note**  
> Builds up on:  
>> [0x0D-web_stack_debugging_0](../0x0D-web_stack_debugging_0)  
>> [0x0E-web_stack_debugging_1](../0x0E-web_stack_debugging_1)  
>> [0x12-web_stack_debugging_2](../0x12-web_stack_debugging_2)  
>> [0x17-web_stack_debugging_3](../0x17-web_stack_debugging_3)  


In this debugging series, broken/bugged webstacks are assessed. The motivation is to come up with Bash/Puppet scripts that once executed, will bring the webstacks to a working state.

Web stack debugging involves identifying and resolving errors, performance bottlenecks, and misconfigurations in the components that make up a web application's infrastructure. You can get useful info from logs, and shell commands meant to analyze server state, system status, appliaction status etc.

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information.  

In this context, we're testing how well a Nginx web server setup is doing under pressure - we are getting a huge amount of failed requests. We'll fix the rate limit/failed requests problem. And we'll fix some `OS` and UNIX user related problems as well.
