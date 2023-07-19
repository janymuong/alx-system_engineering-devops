# MySQL: Database Backup and Replication

<div align="center">
    <img src="./img/stuff_gif.gif" height="300" width="700" />
</div>

---
## Jump To:
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Servers Information](#server-requirements-information)
- [Scripts Description](#scripts-info)
- [Usage](#usage)


## Project Overview
This project aims to manage database `backups` and `replicas` for `MySQL` database management system. It provides shell scripts to create and maintain database backups, set up and manage database replicas, and ensure data availability and integrity.

### Source-Replica Background:
`Replication` involves the source database writing down every change made to the data held within one or more databases in a special file known as the *binary log*. Once the replica instance has been initialized, it creates two threaded processes. The first, called the `IO thread`, connects to the source MySQL instance and reads the binary log events line by line, and then copies them over to a local file on the replica’s server called the `relay log`. The second thread, called the `SQL thread`, reads events from the `relay log` and then applies them to the replica instance as fast as possible.

Recent versions of MySQL support two methods for replicating data. The difference between these replication methods has to do with how replicas track which database events from the source they’ve already processed.

MySQL refers to its traditional replication method as binary log file position-based replication. When you turn a MySQL instance into a replica using this method, you must provide it with a set of binary log coordinates. These consist of the name of the binary log file on the source which the replica must read and a specific position within that file which represents the first database event the replica should copy to its own MySQL instance.

These coordinates are important since replicas receive a copy of their source’s entire binary log and, without the right coordinates, they will begin replicating every database event recorded within it. This can lead to problems if you only want to replicate data after a certain point in time or only want to replicate a subset of the source’s data.

Binary log file position-based replication is viable for many use cases, but this method can become clunky in more complex setups. This led to the development of MySQL’s newer native replication method, which is sometimes referred to as transaction-based replication. This method involves creating a global transaction identifier (GTID) for each transaction — or, an isolated piece of work performed by a database — that the source MySQL instance executes.

The mechanics of transaction-based replication are similar to binary log file-based replication: whenever a database transaction occurs on the source, MySQL assigns and records a GTID for the transaction in the binary log file along with the transaction itself. The GTID and the transaction are then transmitted to the source’s replicas for them to process.

MySQL’s transaction-based replication has a number of benefits over its traditional replication method. For example, because both a source and its replicas preserve GTIDs, if either the source or a replica encounter a transaction with a GTID that they have processed before they will skip that transaction. This helps to ensure consistency between the source and its replicas. Additionally, with transaction-based replication replicas don’t need to know the binary log coordinates of the next database event to process. This means that starting new replicas or changing the order of replicas in a replication chain is far less complicated.


## Learning Objectives
- The main role of a database and its significance in software applications.
- What a database replica is and its purpose in achieving high availability and fault tolerance.
- The importance of storing database backups in different physical locations for disaster recovery.
- The regular operation to verify the effectiveness of your database backup strategy.

## Server Requirements Information
The following servers running on `Ubuntu 20.04 LTS` are available for use in this project.

| Name           | Username | IP              | State    |
|----------------|----------|-----------------|----------|
| SOME-ID-web-01  | ubuntu   | SERVER_IP    | running  |
| SOME-ID-web-02  | ubuntu   | SERVER_IP  | running  |
| SOME-ID-lb-01   | ubuntu   | SERVER_IP   | running  |

## Scripts Info:
1. `5-mysql_backup` - this script creates a backup of the MySQL database and stores it in a specified directory. It ensures that the backup strategy is working effectively and that the data can be restored if needed.

2. `4-mysql_configuration_primary, 4-mysql_configuration_replica` - this script sets up a database main dbms and replica on a designated server. It configures the replication process to keep the replica in sync with the primary database.

## Usage
```bash
    - Ensure you have the required permissions to execute Bash scripts - `chmod +x filename` on each script.
    - Modify the server information and configuration variables within the scripts according to your environment.
    - Run the scripts in the order necessary to achieve your desired database backup and replica setup.
```

```bash
# run SQL scripts in command-line like this:
cat prep_replica | mysql -hlocalhost -uroot -p
```
