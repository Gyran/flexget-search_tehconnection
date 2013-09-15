Search TehConnection
=================
This is a plugin for [Flexget](http://flexget.com/).
It can be used with the the discover plugin to make searches on TehConnection.
Currently it only supports entries with a imdb_id.

Installation
------------
Place the search_tehconnection.py in ~/.flexget/plugins/.

Example Config
---------------
```
tasks:
  theconnection:
    verify_ssl_certificates: no
    form:
      url: "https://tehconnection.eu/login.php"
      username: tehconnection username
      password: tehconnection password
    discover:
      what:
        - emit_movie_queue: yes
      from:
        - search_tehconnection: yes
    movie_queue: yes
```
