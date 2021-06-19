node {


    stage("clone"){
  
        echo "clone start!!!!!!!!"
        checkout scm
   
    }
    dir('front'){
        stage("image build"){
            
            echo "building!!!!"

            sh 'docker build -t testimage .'
            sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:$BUILD_NUMBER'
            
    }

    }
    

    stage("image push"){
      
        echo "pushing!!"
        sh 'aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com'
        sh 'docker push 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:$BUILD_NUMBER'
 
    }

    stage("deploy"){
    
        echo "deploy!!"
   
    }

}
