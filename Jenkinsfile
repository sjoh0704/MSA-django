pipeline {
    agent any

    stages{
        stage("clone"){
            steps {
                echo "clone start!!!!!!!!"
                checkout scm
            }
        }
        stage("image build"){
            steps {
                echo "building!!!!"
    
                sh 'docker build -t testimage front/.'
                sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:latest'
            }
        }
    
    stage("image push"){
            steps {
                echo "pushing!!"
                sh 'rm  ~/.dockercfg || true'
                sh 'rm ~/.docker/config.json || true'
         
             docker.withRegistry('https://752943197678.dkr.ecr.ap-northeast-2.amazonaws.com', 'hanium0119-aws-crediential') {
             /* app.push("${env.BUILD_NUMBER}")
             app.push("latest") */

            }
        }

    stage("deploy"){
            steps {
                echo "deploy!!"
            }
        }
    
    }
}
