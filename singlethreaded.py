import hashlib
import docker

print(docker.__path__)
client = docker.from_env()
messages= ["c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d"]
for message in messages: 
    
    container = client.containers.run("md5summer", environment=["var=%s" % message], detach=True)
    print(container.logs())