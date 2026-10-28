pipeline {
    agent any

    environment {
        APP_DIR = 'C:\\Users\\nagat\\Downloads\\gem-bid-compliance-docker-application'
        DOCKER_COMPOSE = 'C:\\Users\\nagat\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker-compose.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking GeM application files'

                bat '''
                    if not exist "%APP_DIR%\\docker-compose.yml" (
                        echo ERROR: docker-compose.yml not found
                        exit /b 1
                    )

                    if not exist "%APP_DIR%\\frontend\\index.html" (
                        echo ERROR: Frontend file not found
                        exit /b 1
                    )

                    echo Application files found successfully.
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building GeM Docker images'

                bat '''
                    "%DOCKER_COMPOSE%" -f "%APP_DIR%\\docker-compose.yml" build
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Checking Docker Compose configuration'

                bat '''
                    "%DOCKER_COMPOSE%" -f "%APP_DIR%\\docker-compose.yml" config
                    if errorlevel 1 exit /b 1
                    echo Docker Compose configuration is valid.
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying GeM application'

                bat '''
                    "%DOCKER_COMPOSE%" -f "%APP_DIR%\\docker-compose.yml" up -d --force-recreate
                    if errorlevel 1 exit /b 1

                    "%DOCKER_COMPOSE%" -f "%APP_DIR%\\docker-compose.yml" ps
                    if errorlevel 1 exit /b 1
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GeM application built, checked, and deployed.'
        }

        failure {
            echo 'FAILED: Check the Console Output for the exact error.'
        }
    }
}