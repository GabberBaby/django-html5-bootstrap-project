import multiprocessing
import os
import sys


bind = 'unix:/var/tmp/{{ project_name }}dev.sock'
pidfile = '/var/tmp/{{ project_name }}dev.pid'
django_settings = '{{ project_name }}.settings.dev'
pythonpath = '/projects/{{ project_name }}dev/{{ project_name }}/'

workers = multiprocessing.cpu_count() + 1

# backlog - the maximum number of pending connections.
#
# worker_class - the type of worker to use. Valid options are sync, eventlet,
#   gevent, and tornado.  See http://gunicorn.org/design.html
#
# worker_connections - the maximum number of simultaneous clients.
#   (this setting only affects the eventlet and gevent worker types)
#
# max_requests - the maxumum number of requests a worker will process before
#   restarting.  Any value greater than zero will limit the number of requests
#   a worker will process before automatically restarting.  This is a simple
#   method to help limit the damage of memory leaks.
#
# timeout - workers silent for more than this many seconds are killed and
#   restarted.  Generally set to thirty seconds.  Only set this noticeably
#   higher if you're sure of the repercussions for sync workers.  For the non
#   sync workers it just means that the worker process is still communicating
#   and is not tied to the length of time required to handle a single request.
#
# keepalive - the number of seconds to wait for requests on a Keep-Alive
#   connection.  Generally set in the 1-5 seconds range.
#
# debug - turn on debugging in the server.  This limits the number of worker
#   processes to 1 and changes some error handling that's sent to clients.
#
# spew - install a trace function that spews every line executed by the
#   server.  This is the nuclear option.
#
# preload_app - load application code before the worker processes are forked.
#   By preloading an application you can save some RAM resources as well as
#   speed up server boot times.  Although, if you defer application loading to
#   each worker process, you can reload your application code easily by
#   restarting workers.
#
# daemon - daemonize the gunicorn process.
#   (detaches the server from the controlling terminal and enters the
#   background.)
#
# user - switch worker processes to run as this user.
#   A valid user id( as an integer) or the name of a user that can be retrieved
#   with a call to pwd.getpwnam(value) or None to not change the worker process
#   user.
#
# group - switch worker processes to run as this group.
#   A valid group id (as an integer) or the name of a user that an be retrieved
#   with a call to pwd.getgrnam(value) or None to not change the worker process
#   group.
#
# umask - a bit mask for the file mode on files written by gunicorn.
#   Note that this affects unix socket permissions.
#   A valid value for the os.umask(mode) call or a string compatible with
#   int(value, 0) (0 means Python guesses the base, so values like "0", "0xFF",
#   "0022" are valid for decimal, hex, and octal representations)
#
# tmp_upload_dir - directory to store temporary request data as they are
#   read.  This may disappear in the near future!
#
# secure_scheme_headers - a dictionary containing headers and values that the
#   front-end proxy uses to indicate HTTPS requests.  These tell gunicorn
#   to set the wsgi.url_scheme to https, so your application can tell that the
#   request is secure.
#
#   The dictionary should map upper-case header names to exact string values.
#   The value comparisons are case-sensitive, unlike the header names, so make
#   sure they're exactly what your front-end proxy sends when handling HTTPS
#   requests.
#
#   It is important that your front-end proxy configuration ensures that the
#   headers defined here can not be passed directly from the client.
#
#   Default: {"X-FORWARDED-PROTOCOL": "ssl", "X-FORWARDED-SSL": "on"}
#
# logfile - the log file to write to.  Uses stdout by default.
#
# loglevel - the granularity of log ouputs.  Valid level names are:
#   debug, info, warning, error, critical
#
# logconfig - the log config file to use.
#   gunicorn uses the standard python logging module's configuration file
#   format.
#
# proc_name - a base to use with setproctitle for process naming.
#   This affects things like ps and top.  If you're going to be running more
#   one instance of gunicorn you'll probably want to set a name to tell them
#   apart.  This requires that you install the setproctitle module.
#   Default: 'gunicorn'
#
# Server Hooks ----------------------------------------------------------------
#
# on_starting(server) - called just before the master process is initialized.
#   The callable needs to accept a single instance variable for the Arbiter.
#
# when_ready(server) - called just after the server is started.  The callable
#   needs to accept a single instance variable for the Arbiter.
#
#   note: there appears to be an error in the official documentation; it is
#   simultaneously listed as being named start_server
#
# on_reload (server) - called during a reload from a SIGHUP signal.  This
#   callback should create an appropriate number of new workers.  Old workers
#   will be killed automatically by gunicorn, so it is not required to do so
#   here.  The callable needs to accept a single instance variable for the
#   Arbiter.  e.g.:
#
#   def on_reload(server):
#       for i in range(server.app.cfg.workers):
#           server.spawn_worker()
#
# pre_fork(server, worker) - called just before a worker is forked.
#   The callable needs to accept two instance variables for the Arbiter and the
#   new Worker.
#
# post_fork(server, worker) - called just after a worker has been forked.
#   The callable needs to accept two instance variables for the Arbiter and the
#   new Worker.
#
# pre_exec(server) - called just before a new master process is forked.
#   The callable needs to accept a single instance variable for the Arbiter.
#
# pre_request(worker, req) - called just before a worker processes the request.
#   The callable needs to accept two instance variables for the Worker and the
#   Request.
#
# post_request(worker, req) - called after a worker processes the request.
#   The callable needs to accept two instance variables for the Worker and the
#   Request.
#
# worker_exit(server, worker) - called just after a worker has been exited.
#   The callable needs to accept two instance variables for the Arbiter and the
#   just-exited Worker.
