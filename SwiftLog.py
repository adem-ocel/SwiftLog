from datetime import datetime
import os
class Logger():
    def __init__(self,module_name:str):
        self.module_name = module_name
        os.makedirs('logs',exist_ok=True)
        with open(f'logs/{self.module_name}.log','a',encoding='utf-8') as file:
            file.write('')
    def log(self,level_name:str,message:str):
        with open(f'logs/{self.module_name}.log','a',encoding='utf-8') as file:
            now:datetime = datetime.now()
            log:str = f'[{now.strftime('%Y-%m-%d')}] [{now.strftime('%H:%M:%S')}] [{level_name}] [{self.module_name}]: {message}\n'
            file.write(log)
            print(log.removesuffix('\n'))

    def INFO(self,message:str):
        self.log('INFO',message)
    def WARNING(self,message:str):
        self.log('WARNING',message)
    def ERROR(self,message:str):
        self.log('ERROR',message)
    def CRITICAL(self,message:str):
        self.log('CRITICAL',message)
