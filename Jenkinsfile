node {


    stage("clone"){
  
        echo "clone start!!!!!!!!"
        checkout scm
   
    }
    stage("image build"){
      
        echo "building!!!!"

        sh 'docker build -t testimage front/.'
        sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:latest'
   
    }

    stage("image push"){
      
        echo "pushing!!"
    
        docker.withRegistry('https://752943197678.dkr.ecr.ap-northeast-2.amazonaws.com', 'hanium0119-aws-crediential')

    }

    stage("deploy"){
    
        echo "deploy!!"
   
    }

}
