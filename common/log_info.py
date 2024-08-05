# 日志
import logging

logger = logging.getLogger("")

# 设置输出级别，仅当日志级别高于设置的DEBUG级别时会被logger捕获
logger.setLevel(logging.DEBUG)