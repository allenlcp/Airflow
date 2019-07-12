#!/bin/bash
set +o pipefail

CMD="
java -jar /usr/local/airflow/dockerdata/java_project-1.0.jar
"

echo "cmd launched :"
echo "${CMD}"
eval ${CMD}
echo "${BYE}"
