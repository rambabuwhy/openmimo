import logging

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the desired logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger(__name__)

# Example usage
'''
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
'''
