pipeline {
  agent any
  environment {
    IMAGE_NAME = "my_flask_app"
    IMAGE_TAG = "${env.BUILD_NUMBER ?: 'dev'}"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Run Tests') {
      steps {
        bat 'pip install -r requirements.txt'
        bat 'pytest -v'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
        }
      }
    }
    stage('Run Container (smoke test)') {
      steps {
        bat """
          docker run --rm -d -p 5000:5000 --name test_container ${IMAGE_NAME}:${IMAGE_TAG}
          sleep 5
          curl -fsS http://localhost:5000/
          docker stop test_container
        """
      }
    }
  }
  post {
    always {
      cleanWs()
    }
  }
}
