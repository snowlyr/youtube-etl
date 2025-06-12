from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'start_date': datetime(2025, 6, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'youtube_trending_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
        op_kwargs={'api_key': YT_API_KEY}
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
        op_kwargs={'raw_path': "{{ task_instance.xcom_pull(task_ids='extract') }}"}
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data,
        op_kwargs={'df': "{{ task_instance.xcom_pull(task_ids='transform') }}"}
    )

    extract_task >> transform_task >> load_task
