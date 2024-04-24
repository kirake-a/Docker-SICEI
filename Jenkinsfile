pipeline {

    agent any 

    stages {
        stage('Downloading'){
            steps{
                echo 'hola'
            }
        }
        stage('Build'){
            steps{
                echo 'Build Docker image step started'
                sh 'sudo docker build -t sicei-${GIT_BRANCH}:1.1-${BUILD_NUMBER} .'
            }
        }
    }
}