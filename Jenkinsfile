pipeline {
    agent any

    environment {
        IMAGE_NAME = "my_flask_app:dev"
        CONTAINER_NAME = "flask_test_container"
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/Anasmataich/my_flask_app.git']]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${WORKSPACE}") {
                    bat """
                    python --version
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir("${WORKSPACE}") {
                    bat """
                    set PYTHONPATH=%CD%
                    python -m pytest -v
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORKSPACE}") {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Run Container (smoke test)') {
            steps {
                bat """
                docker run --rm -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%
                timeout /t 5 >NUL
                curl -fsS http://localhost:5000/
                docker stop %CONTAINER_NAME%
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
