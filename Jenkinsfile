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
            }
        }
    
    stage("image push"){
            steps {
                echo "pushing!!"
                
            }
        }

    stage("deploy"){
            steps {
                echo "deploy!!"
            }
        }
    
    }
}
