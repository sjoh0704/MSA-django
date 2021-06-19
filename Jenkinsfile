node {


    stage("clone"){
  
        echo "clone start!!!!!!!!"
        checkout scm
   
    }
    dir('front'){
        stage("image build"){
            
            echo "building!!!!"

            /* sh 'docker build -t testimage front/.'
            sh 'docker tag testimage:latest 752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test:latest' */
            app = docker.build("752943197678.dkr.ecr.ap-northeast-2.amazonaws.com/test")
    }

    }
    

    stage("image push"){
      
        echo "pushing!!"
    
        docker.withRegistry('https://752943197678.dkr.ecr.ap-northeast-2.amazonaws.com', 'hanium0119-aws-crediential'){
        app.push("${env.BUILD_NUMBER}")
        app.push("latest")
        }

             
    }

    stage("deploy"){
    
        echo "deploy!!"
   
    }

}
