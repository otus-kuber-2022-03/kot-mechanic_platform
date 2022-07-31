#!/usr/bin/python3

import os

a = os.listdir(path='/opt/otus_kuber/microservices-demo')
#print(a)

for image_name in a:
	bash_command = "cd /opt/otus_kuber/microservices-demo/"+str(image_name)+" && docker build ./ -t mechanik88/"+str(image_name)+":v0.0.1 && docker push mechanik88/"+str(image_name)+":v0.0.1"
#	print(bash_command)
	os.system(bash_command)
