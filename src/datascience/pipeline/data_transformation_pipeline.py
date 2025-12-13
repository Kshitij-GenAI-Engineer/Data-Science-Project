from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self, config: ConfigurationManager):
        self.config = config

    def intiate_date_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
                data_transformation_config = self.config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config=data_transformation_config)
                data_transformation.train_test_split_data()
                
            else:
                raise Exception("Data Validation not completed. Please complete data validation before data transformation.")
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME}: {e}")
            raise e 