
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
                    if not exist backend\\app.py (
                        echo ERROR: backend/app.py not found
                        exit /b 1
                    )

                    if not exist backend\\verification.py (
                        echo ERROR: backend/verification.py not found
                        exit /b 1
                    )

                    if not exist backend\\tests\\test_verification.py (
                        echo ERROR: Test file not found
                        exit /b 1
                    )

                    if not exist backend\\requirements.txt (
                        echo ERROR: Requirements file not found
                        exit /b 1
                    )

                    if not exist frontend\\index.html (
                        echo ERROR: Frontend file not found
                        exit /b 1
                    )

                    if not exist docker-compose.yml (
                        echo ERROR: Docker Compose file not found
                        exit /b 1
                    )

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
                echo 'Running automated pytest test cases'

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
                echo 'Deploying GeM application'

                bat '''
                    "%DOCKER_COMPOSE%" -f docker-compose.yml up -d

                    if errorlevel 1 (
                        echo ERROR: Application deployment failed
                        exit /b 1
                    )

                    "%DOCKER_COMPOSE%" -f docker-compose.yml ps

                    if errorlevel 1 (
                        echo ERROR: Unable to check container status
                        exit /b 1
                    )

                    echo GeM application deployment completed.
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GeM application built, tested and deployed.'
        }

        failure {
            echo 'FAILED: Check Jenkins Console Output for details.'
        }

        always {
            echo 'GeM CI/CD pipeline execution completed.'
        }
    }
}
