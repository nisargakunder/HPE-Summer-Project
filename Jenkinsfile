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
                echo"BUILDING.."
        bat'''cd Automate add to cart
            cd steps
            python3 login.py
            python3 search.py
            python3 reviews.py'''
            }
        }

       
    }
}