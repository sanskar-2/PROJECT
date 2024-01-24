# logger is for the purpose that any execution that probably happens
# we should be able to log all those information the execution everything in file 
# so that we can able to track if there is some error even the custom   exception 
# bascially comes try to log that into the text file
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# so whenever we get an exception we will take that exception logging into the logger file and use 
# login.info to put it in the log file so such way we will able to get that particular foldder also