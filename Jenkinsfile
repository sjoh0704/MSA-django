pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                git "https://gitlab.com/sjoh0704/MSA-django.git"
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
