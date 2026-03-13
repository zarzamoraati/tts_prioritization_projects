import json
from pathlib import Path 

class TTSConfig:
    def __init__(self,config_data):
        self.tts_base_url_server=config_data["tts_url_server"]
        
        
class AppConfig:
    def __init__(self,config_file_path="config.json"):
        
        with open(config_file_path,"r") as f:
            
            data=json.load(f)
            self.tts_server=TTSConfig(data["tts_server"])
    