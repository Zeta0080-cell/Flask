# <>提取参数
# <int:id>  这里的int就是系统转换器
# 自定义转换器

from werkzeug.routing import BaseConverter
from flask import Flask

app=Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex