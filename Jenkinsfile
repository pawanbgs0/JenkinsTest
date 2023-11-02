pipeline{
    agent any
    parameters {
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: "")
        booleanParam(name: 'executeTests', defaultValue: true, description: "")
    }
    stages{
        stage("build"){
            steps{
                echo "Building Stage2"
            }
        }

        stage("test"){
            when {
                expression {
                    params.executeTests
                }
            }
            steps{
                echo "Testing Stage2"
            }
        }

        stage("deploy"){
            steps{
                echo "Deploying Stage2"
                echo "deploying version ${params.VERSION}"
            }
        }
    }
}