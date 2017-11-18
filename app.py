import json
from wsgiref import simple_server
 
import falcon
from rate_limit import RateLimiter
 
 
class HelloResource(object):
    def on_get(self, req, resp):
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'message': 'hello'})
 
app = falcon.API(middleware=[RateLimiter(limit=2)])
hello = HelloResource()
app.add_route('/hello', hello)
 
 
if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8088, app)
    httpd.serve_forever()

