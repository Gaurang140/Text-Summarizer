from textSummarizer.constants import CONFIG_FILE_PATH , PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml
from textSummarizer.utils.common import create_directories
from textSummarizer.entity import (DataIngestionConfig)

class ConfigManager(object):
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH ,
                 params_file_path = PARAMS_FILE_PATH): 
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_files=config.local_data_files,
            unzip_dir=config.unzip_dir


        )
        return data_ingestion_config

        

