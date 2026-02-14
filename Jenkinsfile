pipeline
{
    agent any

    stages {
        stage('git clone') {
            steps {
                echo 'git cloning...'
                // clone file from git hub
                git clone https://github.com/rakeshyadav1289/dummy.git
            }
        }
        stage('building image') {
            steps {
                echo 'building docker image.....'
                // build the docker images
                docker build -t python-app .
            }
        }
        stage('runing image...') {
            steps {
                echo 'Deploying...'
                // runing docker image
                docker run --rm python-app
              // list of docker images
                docker images
            }
        }
    }
}
