pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                echo "clone start!!!!!!!!"
                sh 'rm -rf MSA-django || true'
                sh 'git clone https://github.com/sjoh0704/MSA-django.git'
                
            }
        }
        stage("image build"){
            steps {
                echo "building!!!!"
                sh 'docker build -t textimage MSA-django/front/.'
                sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:latest'
            }
        }
    
    stage("image push"){
            steps {
                echo "pushing!!"
                sh 'aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com'
            }
        }

    stage("deploy"){
            steps {
                echo "deploy!!"
            }
        }
    
    }
}
