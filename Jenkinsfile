pipeline {
    agent any

    stages {
        stage('clone') {
            steps {
                git branch: 'main', credentialsId: 'amazon_automation', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
            }
        }

        stage('Build') {
            steps {
                echo "BUILDING.."
                bat '''
                    cd "Automate add to cart"
                    cd steps
                    python login.py
                    python product_search.py
                    python reviews.py
                '''
            }
        }
    }
}
