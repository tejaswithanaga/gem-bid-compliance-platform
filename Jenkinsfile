
pipeline {
    agent any

    environment {
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

                    echo All required project files found successfully.
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building GeM Docker images'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml build

                    if errorlevel 1 (
                        echo ERROR: Docker image build failed
                        exit /b 1
                    )

                    echo Docker images built successfully.
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated verification tests'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml run --rm backend python -m pytest -v

                    if errorlevel 1 (
                        echo ERROR: Automated tests failed
                        exit /b 1
                    )

                    echo All automated tests passed successfully.
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Removing old containers and deploying the application'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml down --remove-orphans

                    docker rm -f bid-compliance-backend 2>NUL
                    docker rm -f bid-compliance-frontend 2>NUL

                    "%DOCKER_COMPOSE%" -f docker-compose.yml up -d --force-recreate

                    if errorlevel 1 (
                        echo ERROR: Application deployment failed
                        exit /b 1
                    )

                    echo Checking deployed containers

                    "%DOCKER_COMPOSE%" -f docker-compose.yml ps

                    if errorlevel 1 (
                        echo ERROR: Could not check container status
                        exit /b 1
                    )

                    echo Application deployment completed successfully.
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GeM application built, tested and deployed.'
            echo 'All pipeline stages completed successfully.'
        }

        failure {
            echo 'FAILED: Check Jenkins Console Output for details.'
        }

        always {
            echo 'GeM CI/CD pipeline execution completed.'
        }
    }
}
