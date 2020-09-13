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
**Fork this repository and take clone.**
```
git clone https://github.com/mustafanw/auto-postgres-deployment.git
```

**Define database configuration in config.ini file**

```
[DATABASE_CONFIGS]
hostname = localhost
username = postgres
password = postgres
database = ecommerce
```
**Install Jenkins for pipeline creation**

[Steps for Jenkins installation](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04)

**Create below pipeline in Jenkins ( Replace the repository url with your forked repo)**
```
pipeline {
  agent any
  stages {
  stage('Cloning Git') {
      steps {
        git 'https://github.com/mustafanw/auto-postgres-deployment.git'
      }
    }
    stage('Run Script') {
      steps {
                script {
                        withPythonEnv('python3'){
                      sh 'pip install psycopg2'
                      sh './job.sh'
                    }
                }
    }
  }
  }
    }
 ```

**Follow below steps for setup**
- Create folder in root directory for all your micrtoservices.
- Create below four files inside each microservice folder  
      -DDL.sql --> file for (CREATE, DROP, RENAME, ALTER etc) statements.  
      -DML.sql --> file for ( UPDATE, INSERT, MERGE etc) statements.  
      -sprint_delta.sql --> You need to add all the delta scripts for the service version delta.  
      -service_delta.sql --> This file automatically tracks whole service delta scripts.  
      
*Refer account_service, shipping_service,inventory_service folder for above files*
- Define below four varibales in config.ini file
```
[EXECUTE_SCRIPTS]
type = base - You have to define "base" 0r "delta" in type file. "base" for executing DDL and DML scripts and "delta" for executing sprint_delta file.
services = account_service,inventory_service,shipping_service - You have to list down the service folders here for which database scripts needs to be executed.
account_service = 1.0 - Define the version number corresponding to the service code version on GIT
inventory_service = 1.0
shipping_service = 1.0
```
- Follow below steps for port forwarding to trigger local jenkins job if you don't have Jenkins public IP or DNS available.  
[Steps for port forwading](https://medium.com/@ganeshvelrajan/make-your-web-services-go-online-securely-in-less-than-5-minutes-ee0b304f88c7)

- Follow below steps for setting webhook on GIT to auto trigger jenkins job on every push  
[Set GIT Webhook](https://www.socketxp.com/webhookrelay/github-webhook-localhost-jenkins)

**Upcoming Features**
- Database Schema Backup.
- Database DML backup of all tables except operational table.

**Flow Diagram**

![alt text](https://user-images.githubusercontent.com/24622641/93015619-80bf8e80-f5d8-11ea-8aab-876e1f5ed90c.JPG)!


