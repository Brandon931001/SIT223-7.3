pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t garage-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh 'docker run --rm -v "$PWD":/workspace -w /workspace garage-app pytest tests/'
            }
        }


        stage('Code Quality') {
            steps {
                echo 'Running pylint...'
                sh 'docker run --rm -v "$PWD":/workspace -w /workspace garage-app pylint garage.py || true'
            }
        }


        stage('Security Scan') {
            steps {
                echo 'Running Bandit Security Scan...'
                sh 'docker run --rm -v "$PWD":/workspace -w /workspace garage-app bandit -r garage.py || true'
            }
        }


        stage('Deploy (Staging)') {
            steps {
                echo 'Running Docker Container (Staging)...'
                sh 'docker run -d --rm --name garage-app-staging garage-app'
            }
        }

        stage('Release') {
            steps {
                echo 'Simulating release tag...'
                sh 'git tag -a v1.0 -m "First stable release" || true'
                sh 'git push origin --tags || true'
            }
        }

        stage('Monitoring (Simulated)') {
            steps {
                echo 'Simulating Monitoring (Log Check)...'
                sh 'docker logs garage-app-staging || true'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker stop garage-app-staging || true'
        }
    }
}
