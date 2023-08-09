# Webstack Monitoring
> Server Monitoring:  
> This project entails setting up server monitoring using *Datadog* for an Ubuntu 20.04 LTS server.

## Premise
`Server Monitoring` involves systematically tracking the performance, health, and availability of servers to ensure optimal functioning of applications and services. Monitoring servers provides insights into resource utilization, potential bottlenecks, security vulnerabilities, and overall system stability. It enables proactive issue detection, rapid troubleshooting, and effective capacity planning. You can get information from logs if in command-line.

### Datadog:
> Background:  

`Datadog` is a popular monitoring and analytics platform. It offers tools to collect, visualize, and analyze performance metrics, logs, and traces from servers, applications, and cloud services. We will install and integrate the Datadog Agent on an Ubuntu 20.04 LTS server, configure key metrics, and utilize application keys for secure access. This setup aids in real-time visibility, early anomaly detection, and efficient incident response, contributing to the reliability and performance optimization of the monitored server.


### WHAT Datadog API and Application Keys ARE:

In Datadog, both API keys and application keys are authentication mechanisms that allow you to interact with the Datadog API and access various features of the Datadog platform. They serve different purposes:

- `API Key`:
An API key is a unique identifier that grants access to the Datadog API. The API key is used to authenticate API requests made from scripts, applications, or tools that you use to interact programmatically with Datadog.
API keys are often used for automating tasks, integrating Datadog with other systems, retrieving data, and performing administrative tasks through the API.
When you make API requests, you typically include the API key as an authorization header or parameter to prove your identity and gain access to the API's functionalities.

- `Application Key`:
An application key is a token that is used to authenticate access to the Datadog UI and its features. It acts as a way to authenticate users and applications when interacting with the Datadog web interface.
Application keys are often used when you want to allow third-party applications or services to access your Datadog account's data without providing them with direct access to your account credentials.
By generating an application key, you can control the level of access the third-party application has to your Datadog account.



### Prerequisites

- A Datadog account (sign up at [https://www.datadoghq.com/](https://www.datadoghq.com/))
- Server


### Steps

1. **Sign Up for Datadog:**
   - Create a Datadog account on their website.
   - Use the US region [https://app.datadoghq.com](https://app.datadoghq.com) for signing up.

2. **Install Datadog Agent on Your Server:**
   - Log in to your Ubuntu 20.04 LTS server.
   - Run the following commands in your terminal:
   
     ```bash
     DD_API_KEY=YOUR_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"

     ```
     Replace `YOUR_API_KEY` with your Datadog API key.

3. **Start the Agent:**
   - After installation, start the Datadog Agent, if not started as part the setup, using:
   
     ```bash
     sudo systemctl start datadog-agent
     ```

4. **Enable Automatic Start on Boot:**
   - Enable the Datadog Agent to start on server boot:
   
     ```bash
     sudo systemctl enable datadog-agent
     ```

5. **Verify Host Visibility in Datadog:**
   - Log in to your Datadog account.
   - Navigate to "Infrastructure" to verify that your server is visible under the correct hostname.


6. **Create an Application Key:**
   - In Datadog, create an application key for authentication.
   - Lookup 'Application Key' if you cannot find it in the UI. Copy Key

7. **API Validation (Optional):**
   - You can use the provided API to validate server visibility:
   
     ```bash
     curl -X GET "https://api.datadoghq.com/api/v1/hosts/YOUR_HOSTNAME_HERE" -H "Content-Type: application/json" -H "DD-API-KEY: YOUR_API_KEY" -H "DD-APPLICATION-KEY: YOUR_APPLICATION_KEY_HERE"
     ```
     Replace placeholders with actual values.



### Reference:

For more detailed instructions, refer to the official Datadog documentation:
> View [Datadog Docs](https://docs.datadoghq.com/getting_started/)

