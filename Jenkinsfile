pipeline {
    agent any

    environment {
        PROJECT_ID = "medicalchatbot-451208"
        REPO = "my-repo"
        IMAGE = "fastapi-app"
        REGION = "asia-south1"
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag $IMAGE $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([file(credentialsId: 'gcp-creds', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                    gcloud auth configure-docker $REGION-docker.pkg.dev
                    docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE
                    '''
                }
            }
        }
    }
}