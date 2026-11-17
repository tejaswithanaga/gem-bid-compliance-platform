
pipeline {
    agent any

    environment {
        DOCKER_EXE = 'C:\\Users\\nagat\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        DOCKER_COMPOSE = 'C:\\Users\\nagat\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker-compose.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking GeM application files'

                bat '''
                    if not exist backend\\app.py exit /b 1
                    if not exist backend\\verification.py exit /b 1
                    if not exist backend\\tests\\test_verification.py exit /b 1
                    if not exist backend\\requirements.txt exit /b 1
                    if not exist frontend\\index.html exit /b 1
                    if not exist docker-compose.yml exit /b 1

                    echo All required project files found.
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker images'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml build

                    if errorlevel 1 exit /b 1

                    echo Docker images built successfully.
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml run --rm backend python -m pytest -v

                    if errorlevel 1 exit /b 1

                    echo All 5 automated tests passed.
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stopping old application containers'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml down --remove-orphans

                    "%DOCKER_EXE%" rm -f bid-compliance-backend
                    "%DOCKER_EXE%" rm -f bid-compliance-frontend

                    echo Checking for remaining containers

                    "%DOCKER_EXE%" ps -a --filter "name=bid-compliance-backend"

                    echo Starting application

                    "%DOCKER_COMPOSE%" -f docker-compose.yml up -d --force-recreate

                    if errorlevel 1 (
                        echo ERROR: Deployment failed.
                        exit /b 1
                    )

                    echo Checking application status

                    "%DOCKER_COMPOSE%" -f docker-compose.yml ps

                    if errorlevel 1 exit /b 1

                    echo Deployment completed successfully.
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GeM application built, tested and deployed.'
        }

        failure {
            echo 'FAILED: Check the Console Output.'
        }

        always {
            echo 'GeM CI/CD pipeline execution completed.'
        }
    }
}
