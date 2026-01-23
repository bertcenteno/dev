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

    stage ('Docker Check') {
	steps {
		sh 'docker version'
	}

    }
    
    stage('Docker Build') {
	steps {
		sh(label: 'Docker Build', script: '''#!/usr/bin/env bash
		set -euo pipefail
		      echo "BUILD_NUMBER=$BUILD_NUMBER"
		      docker build -t devops-demo:$BUILD_NUMBER .
		      docker images | grep devops-demo | head -n 5
		''')
		      }
    }

  stage('Docker Run (Smoke Test)') {
	  steps {
	    sh(label: 'Docker Run + Debug', script: '''#!/usr/bin/env bash
	      set -euo pipefail

	      docker rm -f devops-demo >/dev/null 2>&1 || true

	      echo "Starting container..."
	      docker run -d --name devops-demo -p 8081:8081 devops-demo:$BUILD_NUMBER

	      echo "Container status:"
	      docker ps -a --filter "name=devops-demo" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

	      echo "Waiting for app..."
	      for i in {1..10}; do
	        OUT=$(curl -s --max-time 2 http://127.0.0.1:8081 || true)
	        if [ -n "$OUT" ]; then
	          echo "CURL OUTPUT: $OUT"
	          exit 0
	        fi
	        sleep 1
	      done

	      echo "❌ No response from app. Showing logs:"
	      docker logs --tail 200 devops-demo || true

	      echo "Inspecting container..."
	      docker inspect devops-demo --format 'State={{json .State}}' || true

	      exit 1
	    ''')
	  }
	}
 

  }

  post {
    success { echo "✅ Pipeline succeeded" }
    failure { echo "❌ Pipeline failed" }
    always  {
	sh 'docker rm -f devops-demo || true'
    echo "Finished: ${currentBuild.currentResult}" }
  }
}

