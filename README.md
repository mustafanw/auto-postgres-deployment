# Automate Database Maintenance for Microservices with Jenkins
***This repository contains the code for maintaining the database script automatically with Jenkins for your microservices.***

**Status:** Ongoing

# Requirements
**1. Python 3.5 +**

**2. Jenkins**

Features
=========================

- Automatic execution of base schema DDL and DML scripts for defined microservices.
- Automatic execution of service version delta scripts.
- Notifying developer for failed query execution.
- Maintaining the service delta for reference and

Setup
=========================
-Take clone of this repository
```
git clone https://github.com/mustafanw/auto-postgres-deployment.git
```

-Define database configuration in config.ini file

```
[DATABASE_CONFIGS]
hostname = localhost
username = postgres
password = postgres
database = ecommerce
```
-Install Jenkins for pipeline creation

[Steps for Jenkins installation](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04)
