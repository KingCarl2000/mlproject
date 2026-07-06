import logging
import os
import tempfile
from datetime import datetime

# Generate a filename using the current date and time formatted as 'MM_DD_YYYY_HH_MM_SS.log'
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir_candidates=[
    os.path.join(os.getcwd(),"logs"),
    os.path.join(os.getcwd(),"artifacts","logs"),
    os.path.join(tempfile.gettempdir(),"mlproject_logs"),
]

for logs_path in log_dir_candidates:
    try:
        os.makedirs(logs_path,exist_ok=True)
        LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
        with open(LOG_FILE_PATH,"a",encoding="utf-8"):
            pass
        break
    except OSError:
        continue
else:
    raise OSError("Unable to create a writable log file.")

# Configure the fundamental settings for the logging system
logging.basicConfig(
    # Tell the logger to write all logs into the file we just defined
    filename=LOG_FILE_PATH,
    # Define the exact layout of each log message: [ Timestamp ] LineNumber LoggerName - LogLevel - Message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Set the threshold to INFO. It will record INFO, WARNING, ERROR, and CRITICAL messages, but ignore DEBUG.
    level=logging.INFO,
)
