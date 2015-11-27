###test documentation###
* You need to download redis and redis-py before you start to test.
* redis: https://github.com/antirez/redis
* redis-py: https://github.com/andymccurdy/redis-py
* You should run these test programs in the redis-py folder.(I do not know why sys.path.append() does not work...) 
* python version: >= 3.0
* I just want to test two items: 
** How many items(50M) can redis store(including generating-data time) in a given time?
** How long it will take when it generates a given number of items(50M)?
