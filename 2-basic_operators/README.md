Objective:
- BashOperator
- PythonOperator
- PythonSensor
- FileSensor
- PostgresOperator
- EmailOperator to send email to inform task completion and Operator error

For docker
remove all docker container: docker system prune --all --volumes
remove orphan container: docker-compose down --volumes --remove-orphans