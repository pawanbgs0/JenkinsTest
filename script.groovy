def buildApp() {
    echo 'Building application command using groovy'
}

def testApp() {
    echo 'Testing application command using groovy'
}

def deployApp() {
    echo 'Deploying application command using groovy'
    echo "deploying version ${params.VERSION}"
}

return this