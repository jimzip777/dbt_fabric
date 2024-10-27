import os
from pathlib import Path
from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent / "dags" / "dbt"
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))
profile_config = ProfileConfig(
     profile_name="dbt_fabric_test",
     target_name="dev",
     profiles_yml_filepath=DBT_ROOT_PATH / "profiles.yml",
)

dbt_fabric_dag = DbtDag(
     project_config=ProjectConfig(DBT_ROOT_PATH,),
     operator_args={"install_deps": True},
     profile_config=profile_config,
     schedule_interval="@daily",
     start_date=datetime(2023, 9, 10),
     catchup=False,
     dag_id="dbt_fabric_dag",
)

# We're hardcoding this value here for the purpose of the demo, but in a production environment this
# would probably come from a config file and/or environment variables!
# DBT_PROJECT_DIR = "/dags/dbt_fabric_test"

# dbt_run = BashOperator(
#     task_id="dbt_run",
#     bash_command=f"dbt run --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}",
# )

# dbt_test = BashOperator(
#     task_id="dbt_test",
#     bash_command=f"dbt test --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}",
# )

# dbt_run
