pipeline {
    agent any
    stages {
        stage('Source code scanning') {
            steps {
                sh 'python source_code_scan.py --input-dir src --output-file source_code_scan_results.json'
            }
        }
        stage('Dependency scanning') {
            steps {
                sh 'python dependency_scan.py --input-file requirements.txt --output-file dependency_scan_results.json'
            }
        }
        stage('Container image scanning') {
            steps {
                sh 'docker run -v $(pwd)/container_images:/images vulnerability_scanner:latest --image mycontainer:latest --output-file container_image_scan_results.json'
            }
        }
    }
}
