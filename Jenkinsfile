
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out GeM project from GitHub'

                checkout scm

                bat '''
                    if not exist backend\\app.py exit /b 1
                    if not exist backend\\verification.py exit /b 1
                    if not exist backend\\tests\\test_verification.py exit /b 1
                    if not exist frontend\\index.html exit /b 1
                    if not exist docker-compose.yml exit /b 1

                    echo All required project files found.
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building GeM Docker images'

                bat 'docker compose build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated pytest test cases'

                bat 'docker compose run --rm backend python -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying GeM application'

                bat 'docker compose up -d'

                bat 'docker compose ps'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GeM application built, tested and deployed.'
        }

        failure {
            echo 'FAILED: Check Jenkins Console Output.'
        }
    }
}
