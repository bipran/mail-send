"""log file configuration."""
import logging
from logging.handlers import RotatingFileHandler
from logging import config

# set root logger
root_logger = logging.getLogger()

# main formatter
formatter_log_file = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter_log_file = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(user)s - %(ip)s')
# for additional information in logger file.
# different handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter_log_file)

rotating_file_handler = RotatingFileHandler(
    filename='logs/api_log.log',
    mode='a',
    maxBytes=10 * 1024 * 1024,
    backupCount=4,
)
rotating_file_handler.setFormatter(formatter_log_file)

# configure the logger
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(console_handler)
# root_logger.error("I am error")
# root_logger.info('User logged in', extra={'user':'apple', 'ip':'127.0.0.1'})
mail_send_logger = logging.getLogger('rabbitmq_mail_send')
mail_send_logger.addHandler(rotating_file_handler)
# local_body_app_logger = logging.getLogger('app.local_body')
