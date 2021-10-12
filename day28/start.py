# import logging

from PyQt5 import QtWidgets
from controller import MainWindow_controller
# from utils import wongwong_logger_simple

# Singleton 單例模式 (only one instance)
from utils import WongWongLogger
logger = WongWongLogger(level = "WARNING") 
# 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'

# logger = wongwong_logger_simple("root")
# logger.debug('This message should go to the log file')
# logger.info('So should this')
# logger.warning('And this, too')
# logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
# logger.critical('critical')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
