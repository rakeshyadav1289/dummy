pipeline
{
    agent any

    stages {
        stage('git clone') {
            steps {
                echo 'git cloning...'
                // Add your build commands here
                git branch: 'main', url: 'https://github.com/rakeshyadav1289/dummy.git'

            }
        }
        stage('build') {
            steps {
                echo 'building...'
                // Add your build commands here
                sh 'docker build -t myapp:latest .'

            }
        }
        stage('runing image...') {
            steps {
                echo 'Deploying...'
                // Add your deploy commands here
                sh 'docker run --rm myapp'
                sh 'docker images'
            }
        }
        
    }
}
