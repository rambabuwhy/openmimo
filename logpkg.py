import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5),  # Rotate after 1 MB, keep 5 backups
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# Example usage
'''
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
'''
