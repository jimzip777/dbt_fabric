# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "40baeaa8-9d7c-4db3-b557-837994bc7158",
# META       "default_lakehouse_name": "LH_test",
# META       "default_lakehouse_workspace_id": "8ac0a7a2-b0da-43af-afe3-3626f402bf31"
# META     },
# META     "environment": {
# META       "environmentId": "55740fea-1d48-44d2-b114-3d20ee1ee1f2",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC 
# MAGIC pip install azure-cli dbt-core dbt-fabric

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC git clone https://github.com/dbt-labs/jaffle-shop-classic/

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC cd jaffle-shop-classic
# MAGIC rm ./profiles.yml
# MAGIC touch ./profiles.yml
# MAGIC echo 'config:' >> ./profiles.yml
# MAGIC echo '  partial_parse: true'  >> ./profiles.yml
# MAGIC echo 'jaffle_shop:'  >> ./profiles.yml
# MAGIC echo '  target: fabric-dev'  >> ./profiles.yml
# MAGIC echo '  outputs:    '  >> ./profiles.yml
# MAGIC echo '    fabric-dev:'  >> ./profiles.yml
# MAGIC echo '      authentication: serviceprincipal'  >> ./profiles.yml
# MAGIC echo '      driver: ODBC Driver 18 for SQL Server'  >> ./profiles.yml
# MAGIC echo '      schema: edw'  >> ./profiles.yml
# MAGIC echo '      threads: 4'  >> ./profiles.yml
# MAGIC echo '      type: fabric'  >> ./profiles.yml
# MAGIC echo "      host: e5zvzpbowhnurkcwc5kzd3gs6a-ukt4bcw2wcxuhl7dgytpiav7ge.datawarehouse.fabric.microsoft.com" >> ./profiles.yml
# MAGIC echo "      tenant_id: bc5c7327-b12e-48db-a856-175591ecd2f0" >> ./profiles.yml
# MAGIC echo "      database: WH_test" >> ./profiles.yml
# MAGIC echo "      client_id: 9acf00a5-b63c-4689-99ad-33eab21eabac" >> ./profiles.yml
# MAGIC echo "      client_secret: C338Q~Nys15WtW4jolfkB7mMIr7OE.70zLWRLaVb" >> ./profiles.yml

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC cd jaffle-shop-classic
# MAGIC dbt debug --profile jaffle_shop

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC cd jaffle-shop-classic/
# MAGIC dbt seed --profile jaffle_shop

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC cd jaffle-shop-classic
# MAGIC dbt run --profile jaffle_shop

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import shutil
shutil.copytree("/jaffle-shop-classic/logs", "/lakehouse/logs_1")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC 
# MAGIC az --version

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Copies the file (or folder) from Notebook resources.
# You can copy the Lakehouse ABFS path from the contextual menu of any Lakehouse folder.
notebookutils.fs.cp(
"file:///synfs/nb_resource/builtin/test (3).txt",
"abfss://8ac0a7a2-b0da-43af-afe3-3626f402bf31@onelake.dfs.fabric.microsoft.com/40baeaa8-9d7c-4db3-b557-837994bc7158/Files/dbt_logs_1",       # Target Lakehouse ABFS path
True        # Recursive?
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from f"{notebookutils.nbResPath}/builtin/test (3).txt"
df =  pd.read_csv(f"{notebookutils.nbResPath}/builtin/test (3).txt", sep="\\s+")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
