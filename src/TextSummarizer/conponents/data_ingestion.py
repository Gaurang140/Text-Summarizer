# components 
import os 
from urllib import request as request
import zipfile
from textSummarizer.logging import logger 
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig



class DataIngestion:
    def __init__(self , config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_files
                
            )
            logger.info(f'{filename}  download! with folder info \n{headers}')
        else : 
            logger.info(f"file already exist size of {get_size(Path(self.config.local_data_files))}")


    def extract_data(self):
        """
        Zip_file_path  : str 
        Extrtact the data from the zip file into the local data folder
        functions return None 
        """
        unzip_file_path = self.config.unzip_dir

        os.makedirs(unzip_file_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_file_path)