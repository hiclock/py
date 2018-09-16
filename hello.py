import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("test Hello, world")
        
Handlers=[
    (r"/", MainHandler),
    (r"/test", TestHandler),
]
application = tornado.web.Application(Handlers)
if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
