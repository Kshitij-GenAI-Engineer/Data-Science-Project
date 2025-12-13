import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_split(self)
        data=pd.read_csv(self.config.data_path)
        
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
        
        train_data.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Data split and saved at {self.config.root_dir}")
        