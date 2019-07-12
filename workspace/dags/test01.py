import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

import pendulum
from airflow.models import Variable
from airflow.contrib.sensors.bash_sensor import BashSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from datetime import datetime
from datetime import timedelta

local_tz = pendulum.timezone("America/New_York")
start_date=datetime(2019, 7, 10, tzinfo=local_tz)

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
    'max_active_runs_per_dag': 1,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'adhoc':False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'test01',
    default_args=default_args,
    description='test01',
    max_active_runs=1,
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='start',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='run_jar',
    depends_on_past=False,
    bash_command='/usr/local/airflow/script/launch.sh ',
    dag=dag,
    env={
            'BYE': 'BYE ',
        },
)

t1 >> t2