pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                sh 'git clone https://github.com/sjoh0704/MSA-django.git'
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
