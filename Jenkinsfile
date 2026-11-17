
pipeline {
    agent any

    environment {
        DOCKER_EXE = 'C:\\Users\\nagat\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking GeM application files'

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

                bat '''
                    "%DOCKER_EXE%" compose build
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated pytest tests'

                bat '''
                    "%DOCKER_EXE%" compose run --rm backend python -m pytest -v
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying GeM application'

                bat '''
                    "%DOCKER_EXE%" compose up -d
                    if errorlevel 1 exit /b 1

                    "%DOCKER_EXE%" compose ps
                    if errorlevel 1 exit /b 1
                '''
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

pipeline {
    agent any

    environment {
        DOCKER_EXE = 'C:\\Users\\nagat\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking GeM application files'

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

                bat '''
                    "%DOCKER_EXE%" compose build
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated pytest tests'

                bat '''
                    "%DOCKER_EXE%" compose run --rm backend python -m pytest -v
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying GeM application'

                bat '''
                    "%DOCKER_EXE%" compose up -d
                    if errorlevel 1 exit /b 1

                    "%DOCKER_EXE%" compose ps
                    if errorlevel 1 exit /b 1
                '''
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
