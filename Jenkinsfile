pipeline {
    agent any

    stages {
        stage('Stop all previous container') {
            steps {
                echo 'Stoping all containers related to project'
                script {
                    sh 'sudo docker ps -a | grep sicei | awk \'{print $1}\' | xargs docker stop'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Build Docker image step started'
                sh 'sudo docker build -t sicei-${GIT_BRANCH}:1.1-${BUILD_NUMBER} .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy Docker image step started'
                sh "sudo docker run -d -p 8000:8000 --name sicei-${BUILD_NUMBER} sicei-${GIT_BRANCH}:1.1-${BUILD_NUMBER}"
            }
        }
    }
}
