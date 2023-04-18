pipeline {
    agent any
    stages {
        stage('Source code scanning') {
            steps {
                echo 'source code scan'
                sh 'python source_code_scan.py --input-dir src --output-file source_code_scan_results.json'
            }
        }
        stage('Dependency scanning') {
            steps {
                echo 'Dependency scann'
                sh 'python dependency_scan.py --input-file requirements.txt --output-file dependency_scan_results.json'
            }
        }
        stage('Build Container Image') {
            steps {
                echo 'build container'
                // Build the container image and tag it with the commit hash
                sh "docker build -t myapp:${env.GIT_COMMIT} ."
            }
        }

        stage('Scan Container Image') {
            steps {
                
                echo 'image scan python script'
                // Run the container image scanning script and save the results to a file
                sh "python container_image_scanning.py --image-name myapp:${env.GIT_COMMIT} --output-file scan_results.json"

                // Parse the scan results and print them to the console
                script {
                    def results = readJSON(file: 'scan_results.json')
                    println results
                }

                // Fail the build if the scan results contain critical vulnerabilities
                script {
                    def results = readJSON(file: 'scan_results.json')
                    def vulnerabilities = results.get('vulnerabilities', [])
                    def critical_vulnerabilities = vulnerabilities.findAll { it.severity == 'HIGH' || it.severity == 'CRITICAL' }
                    if (critical_vulnerabilities.size() > 0) {
                        error 'Critical vulnerabilities found in container image'
                    }
                }
            }
        }

        stage('Deploy Container Image') {
            steps {
                echo 'deploy'
                // Deploy the container image to a Kubernetes cluster
                sh "kubectl apply -f deployment.yaml"
            }
        }
    }
}
