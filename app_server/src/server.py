#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :server.py
@说明        :
@时间        :2020/07/22 17:58:16
@作者        :Riven
@版本        :1.0.0
'''

from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    # app.config.from_object(Config)

    # import error
    # error.init_error(app)

    # import log
    # log.init_log(app)

    # import routes
    # routes.init_routes(app)

    if app.config['ENV'] == 'development':
        print(app.url_map)

    return app

# app = create_app()

def main():
    app = create_app()
    
    @app.route('/')
    def index():
        return 'hello'

    app.run()

if __name__ == '__main__':
    main()