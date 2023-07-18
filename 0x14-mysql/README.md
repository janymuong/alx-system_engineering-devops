# MySQL: Database Backup and Replication

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Servers Information](#server-requirements-information)
- [Scripts Description](#scripts-info)
- [Usage](#usage)


## Project Overview
This project aims to manage database `backups` and `replicas` for `MySQL` database management system. It provides shell scripts to create and maintain database backups, set up and manage database replicas, and ensure data availability and integrity.

## Learning Objectives
- The main role of a database and its significance in software applications.
- What a database replica is and its purpose in achieving high availability and fault tolerance.
- The importance of storing database backups in different physical locations for disaster recovery.
- The regular operation to verify the effectiveness of your database backup strategy.

## Server Requirements Information:
The following servers running on `Ubuntu 20.04 LTS` are available for use in this project.

| Name           | Username | IP              | State    |
|----------------|----------|-----------------|----------|
| SOME-ID-web-01  | ubuntu   | SERVER_IP    | running  |
| SOME-ID-web-02  | ubuntu   | SERVER_IP  | running  |
| SOME-ID-lb-01   | ubuntu   | SERVER_IP   | running  |

## Scripts Info
1. `5-mysql_backup` - this script creates a backup of the MySQL database and stores it in a specified directory. It ensures that the backup strategy is working effectively and that the data can be restored if needed.

2. `4-mysql_configuration_primary, 4-mysql_configuration_replica` - this script sets up a database main dbms and replica on a designated server. It configures the replication process to keep the replica in sync with the primary database.

## Usage:
```bash
    - Ensure you have the required permissions to execute Bash scripts - `chmod +x filename` on each script.
    - Modify the server information and configuration variables within the scripts according to your environment.
    - Run the scripts in the order necessary to achieve your desired database backup and replica setup.
```
```bash
# run scripts in command-line like this:
./4-mysql_configuration_primary
```

----
<div align="center">
    <img src="./img/stuff_gif.gif" height="200" width="600" />
</div>