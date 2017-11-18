BUILDING A RATE LIMITER IN PYTHON 3 (FALCON + DOCKER)
=====================================================


From: [http://www.giantflyingsaucer.com/blog/?p=5910](http://www.giantflyingsaucer.com/blog/?p=5910)

Here is an example of a really small microservice, using 2 containers in Docker
(without any Swarm): one for Redis, the other executing the application script
with a simple server.

Having your REST services exposed publicly (and sometimes internally) can lead to particular bots or people abusing the service by essentially performing a denial of service (whether intentional or not) on your application. Rate limiting is a fact of life in REST applications and microservices world. Rate limiting if your not familiar allows you to control how much end users or systems can hit your service endpoints. So essentially something to allow them to hit the service 30 times per minute but no more.

Once you've got this repo + installed modules requirements, you can:

from */docker* directory, run this command to lauch the containers

$ docker-compose up

In another terminal (or tab) run a cURL against the service, like this:

$ curl GET http://localhost:8088/hello -v

Then ,you should have this display on your terminal:

```
* Connected to localhost (::1) port 8080 (#0)
> GET /hello HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.43.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Date: Wed, 22 Jun 2016 03:47:13 GMTR
< Server: WSGIServer/0.2 CPython/3.4.4
< x-ratelimit-limit: : 2
< content-length: 20
< x-ratelimit-reset: : 1466567293.11422
< x-ratelimit-remaining: : 1
< content-type: application/json
<
{"message": "hello"}
```
Run this command a couple more times until you'll reach the rate limit.

```
* Connected to localhost (::1) port 8080 (#0)
> GET /hello HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.43.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 429 Too Many Requests
< Date: Wed, 22 Jun 2016 03:48:11 GMT
< Server: WSGIServer/0.2 CPython/3.4.4
< content-length: 82
< content-type: application/json; charset=UTF-8
< x-ratelimit-limit: : 2
< x-ratelimit-reset: : 1466567293.4633517
< x-ratelimit-remaining: : -1
< vary: Accept
< 
{
    "title": "Rate Limit Hit",
    "description": "Blocked: Too many requests"
}
```

You have to wait for a full reset of this limit.

