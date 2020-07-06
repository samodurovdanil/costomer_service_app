import sys, os
import logging

# формировщик логов
FORMATTER = logging.Formatter(f"%(asctime)s - %(levelname)s - {__name__} - %(message)s ")

# поток вывода
FILE_HANDLER = logging.FileHandler(f'{os.path.join(os.getcwd(),"LOG", "messeger.log")}', encoding='utf-8')
FILE_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setLevel(logging.DEBUG)

# регистратор
APP_LOG = logging.getLogger('client')
APP_LOG.setLevel(logging.DEBUG)
APP_LOG.addHandler(FILE_HANDLER)

if __name__ == '__main__':
    APP_LOG.error('An error occurred')
    APP_LOG.warning('Warning')
    APP_LOG.info('Message')
    APP_LOG.critical('Critical error')
