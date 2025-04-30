import json
import subprocess

# --- Hardcoded Databricks host and token ---
DATABRICKS_HOST = "https://dbc-5f99fc48-0975.cloud.databricks.com"
DATABRICKS_TOKEN = "dapiee6e44bd23367fa14cb92cc95cf048cb"  # Replace with your token
# -------------------------------------------

JOB_FILE = "bundle/jobs/sample-job.json"
LOCAL_SCRIPT = "bundle/jobs/my_script.py"
DBFS_SCRIPT_PATH = "dbfs:/scripts/my_script.py"

def upload_script_to_dbfs():
    print(f"Uploading script to DBFS: {LOCAL_SCRIPT} -> {DBFS_SCRIPT_PATH}")
    result = subprocess.run([
        "databricks", "fs", "cp", LOCAL_SCRIPT, DBFS_SCRIPT_PATH, "--overwrite"
    ], env={
        "DATABRICKS_HOST": DATABRICKS_HOST,
        "DATABRICKS_TOKEN": DATABRICKS_TOKEN
    }, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def deploy_job():
    with open(JOB_FILE, 'r') as f:
        job_config = json.load(f)

    print("Creating or updating Databricks job...")
    result = subprocess.run([
        "databricks", "jobs", "create",
        "--json-file", JOB_FILE
    ], env={
        "DATABRICKS_HOST": DATABRICKS_HOST,
        "DATABRICKS_TOKEN": DATABRICKS_TOKEN
    }, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == "__main__":
    upload_script_to_dbfs()
    deploy_job()
