pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        echo "Building on Jenkins"
      }
    }

    stage('Test') {
      steps {
        echo "Running tests"
      }
    }
  }

  post {
    success {
      echo "Pipeline succeeded"
    }
    failure {
      echo "Pipeline failed"
    }
  }
}

