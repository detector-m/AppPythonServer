#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :main.py
@说明        :
@时间        :2020/07/23 09:08:39
@作者        :Riven
@版本        :1.0.0
'''

from flask import Flask

import sys
sys.path.append('.')
from app_server.src.config import setting
from app_server.src.error import error
from app_server.src.log import log
from app_server.src.routes import routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    # 配置
    # app.config.from_object(setting)
    load_config(app)

    # 错误处理
    # error.init_error(app)
    error.handle_error(app)

    # 日志处理
    log.init_log(app)
    # app.logger.error('error')
    # log.LOGGER.warn('-----sef')
    
    # 路由处理
    routes.init_routes(app)

    # if app.config['ENV'] == 'development':
    #     print(app.url_map)

    # @app.route('/')
    # def index():
    #     return 'hello'

    return app

def load_config(app):
    app.config.from_object(setting)

def main():
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()