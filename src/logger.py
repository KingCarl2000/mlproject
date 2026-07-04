import logging
import os
from datetime import datetime

# Generate a filename using the current date and time formatted as 'MM_DD_YYYY_HH_MM_SS.log'
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the path for the directory where the log file will be saved.
# NOTE: This currently appends the log file name to the directory path.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Create the directory structure. 'exist_ok=True' ensures the program doesn't crash if the folder already exists.
os.makedirs(logs_path,exist_ok=True)

# Construct the final file path for the log file itself by joining the directory path and the file name.
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure the fundamental settings for the logging system
logging.basicConfig(
    # Tell the logger to write all logs into the file we just defined
    filename=LOG_FILE_PATH,
    # Define the exact layout of each log message: [ Timestamp ] LineNumber LoggerName - LogLevel - Message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Set the threshold to INFO. It will record INFO, WARNING, ERROR, and CRITICAL messages, but ignore DEBUG.
    level=logging.INFO,
)