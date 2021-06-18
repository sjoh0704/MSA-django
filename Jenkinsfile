pipeline {
    agent any

    stages{
        stage("start"){
            steps {
                cd ~
                git clone https://gitlab.com/sjoh0704/MSA-django.git
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
