pipeline {
    agent any

    environment {
        VERSION = '1.0.0-SNAPSHOT'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', credentialsId: 'bb-key', url: 'git@bitbucket.org:gitkloud/gk-demo-api.git'
            }
        }
        stage('Lint') {
            steps {
                script {
                    sh '''
                        #!/bin/bash
                        echo "Linting started"
                        pip install -r requirements.txt --break-system-packages --user
                        echo "Start Lint"
                        pylint src/* || true
                        echo "Done Lint"
                    '''
                }
            }
        }
        stage('Unit') {
            steps {
                sh '''
                    #!/bin/bash
                    echo 'Unit test'
                    pytest -v || true
                '''
            }
        }
        stage('Package') {
            steps {
                sh '''
                    #!/bin/bash
                    echo 'Packaging'
                    mkdir -p target/
                    zip -r target/gk-demo-api-${VERSION}.zip src/*
                    echo "Created"
                '''
                stash includes: 'target/', name: 'artifacts'
            }
        }
        stage('Publish') {
            steps {
                unstash 'artifacts'
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-gk-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                        #!/bin/bash
                        echo 'Publishing'
                        aws s3 cp target/gk-demo-api-${VERSION}.zip s3://gk-demo-api-artifacts-975049893517-us-east-1/artifacts/gk-demo-api-${VERSION}.zip
                        echo "Copied Artifact to S3"
                    '''
                }
            }
        }
        stage('Deploy to Dev') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-gk-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                        #!/bin/bash
                        echo 'Downloading the Artifacts'
                        mkdir -p deploy/
                        aws s3 cp s3://gk-demo-api-artifacts-975049893517-us-east-1/artifacts/gk-demo-api-${VERSION}.zip deploy/gk-demo-api-${VERSION}.zip
                        echo "Copied Artifact from S3 for deployment"
                        echo "Deployment::: Started"
                    '''
                    sshPublisher(publishers: [sshPublisherDesc(configName: 'gk-dev-machine', transfers: 
                        [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''
#!/bin/bash
echo "Stopping the server"
unzip -o /home/ubuntu/artifacts/deploy/gk-demo-api-${VERSION}.zip -d /home/ubuntu/app/
echo "Unzip Success"
sudo systemctl restart gk
echo "App Deployed and Restarted"
'''
            , execTimeout: 120000,
            flatten: false,
            makeEmptyDirs: false,
            noDefaultExcludes: false,
            patternSeparator: '[, ]+',
            remoteDirectory: 'artifacts/',
            remoteDirectorySDF: false,
            removePrefix: '',
            sourceFiles: 'deploy/*.zip')],
            usePromotionTimestamp: false,
            useWorkspaceInPromotion: false,
            verbose: true)])
                }
            }
        } 
    }
    post { 
        always { 
            echo 'Post Build Action!'
            archiveArtifacts artifacts: 'target/*', followSymlinks: false
        }
    }
}
