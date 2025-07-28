import pandas as pd, json, sys
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

ref   = pd.read_parquet('data/reference.parquet')
batch = pd.read_parquet('data/latest_batch.parquet')

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=batch)
result = report.as_dict()

with open('drift_report.json', 'w') as f:
    json.dump(result, f, indent=4)

# Exit with a non-zero status code if drift is detected
if result['metrics'][0]['result']['dataset_drift']:
    print("Data drift detected!")
    sys.exit(1)
else:
    print("No data drift detected.")
    sys.exit(0)
