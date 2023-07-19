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
This project aims to manage database `backups` and `replicas` for `MySQL` database management system. It provides shell scripts/configuration files to create and maintain database backups, set up and manage database replicas, and ensure data availability and integrity.

### Source-Replica Background:
`Replication` involves the source database writing down every change made to the data held within one or more databases in a special file known as the *binary log*. Once the replica instance has been initialized, it creates two threaded processes. The first, called the `IO thread`, connects to the source MySQL instance and reads the binary log events line by line, and then copies them over to a local file on the replica’s server called the `relay log`. The second thread, called the `SQL thread`, reads events from the `relay log` and then applies them to the replica instance as fast as possible.

Recent versions of MySQL support two methods for replicating data. The difference between these replication methods has to do with how replicas track which database events from the source they’ve already processed.

MySQL refers to its traditional replication method as `binary log file position-based replication.` When you turn a MySQL instance into a replica using this method, you must provide it with a set of *binary log coordinates*. These consist of the name of the binary log file on the source which the replica must read and a specific position within that file which represents the first database event the replica should copy to its own MySQL instance.

These coordinates are important since replicas receive a copy of their source’s entire binary log and, without the right coordinates, they will begin replicating every database event recorded within it. This can lead to problems if you only want to replicate data after a certain point in time or only want to replicate a subset of the source’s data.

Binary log file position-based replication is viable for many use cases, but this method can become clunky in more complex setups. This led to the development of MySQL’s *newer native replication method*, which is sometimes referred to as `transaction-based replication`. This method involves creating a `global transaction identifier `**(GTID)** for each transaction — or, an isolated piece of work performed by a database — that the source MySQL instance executes.

The mechanics of transaction-based replication are similar to binary log file-based replication: whenever a database transaction occurs on the source, MySQL assigns and records a GTID for the transaction in the binary log file along with the transaction itself. The GTID and the transaction are then transmitted to the source’s replicas for them to process.

MySQL’s transaction-based replication has a number of benefits over its traditional replication method. For example, because both a `source` and its `replicas` preserve GTIDs, if either the source or a replica encounter a transaction with a GTID that they have processed before they will skip that transaction. This helps to ensure consistency between the source and its replicas. Additionally, with transaction-based replication replicas don’t need to know the binary log coordinates of the next database event to process. This means that starting new replicas or changing the order of replicas in a replication chain is far less complicated.


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

2. `4-mysql_configuration_primary, 4-mysql_configuration_replica` - these MySQL config files set up a database source main dbms and replica on a designated server. They configure the replication process to keep the replica in sync with the primary database.

## Usage
```bash
    - Ensure you have the required permissions to execute Bash scripts - `chmod +x filename` on each script.
    - Modify the server information and configuration variables within the config files according to your environment.
    - Run the scripts/modify `/etc/mysql/mysql.conf.d/mysqld.cnf` in the order necessary to achieve your desired database backup and replica setup.
```

```bash
# run SQL scripts in command-line like this:
cat prep_replica | mysql -hlocalhost -uroot -p
```

---
## Specific Source-Replica Setup:
### Helper Scripts:
> view replica_user, source_replica, prep_replica My`SQL` files for creating db users, creating source db; and populating the db with some records.  

### Replication:
`config files`:
SSH into each server and edit the configuration files. 
```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
> Ascertain you comment out the bind address directive.  
> Edit and save `.cnf` files so that [mysqld] section looks like this. Save and restart MySQL server in each case.
```bash
# web 1:  /etc/mysql/mysql.conf.d/mysqld.cnf:

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
server-id       = 1
log_bin         = /var/log/mysql/mysql-bin.log
binlog_do_db    = tyrell_corp

# web 2: /etc/mysql/mysql.conf.d/mysqld.cnf: 
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
server-id       = 2
log_bin         = /var/log/mysql/mysql-bin.log
relay_log       = /var/log/mysql/mysql-relay-bin.log
```
- SSH into Server 1:

```bash
# web 01:
$ ssh ubuntu@web-01-IP
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1021-aws x86_64)
...
*** System restart required ***
Last login: Tue Jul 18 21:37:49 2023 from 41.90.66.13
$
```

- Check for the status of db, and table like this(You created db `tyrell_corp` and added rows to the `nexus6` table)
> View the records in MySQL shell:

```bash
$ mysql -uroot -pyour_passwd -e "use tyrell_corp; select * from nexus6"
mysql: [Warning] Using a password on the command line interface can be insecure.
+----+----------+
| id | name     |
+----+----------+
|  1 | Mikasa   |
|  2 | Ackerman |
|  3 | Goku     |
|  4 | Ymir     |
+----+----------+
$
```

- Show status of main db (the db to replicate):  
> NOte the `MASTER_LOG_FILE` and the Position Values. You will use them in the later stage.
```bash
$ mysql -uroot -pyour-passwd
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 360
Server version: 5.7.42-log MySQL Community Server (GPL)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show master status;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      433 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

