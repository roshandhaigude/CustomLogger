import logging
import logging.handlers
import traceback
import datetime
import os
import json

class CustomLogger:

    def __init__(self, log_dir, log_file_prefix, max_file_size, days_to_keep):
        self.log_dir = log_dir
        self.log_file_prefix = log_file_prefix
        self.max_file_size = max_file_size
        self.days_to_keep = days_to_keep

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        today = datetime.datetime.now().strftime('%Y-%m-%d')

        self.debug_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(self.log_dir, f'{self.log_file_prefix}-debug-{today}.log'),
            maxBytes=self.max_file_size,
            encoding='utf-8',
            delay=True
        )
        self.debug_handler.setFormatter(self.formatter)
        self.debug_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.debug_handler)

        self.error_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(self.log_dir, f'{self.log_file_prefix}-error-{today}.log'),
            maxBytes=self.max_file_size,
            encoding='utf-8',
            delay=True
        )
        self.error_handler.setFormatter(self.formatter)
        self.error_handler.setLevel(logging.ERROR)
        self.logger.addHandler(self.error_handler)

        self.critical_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(self.log_dir, f'{self.log_file_prefix}-critical-{today}.log'),
            maxBytes=self.max_file_size,
            encoding='utf-8',
            delay=True
        )
        self.critical_handler.setFormatter(self.formatter)
        self.critical_handler.setLevel(logging.CRITICAL)
        self.logger.addHandler(self.critical_handler)

        self.remove_old_files()

    def remove_old_files(self):
        for file_name in os.listdir(self.log_dir):
            if file_name.startswith(self.log_file_prefix):
                file_path = os.path.join(self.log_dir, file_name)
                modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                age_in_days = (datetime.datetime.now() - modified_time).days
                if age_in_days > self.days_to_keep:
                    os.remove(file_path)

    def debug(self, message):
        self.logger.debug(f'{message}\n{traceback.format_exc()}')

    def error(self, message):
        self.logger.error(f'{message}\n{traceback.format_exc()}')

    def critical(self, message):
        self.logger.critical(f'{message}\n{traceback.format_exc()}')

    # def log_message(self, level, message):
    #     if level == "error":
    #         self.error(message)
    #     elif level == "debug":
    #         self.debug(message)
    #     elif level == "critical":
    #         self.critical(message)
    #     else:
    #         raise ValueError("Invalid logging level specified.")

