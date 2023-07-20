# MySQL: Database Backup and Replication

<div align="center">
    <img src="./img/stuff_gif.gif" height="300" width="700" />
</div>

---
## Contents:
- [Source-Replica Background:](#source-replica-background)
- [Learning Objectives](#learning-objectives)
- [Servers Information](#server-requirements-information)
- [Scripts Description](#scripts-info)
- [Usage](#usage)
- [Jump To Replication](#replication)
- [MySQL Insatllation](#appendix)


## Project Overview
This project aims to manage database `backups` and `replicas` for `MySQL` database management system. It provides shell scripts/configuration files to create and maintain database backups, set up and manage database replicas, and ensure data availability and integrity.

### Source-Replica Background:
`Replication` involves the source database writing down every change made to the data held within one or more databases in a special file known as the *binary log*. Once the replica instance has been initialized, it creates two threaded processes. The first, called the `IO thread`, connects to the source MySQL instance and reads the binary log events line by line, and then copies them over to a local file on the replica’s server called the `relay log`. The second thread, called the `SQL thread`, reads events from the `relay log` and then applies them to the replica instance as fast as possible.

Recent versions of MySQL support two methods for replicating data. The difference between these replication methods has to do with how replicas track which database events from the source they’ve already processed.

MySQL refers to its traditional replication method as `binary log file position-based replication.` When you turn a MySQL instance into a replica using this method, you must provide it with a set of *binary log coordinates*. These consist of the name of the binary log file on the source which the replica must read and a specific position within that file which represents the first database event the replica should copy to its own MySQL instance.

These coordinates are important since replicas receive a copy of their source’s entire binary log and, without the right coordinates, they will begin replicating every database event recorded within it. This can lead to problems if you only want to replicate data after a certain point in time or only want to replicate a subset of the source’s data.

Binary log file position-based replication is viable for many use cases, but this method can become clunky in more complex setups. This led to the development of MySQL’s *newer native replication method*, which is sometimes referred to as `transaction-based replication`. This method involves creating a `global transaction identifier `**(GTID)** for each transaction — or, an isolated piece of work performed by a database — that the source MySQL instance executes.

The mechanics of transaction-based replication are similar to binary log file-based replication: whenever a database transaction occurs on the source, MySQL assigns and records a GTID for the transaction in the binary log file along with the transaction itself. The GTID and the transaction are then transmitted to the source’s replicas for them to process.

MySQL’s transaction-based replication has a number of benefits over its traditional replication method. For example, because both a `source` and its `replicas` preserve GTIDs, if either the source or a replica encounter a transaction with a GTID that they have processed before they will skip that transaction. This helps to ensure consistency between the source and its replicas. Additionally, with *transaction-based replication* replicas don’t need to know the binary log coordinates of the next database event to process. This means that starting new replicas or changing the order of replicas in a replication chain is far less complicated.


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
> view [`replica_user`](./replica_user), [`source_replica`](./source_replica), [`prep_replica`](./prep_replica) **SQL** files for creating db users, creating source db; and populating the db with some records.  

### Firewall TCP rules:
> Configure ufw on server 1 to allow connection from server 2. This is required for the replication:
```bash
$ cat script_ufw.sh
#!/usr/bin/env bash
# run: sudo ./script_ufw.sh

# configure ufw - blocks all ingress, except these TCP ports:
#	22 (SSH), 443 (HTTPS SSL), 80 (HTTP) and MySQL port 3306

sudo apt-get update -y
sudo apt-get install -y ufw
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw allow 3306/tcp # or use: `sudo ufw allow from server2-IP-ADDRESS to any port 3306`
echo "yes" | sudo ufw enable
sudo ufw status
```


```bash
# web-01:
$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
3306                       ALLOW       Anywhere
3306                       ALLOW       Your-Server2-IP
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
443/tcp (v6)               ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
3306 (v6)                  ALLOW       Anywhere (v6)
```


### Replication:
`config files`:
SSH into each server and edit the configuration files. 
```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
> Ascertain you comment out the bind address directive.  
> Edit and save the `.cnf` files so that `[mysqld]` section looks like this. Save and ***restart MySQL server*** in each case.
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
# web 01
$ mysql -uroot -punix-xkcdnotserious -e "use tyrell_corp; select * from nexus6"
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
> NOte the `MASTER_LOG_FILE` and the `Position` Values. You will use them in the later stage.
```bash
$ mysql -uroot -punix-xkcdnotserious
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
```


- SSH into Server 2:

```bash
# web 02
$ ssh ubuntu@web-02-IP
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1021-aws x86_64)
...
*** System restart required ***
Last login: Wed Jul 19 14:40:48 2023 from 41.90.66.13

# login as root MySQL server user:
$ mysql -uroot -punix-xkcdnotserious
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.7.42-log MySQL Community Server (GPL)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# create tyrell_corp and nexus6 table(empty) in MySQL shell:
mysql> CREATE DATABASE IF NOT EXISTS tyrell_corp;
...
mysql> CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (     id INT PRIMARY KEY AUTO_INCREMENT,     name VARCHAR(255) NOT NULL );
...
```

- Setup user `replica_user` to start replication

> Well, you have to remember you NOted the `MASTER_LOG_FILE` and the `Position` values from some step up here; you will use them now.

```bash
# web 02 MySQL shell:
mysql> CHANGE MASTER TO MASTER_HOST='add-web-01-IP', MASTER_USER='replica_user', MASTER_PASSWORD='replica_userpasswdxkcd', MASTER_LOG_FILE='mysql-bin.000002', MASTER_LOG_POS=435;
```

- Start Replication(still in mysql console):

```bash
mysql> start slave;
...

# show status use this to verify replication is working/running. observe especially `Slave_IO_Running` and `Slave_SQL_Running`
mysql> show slave status\g
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 54.196.27.23
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000002
          Read_Master_Log_Pos: 715
               Relay_Log_File: mysql-relay-bin.000002
                Relay_Log_Pos: 600
        Relay_Master_Log_File: mysql-bin.000002
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 715
              Relay_Log_Space: 807
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
                  Master_UUID: e9304182-256b-11ee-88db-0637a6795dad
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp:
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
1 row in set (0.01 sec)

mysql>
```

  

> SSH into server 1 again and add one more record to the table, and then SSH into server 2; see if the record is replicated in the replica table/db.  
> And that is how replication works, man :)

---
## ```APPENDIX```

### MySQL Installation Guide and Resource:

> This is a project on creating redundancy; replicas and backups of a MySQL dbms.

- Read through resources on: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication) to understand WHAT **RAID** IS.  

- Read through [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql) on Digital Ocean as well to understand replication and how to do a `source-replica` setup.


### Install MySQL 5.7.*
Read about *Signature Checking Using GnuPG* on this MySQL docs resources site: [https://dev.mysql.com/](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html).

Copy the key from there - it looks like this:
```bash
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.6
Comment: Hostname: pgp.mit.edu

mQINBGG4urcBEACrbsRa7tSSyxSfFkB+KXSbNM9rxYqoB78u107skReefq4/+Y72TpDvlDZL
mdv/lK0IpLa3bnvsM9IE1trNLrfi+JES62kaQ6hePPgn2RqxyIirt2seSi3Z3n3jlEg+mSdh
AvW+b+hFnqxo+TY0U+RBwDi4oO0YzHefkYPSmNPdlxRPQBMv4GPTNfxERx6XvVSPcL1+jQ4R
2cQFBryNhidBFIkoCOszjWhm+WnbURsLheBp757lqEyrpCufz77zlq2gEi+wtPHItfqsx3rz
...
sTSKHe+QnnnoFmu4gnmDU31i
=Xqbo
-----END PGP PUBLIC KEY BLOCK-----
```

```bash
# paste/save it in a file called signature.key:
$ cat > signagure.key # and paste
# CTRL + D
$
# or 
$ vi signature.key` # and paste/save
```

#### [How to] Install mysql 5.7.* - [resouce page](https://intranet.alxswe.com/concepts/100002):  

- The copied GPG key from the MySQL website, and asved to a file called `signature.key`, is used to verify the validity of the packages that are downloaded from the MySQL 5.7 `apt` repo.

```bash
sudo apt-key add signature.key
```

> Info on Subsequent Lines Below:  
>> You add the MySQL 5.7 repository to the list of repositories that Ubuntu uses to find software. This is done by creating a new file called `mysql.list` in the directory `/etc/apt/sources.list.d/`. The file contains a line that specifies the URL of the ***MySQL 5.7 repository***. You update the list of repositories that Ubuntu uses to find software. This is done by running the apt-get update command.
You check the available versions of MySQL 5.7. This is done by running the `apt-cache policy mysql-server` command.
Install MySQL 5.7.* eventually. 

```bash
$ sudo apt-get update -y
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
$
$ sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```
> MySQL server setup wizard will display. Type and re-type a password for the `root` user (a MySQL user called **root**). Setup a password or blank.
