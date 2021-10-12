from datetime import datetime, timezone
import logging
import pytz
import os

ColorLevel = {
    'CRITICAL': '\33[35mCRITICAL\33[0m',
    'ERROR': '\33[31mERROR\33[0m',
    'WARNING': '\33[33mWARNING\33[0m',
    'INFO': '\33[36mINFO\33[0m',
    'DEBUG': '\33[32mDEBUG\33[0m'
}

class MyFormatter(logging.Formatter):
    # override the converter in logging.Formatter
    converter = datetime.fromtimestamp

    # override formatTime in logging.Formatter
    def formatTime(self, record, datefmt=None, timezone="UTC"):
        dt = self.converter(record.created, tz=pytz.timezone(timezone)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        tz = self.converter(record.created, tz=pytz.timezone(timezone)).strftime("%z")
        tz_ = "".join([dt, tz])
        print(tz_)
        return tz_

    # override color word
    def format(self, record):
        """
        Format the specified record as text.

        The record's attribute dictionary is used as the operand to a
        string formatting operation which yields the returned string.
        Before formatting the dictionary, a couple of preparatory steps
        are carried out. The message attribute of the record is computed
        using LogRecord.getMessage(). If the formatting string uses the
        time (as determined by a call to usesTime(), formatTime() is
        called to format the event time. If there is exception information,
        it is formatted using formatException() and appended to the message.
        """
        record.message = record.getMessage()

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        s = self.formatMessage(record)

        for key, value in ColorLevel.items():
            s = s.replace(key, value)

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + record.exc_text
        if record.stack_info:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + self.formatStack(record.stack_info)
        return s



#TO DO: Refactor filehandler
class WongWongLogger(logging.RootLogger):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, file_name=None, mode="w", level="DEBUG"):
        """
        Initialize the logger with the name "root".
        """
        logging.Logger.__init__(self, "root", level)
        if file_name is not None:
            file_name = os.path.abspath(file_name)
        self.logging_setting(file_name, mode, level)


    def logging_setting(self, file_name=None, mode="w", level="DEBUG"):
        if self.handlers:
            for handler in self.handlers:
                self.removeHandler(handler)

        self.setLevel(level=level)
        console = logging.StreamHandler()
        
        formatter = MyFormatter(fmt="[log][%(asctime)s#%(process)d][%(levelname)s][%(module)s.%(funcName)s]:[%(message)s]")
        self.Formatter = formatter
        console.setFormatter(formatter)
        
        self.addHandler(console)
        if file_name is not None:
            file_handler = logging.FileHandler(os.path.abspath(file_name), mode=mode, encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)
        

# Abandon function
# def logging_setting(file_name="example.log", mode="w", level="DEBUG"):

#     root = logging.getLogger()
#     if root.handlers:
#         for handler in root.handlers:
#             root.removeHandler(handler)

#     root.setLevel(level=level)
#     console = logging.StreamHandler()
#     file_handler = logging.FileHandler(os.path.abspath(file_name), mode=mode)
#     formatter = MyFormatter(fmt="[watchlog][%(asctime)s#%(process)d][%(levelname)s][%(funcName)s]:[%(message)s]")
#     # print(formatter.getlevel())
#     logging.Formatter = formatter
#     console.setFormatter(formatter)
#     file_handler.setFormatter(formatter)
#     root.addHandler(console)
#     root.addHandler(file_handler)
#     return logging
#     #root.addHandler(logging.FileHandler("example.log", mode='w'))
#     #logging.critical('test')


# Abandon function
# def log_wrapper(func):
#     def warp(*args, **kwargs):
#         #print(f"[wrapper] args = {args}")
#         #print(f"[wrapper] kwargs = {kwargs}")
#         try:
#             func(*args, **kwargs)
#         except NameError as err:
#             logging.error("function: {} fail got NameError:{}".format(func.__name__, err))
#             #raise e
#         except Exception as e:
            
#             logging.error("function: {} fail got:{}".format(func.__name__, e))
#             #raise e
#         else:
#             logging.info("function: {} pass args:{}".format(func.__name__, args))
            
#         finally:
#             pass
#             #logging.info("function: {} pass".format(func.__name__))

#     return warp


if __name__ == "__main__":
    # example
    logger = WongWongLogger()

    # logging_setting()
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    logger.critical('critical')