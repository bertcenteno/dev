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
      sh '''
      echo "APP_NAME      : $APP_NAME"
      echo "JOB_NAME       : $JOB_NAME"
      echo "BUILD_NUMBER   : $BUILD_NUMBER"
      echo "GIT_COMMIT     : ${GIT_COMMIT:-N/A}"
      #echo "GIT_BRANCH     : $(git rev-parse --abbrev-ref HEAD)"
      echo "GIT_BRANCHES   :"
      git branch -a | sed 's/^/* /'
      '''
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

