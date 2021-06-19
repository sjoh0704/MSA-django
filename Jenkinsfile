node {


    stage("clone"){
  
        echo "clone start!!!!!!!!"
        checkout scm
   
    }
    dir('front'){
        stage("image build"){
            
            echo "building!!!!"

            sh 'docker build -t testimage .'
            sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:{$BUILD_NUMBER}'
            /* app = docker.build("752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:$BUILD_NUMBER") */
    }

    }
    

    stage("image push"){
      
        echo "pushing!!"
    
        docker.withRegistry('https://752943197678.dkr.ecr.ap-northeast-2.amazonaws.com', 'hanium0119-aws-crediential')

             
    }

    stage("deploy"){
    
        echo "deploy!!"
   
    }

}
