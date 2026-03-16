pipeline {
    agent any

    // Тригер для автоматичного запуску від GitHub
    triggers {
        githubPush()
    }

    stages {
        stage('Підготовка (Checkout)') {
            steps {
                echo 'Jenkins автоматично завантажив код із GitHub завдяки Jenkinsfile!'
                // Нам більше не треба писати тут команду git url: '...',
                // бо Jenkins сам знає, звідки він взяв цей Jenkinsfile!
            }
        }

        stage('Тестування (Test)') {
            steps {
                dir('src') {
                    echo 'Запускаємо автоматичні тести Python...'
                    bat '''
                    set PYTHONPATH=.
                    python -m unittest test_calculator.py
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Надсилаємо повідомлення про успіх...'
            withCredentials([
                string(credentialsId: 'TELEGRAM_TOKEN', variable: 'TOKEN'),
                string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'CHAT_ID')
            ]) {
                bat '''
                curl -s -X POST https://api.telegram.org/bot%TOKEN%/sendMessage -d chat_id=%CHAT_ID% -d text="Zbirka uspishna! Vsi testy projdeno z Jenkinsfile."
                '''
            }
        }
        failure {
            echo 'Надсилаємо повідомлення про помилку...'
            withCredentials([
                string(credentialsId: 'TELEGRAM_TOKEN', variable: 'TOKEN'),
                string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'CHAT_ID')
            ]) {
                bat '''
                curl -s -X POST https://api.telegram.org/bot%TOKEN%/sendMessage -d chat_id=%CHAT_ID% -d text="Pomylka zbirky! Perevir Jenkins."
                '''
            }
        }
    }
}