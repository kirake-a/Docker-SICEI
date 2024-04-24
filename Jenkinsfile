pipeline {

    agent any 
    
    stages{
        stage('First step'){
            steps{
                echo 'hola'
            }
        }
        stage('Build'){
            steps{
                
                sh 'sudo docker build -t sicei-${GIT_BRANCH}:1.1-${BUILD_NUMBER} .'
            }
        }
    }
}