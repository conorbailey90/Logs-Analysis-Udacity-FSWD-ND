# Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

This project is an internal reporting tool which uses information from a large database containing data from a news website. The tool is written in Python and it utilizes the `psycopg2` module to connect to and fetch data from the postgresql database. The tool is used to print reports for the following queries in plain text format:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Installation

It is recommended that you run this program using a virtual machine. We will be using VirtualBox and Vagrant.

### Install VirtualBox
[Virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) is the software that actually runs the virtual machine. You do not need to launch VirtualBox after installing it; Vagrant will do that.

### Install Vagrant

[Vagrant](https://www.vagrantup.com/) is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Install the version for your operating system.

### Github Repository Fork / Clone

Fork this repository in Github. Next, clone the repository in your terminal using the following command:

```
git clone https://github.com/conorbailey90/Logs-Analysis-Udacity-FSWD-ND.git
```

## Running The Program

1. Now that the project has been cloned to your local machine `cd` into the project directory in your terminal. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** subdirectory.

2. From your terminal, inside the **Vagrant** subdirectory, run the command `vagrant up`. This will cause Vagrant to download and install the Linux operating system. This may take a few minutes depending on your internet connection speed.

3. When `Vagrant up` is finished running, you will get your shell prompt back. Next run `vagrant ssh` to log in to your newly installed linux virtual machine. 

4. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should the be placed inside the above mentioned Vagrant directory.

5. From your terminal, load up the database using the folling command line: `psql -d news -f newsdata.sql`.

6. Next, connect to the database using the following command line: `psql news`.

7. Create the Views listed below below. Then exit `psql` using the `\q` command.

8. Finally, run the logs_analysis.py file using the following command line: `python logs_analysis.py`.


## Views used for Query 3 in the program:

```
CREATE VIEW logs AS 
SELECT to_char(time, 'DD-MM-YYYY') as Date, count(*) as LogsCount
FROM log
GROUP BY Date;
```
```
CREATE VIEW errorcount AS
SELECT to_char(time, 'DD-MM-YYYY') as Date, count(*) as errors
FROM log
WHERE status != '200 OK'
GROUP BY Date;
```