pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                echo "clone start!!!!!!!!"
                sh 'rm -rf MSA_django || true'
                sh 'git clone https://github.com/sjoh0704/MSA-django.git'
                sh 'docker build -t textimage MSA-django/front/.'
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
