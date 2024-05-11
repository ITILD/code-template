import logging
import logging.config
#默认的warning级别，只输出warning以上的
#使用basicConfig()来指定日志级别和相关信息
from config.path import base_path,path_config
import os


# 读取配置文件
logging.config.fileConfig(os.path.join(path_config,'logging.ini' ),encoding='utf-8')

'''
    生成文件log和带颜色控制台log
'''
error_logger = logging.getLogger('error')
state_logger = logging.getLogger('state')
# ANSI 转义序列
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
class console:
    # 静态方法
    @staticmethod
    def error(message):
        error_logger.error(Color.RED + message + Color.RESET,) 
    @staticmethod
    def exception(message,*other):
        error_logger.exception(Color.RED + message + Color.RESET,*other)
    @staticmethod
    def log(message,*other):
        state_logger.info(Color.GREEN + message + Color.RESET,*other)
        
# 输出带颜色的日志
console.log('...log配置完成')

console.log('项目根路径:'+base_path)

