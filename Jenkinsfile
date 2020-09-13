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