pipeline {
  agent any

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '20'))
  }

  environment {
    APP_NAME = "devops-demo"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Info') {
      steps {
        echo "APP_NAME      : ${APP_NAME}"
        echo "JOB_NAME       : ${env.JOB_NAME}"
        echo "BUILD_NUMBER   : ${env.BUILD_NUMBER}"
        echo "BRANCH_NAME    : ${env.BRANCH_NAME ?: 'N/A'}"
        echo "GIT_COMMIT     : ${env.GIT_COMMIT ?: 'N/A'}"
      }
    }

    stage('Build') {
      steps {
        sh '''
          set -e
          echo "Building on $(uname -a)"
          echo "Workspace: $WORKSPACE"
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''
          set -e
          echo "Running tests..."
          echo "OK"
        '''
      }
    }
  }

  post {
    success { echo "✅ Pipeline succeeded" }
    failure { echo "❌ Pipeline failed" }
    always  { echo "Finished: ${currentBuild.currentResult}" }
  }
}

