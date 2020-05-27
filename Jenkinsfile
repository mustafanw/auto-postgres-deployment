pipeline {

  agent any
  stages {
    stage('powershell') {
      steps {
                script {
                        withPythonEnv('python3'){
                      sh 'pip install psycopg2'
                      sh 'cd /home/ubuntuaiq/auto_postgres/auto-postgres-deployment && ./job.sh'
                        
                    }
                }
    }
	}
	}
	}
