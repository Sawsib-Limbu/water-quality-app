pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'python app.py &'
            }
        }
    }
}
