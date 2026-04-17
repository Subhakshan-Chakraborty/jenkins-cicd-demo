pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop fastapi-container || true'
                sh 'docker rm fastapi-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8001:8000 --name fastapi-container fastapi-app'
            }
        }
    }
}