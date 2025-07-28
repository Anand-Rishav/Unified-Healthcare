from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('retrain_if_drift', start_date=datetime(2025,7,26),
         schedule_interval='@daily', catchup=False) as dag:

    # This task will fail if drift is detected (sys.exit(1))
    drift = BashOperator(
        task_id='detect_drift', 
        bash_command='python /path/to/your/project/check_drift.py'
    )

    # This task only runs if the upstream task (drift) fails
    retrain = BashOperator(
        task_id='retrain_model', 
        bash_command='python /path/to/your/project/retrain.py',
        trigger_rule='one_failed'
    )

    drift >> retrain
