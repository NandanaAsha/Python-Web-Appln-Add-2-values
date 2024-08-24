pipeline {
    agent any
    
    environment {
        // Define any environment variables here if needed
    }
    
    stages {
        stage('Clone repo') {
            steps {
                // Checkout the source code from the repository
                git 'https://github.com/NandanaAsha/python-web-appln.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run tests if available, adjust as needed
                sh 'pytest'
            }
        }
        
        stage('Package Application') {
            steps {
                // Package the application into a zip file
                sh 'zip -r app.zip app.py'
            }
        }
    }
    
    post {
        always {
            // Archive the zip file as an artifact
            archiveArtifacts artifacts: 'app.zip', allowEmptyArchive: true
        }
        
        success {
            // Additional actions on success
            echo 'Build succeeded!'
        }
        
        failure {
            // Additional actions on failure
            echo 'Build failed!'
        }
    }
}
