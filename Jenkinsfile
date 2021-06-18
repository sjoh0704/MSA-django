pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                git 
                git credentialsId: 'gitlab',
                    url: 'https://github.com/sjoh0704/MSA-django.git'
            }
        }
        stage("stop"){
            steps {
                echo "start!!"
            }
        }
    
    stage("build"){
            steps {
                echo "build!!"
            }
        }

    stage("deploy"){
            steps {
                echo "deploy!!"
            }
        }
    
    }
}
