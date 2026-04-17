pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git credentialsId: 'github-creds',
                    url: 'https://github.com/Subhakshan-Chakraborty/jenkins-cicd-demo.git'
            }
        }

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