from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'tarik',
    'start_date': datetime(2024, 1, 25),
    'catchup': False,
}

dag = DAG(
    'hello_world',
    default_args = default_args,
    schedule= timedelta(days=1)
)

t1= BashOperator(
    task_id = 'hello_world',
    bash_command ='echo "Hello world"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_tarik',
    bash_command ='echo "Hello Tarik"',
    dag = dag
)

t1 >> t2
