pipeline {
    agent any

    parameters {
        string(name: 'ARGUMENTS', defaultValue: '', description: 'Arguments for the Python script')
    }

    environment {
        ENV_VAR_1 = "${BRANCH_NAME}"
        ENV_VAR_2 = "${BUILD_NUMBER}"
    }

    stages {
        stage('Run Python Script') {
            steps {
                script {
                    sh "python3 script.py ${ENV_VAR_1} ${ENV_VAR_2} ${params.ARGUMENTS}"
                }
            }
        }
    }
}
