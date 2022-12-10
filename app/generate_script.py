import os, sys 

def generate_argo_script(username, password, app_name, argo_host):
	
	login_string = f"argocd login {argo_host} --username {username} --password {password} --insecure --plaintext --loglevel debug"

	revert_string = f"argocd app rollback {app_name} --insecure --plaintext --loglevel debug"

	script = ("#!/bin/bash -e" + "\n" + 
			 login_string + "\n" + 
			 revert_string)

	return script


if __name__=="__main__":
	
	#Set values from environment variables 
	username = os.getenv("USERNAME")
	password = os.getenv("PASSWORD")
	host = os.getenv("HOST")
	app = os.getenv("APP_NAME")

	my_script = generate_argo_script(username, password, app, host)

	f = open("argo-rollback.sh", "w")
	f.write(my_script)
	f.close()