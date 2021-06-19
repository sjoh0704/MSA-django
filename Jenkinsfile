pipeline {
    agent any
    environment{
    IMAGE_NAME = 'test'
    }
    

    stages{
    
    stage("clone"){
        steps{
        echo "clone start!!!!!!!!"
        checkout scm
        echo "dfffff '${IMAGE_NAME}'"
        }

    }
    dir('front'){
        stage("image build"){
            steps{
            echo "building!!!!"
        
            sh 'docker build -t ${IMAGE_NAME} .'
            sh 'docker tag ${IMAGE_NAME}:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/${IMAGE_NAME}:$BUILD_NUMBER'
            }
            
            
    }

    }
    

    stage("image push"){
        steps{
             echo "pushing!!"
        sh 'aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com'
        sh 'docker push 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/${IMAGE_NAME}:$BUILD_NUMBER'
        }
       
 
    }

    stage("deploy"){
        steps{
        echo "deploy!!"
        }
      
   
        }

    }
    
}
