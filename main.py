import logging
import os

import tornado.web as web
import tornado.ioloop as loop
import tornado.httpserver


class MainHandler(web.RequestHandler):
    def get(self):
        self.render('main.html')

    def post(self):
        pass

    def get_template_path(self):
        return os.getcwd() + '/templates/'


class Application(web.Application):
    def __init__(self):
        logging.basicConfig(format="%(filename)8s[line: %(lineno)s] %(levelname)3s - %(message)s", level=logging.DEBUG)
        handlers = [
            (r"/", MainHandler),
        ]
        settings = {
            'debug': True,
            'compiled_template_cache': False,
            'static_path':  os.getcwd() + '/statics/'
        }
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(81)
    print("Server starts")
    loop.IOLoop.current().start()