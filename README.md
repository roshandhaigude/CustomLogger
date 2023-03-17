#Custom Logger
This is a simple custom logger class that allows you to log messages with different levels of severity to different log files. It is designed to rotate log files based on a maximum file size and the number of days to keep the logs.

How to use
Create an instance of the CustomLogger class:
python
Copy code
from custom_logger import CustomLogger

log_dir = '/path/to/logs'
log_file_prefix = 'my-app'
max_file_size = 1048576 # 1 MB
days_to_keep = 30

logger = CustomLogger(log_dir, log_file_prefix, max_file_size, days_to_keep)

Use the logger to log messages:

logger.debug('This is a debug message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')

Parameters

log_dir (str): The directory where log files will be stored.
log_file_prefix (str): A prefix for the log file names.
max_file_size (int): The maximum size of each log file in bytes.
days_to_keep (int): The number of days to keep log files before they are rotated.

Methods

debug(message): Log a message with severity level DEBUG.
error(message): Log a message with severity level ERROR.
critical(message): Log a message with severity level CRITICAL.

Log files

The logger creates three log files with different severity levels:

{log_file_prefix}-debug-{date}.log: Debug log messages.
{log_file_prefix}-error-{date}.log: Error log messages.
{log_file_prefix}-critical-{date}.log: Critical log messages.
Log files are rotated based on the max_file_size and days_to_keep parameters. Old log files will be automatically removed.

Dependencies
This code has no external dependencies.
