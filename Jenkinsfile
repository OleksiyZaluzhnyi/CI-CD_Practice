pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Підготовка (Checkout)') {
            steps {
                echo 'Завантажуємо свіжий код...'
            }
        }

        stage('Тестування (Test)') {
            steps {
                dir('src') {
                    echo 'Запускаємо автоматичні тести...'
                    bat '''
                    set PYTHONPATH=.
                    python -m unittest test_calculator.py
                    '''
                }
            }
        }

        // НОВИЙ ЕТАП: Пакування готового продукту
        stage('Доставка (Deliver)') {
            steps {
                echo 'Тести пройдено! Зберігаємо готову програму як Артефакт...'
                // Ця команда каже: "Знайди всі файли .py в папці src і збережи їх"
                archiveArtifacts artifacts: 'src/*.py', fingerprint: true
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
                curl -s -X POST https://api.telegram.org/bot%TOKEN%/sendMessage -d chat_id=%CHAT_ID% -d text="Zbirka uspishna! Artefakty zberesheno."
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
