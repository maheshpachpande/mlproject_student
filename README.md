# mlproject_student
# mlproject
#### virtual enviroment
- conda create -p student python==3.9 -y
- conda activate C:\Users\pachp\Desktop\projects\mlproject_student\student
#### create the template.py for generic folder structure of machine learning project
- python template.py
#### create logger.py
#### create exception handling in exception.py
#### create data_ingestion
#### track data by dvc --> dvc init ---> delete artifacts --> git add . ---> git status --> git commit -m "first" ---> git push origin main ---> python app.py ---> dvc add artifacts/raw.csv ---> git add . ---> git commit ---> git push. ---> git logs ---> git checkout adddcommitnumber.
#### mlflow tracking
- MLFLOW_TRACKING_URI=https://dagshub.com/pachpandemahesh300/mlproject_student.mlflow \
- MLFLOW_TRACKING_USERNAME=pachpandemahesh300 \
- MLFLOW_TRACKING_PASSWORD=9f73334e82cb0e1dc7693e6eed2b0827c86e8db9 \
- python script.py