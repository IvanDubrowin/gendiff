import unittest
from core import main


pretty_json = '''{
                	common: {
                		setting1: Value 1
                		- setting2: 200
                		+ setting3: {'key': 'value'}
                	- setting3: True
                	setting6: {
                		key: value
                		+ ops: vops
                }
                		+ follow: False
                		+ setting4: blah blah
                		+ setting5: {'key5': 'value5'}
                }
                	group1: {
                		+ baz: bars
                	- baz: bas
                		foo: bar
                		+ nest: str
                	- nest: {'key': 'value'}
                }
                		- group2: {'abc': '12345'}
                		+ group3: {'fee': '100500'}
                }'''


pretty_yaml = '''{
                		version: 3
                	services: {
                	nginx: {
                		image: nginx:latest
                		container_name: nginx1
                		+ ports: ['80:8070']
                	- ports: ['8085:80']
                		restart: always
                		volumes: ['./main_app/static:/static', './nginx/conf.d/app.conf:/etc/nginx/conf.d/app.conf', './nginx/nginx.conf:/etc/nginx/nginx.conf', './nginx/mime.types:/etc/nginx/mime.types']
                		depends_on: ['web']
                }
                	web: {
                		build: ./
                		+ container_name: appp
                	- container_name: app
                		+ expose: [8090]
                	- expose: [8080]
                		ports: ['8080:8080']
                }
                	mongodb: {
                		image: mongo:latest
                		container_name: mongodb
                		- ports: ['27017:27017']
                	test: {
                		+ nest: [7777, 1234]
                	- nest: [12345]
                }
                }
                		+ key: ['val1', 'val2']
                }'''

plain_json = '''Property "common.setting2" was removed
                Property "common.setting3" was updated. From "True"​ to "{'key': 'value'}"
                Property "common.setting6.ops" was added with value: "vops"
                Property "common.follow" was added with value: "False"
                Property "common.setting4" was added with value: "blah blah"
                Property "common.setting5" was added with value: "[complex value]"
                Property "group1.baz" was updated. From "bas"​ to "bars"
                Property "group1.nest" was updated. From "{'key': 'value'}"​ to "str"
                Property "group2" was removed
                Property "group3" was added with value: "[complex value]"'''

plain_yaml = '''Property "services.nginx.ports" was updated. From "['8085:80']"​ to "['80:8070']"
                Property "services.web.container_name" was updated. From "app"​ to "appp"
                Property "services.web.expose" was updated. From "[8080]"​ to "[8090]"
                Property "services.mongodb.ports" was removed
                Property "services.mongodb.test.nest" was updated. From "[12345]"​ to "[7777, 1234]"
                Property "services.key" was added with value: "[complex value]"'''
