pipeline {
    agent any

    environment {
        PROJECT_ID = "medicalchatbot-451208"
        REPO = "my-repo"
        IMAGE = "fastapi-app"
        REGION = "asia-south1"
        VM_IP = "34.47.232.9"
        VM_USER = "subhakshan"
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
                    gcloud auth configure-docker $REGION-docker.pkg.dev -q
                    docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE
                    '''
                }
            }
        }

        stage('Deploy on VM') {
            steps {
                sh '''
                ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no $VM_USER@$VM_IP << EOF
                docker pull $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE
                docker stop fastapi-container || true
                docker rm fastapi-container || true
                docker run -d -p 8000:8000 --name fastapi-container $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE
                EOF
                '''
            }
        }
    }
}