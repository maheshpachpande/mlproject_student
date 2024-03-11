import sys
import os
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("Welcome")

try:
    data_ingestion = DataIngestion()
    train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
    print(train_data_path)
    print()
    print(test_data_path)
    

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)

