import os

wsgi_app = "wsgi:app"
bind = "0.0.0.0:5000"
worker_class = "gevent"
workers = (2 * len(os.sched_getaffinity(0))) + 1
accesslog = f"""/var/log/gunicorn/{os.environ.get("DOMAIN")}/access.log"""
errorlog = f"""/var/log/gunicorn/{os.environ.get("DOMAIN")}/error.log"""
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %({x-forwarded-for}i)s'
)
