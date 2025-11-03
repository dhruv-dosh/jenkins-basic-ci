pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "portfolio-site"
        CONTAINER_NAME = "portfolio-site-container"
        PORT = "5000"
    }
    
    stages {
        stage("Clone Code") {
            steps {
                echo "🔁 Cloning the code from GitHub..."
                git branch: "main", url: "https://github.com/dhruv-dosh/jenkins-basic-ci"
            }
        }
        
        stage("Clean Old Containers & Images") {
            steps {
                echo "🧹 Removing old containers and images..."
                bat '''
                docker ps -q --filter "name=%CONTAINER_NAME%" > nul 2>&1 && docker stop %CONTAINER_NAME% || echo No running container
                docker ps -aq --filter "name=%CONTAINER_NAME%" > nul 2>&1 && docker rm %CONTAINER_NAME% || echo No container to remove
                docker images -q %IMAGE_NAME% > nul 2>&1 && docker rmi %IMAGE_NAME% || echo No image to remove
                '''
            }
        }
        
        stage("Build Docker Image") {
            steps {
                echo "⚙️ Building Docker image from portfolio-site folder..."
                bat "docker build -t %IMAGE_NAME%:latest ./portfolio-site"
            }
        }
        
        stage("Deploy Container") {
            steps {
                echo "🚀 Deploying container..."
                bat "docker run -d --name %CONTAINER_NAME% -p %PORT%:5000 %IMAGE_NAME%:latest"
            }
        }
    }
    
    post {
        success {
            echo "✅ Deployment successful! Application is running at http://localhost:${PORT}"
        }
        failure {
            echo "❌ Deployment failed! Check Jenkins logs for details."
        }
    }
}