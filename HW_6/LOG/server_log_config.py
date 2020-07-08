import os
import logging
from logging import handlers


# формировщик логов
FORMATTER = logging.Formatter(f"%(asctime)s - %(levelname)s - {__name__} - %(message)s ")

# ротация
ROTATION = handlers.TimedRotatingFileHandler(f'{os.path.join(os.getcwd(),"LOG", "messeger.log")}', encoding='utf-8', when='D', interval=1)
ROTATION.setFormatter(FORMATTER)
# регистратор

APP_LOG = logging.getLogger('server')
APP_LOG.addHandler(ROTATION)
APP_LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    APP_LOG.error('An error occurred')
    APP_LOG.warning('Warning')
    APP_LOG.info('Message')
    APP_LOG.critical('Critical error')
