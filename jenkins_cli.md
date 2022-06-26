## Jenkins CLI commands:

Basic commands


##HELP
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'username:password' help  <---list vaid commands
```
##INSTALL PLUGIN
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'username:password' install-plugin cloudbees-bitbucket-branch-source

sudo service jenkins restart
```
Note: upgrading a plugin from cli uses install plugin as well. still need restart to take effect.


##DISABLE PLUGIN
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'admin:Adm!n321' install-plugin github
```
(no restart needed for just diabling)
