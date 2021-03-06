## Jenkins CLI commands:

### HELP
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'username:password' help  <---list vaid commands
```
### INSTALL PLUGIN
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'username:password' install-plugin cloudbees-bitbucket-branch-source

sudo service jenkins restart
```
Note: upgrading a plugin from cli uses install plugin as well. still need restart to take effect.


### DISABLE PLUGIN
```
java -jar jenkins-cli.jar -s http://localhost:8085 -auth 'admin:Adm!n321' install-plugin github
```
(no restart needed for just diabling)


### JENKINS TROUBLESHOOTING

Restarting Jenkins
```
<jenkins-url>/restart and click on Yes to confirm
```

Clearing the build queue: Manage jenkins > Script Console
```
Jenkins.instance.queue.clear()
```

If you have a build that won't cancel, 
```
http://jenkins-url/job/{job name}/{build number}/stop
```
if that doesn't work, could try
```
http://jenkins-url/job/{job name}/{build number}/kill
```

You can find the proper job full name with Script Console >
```
  Jenkins.instance.getAllItems(AbstractItem.class).each {
    println(it.fullName)
  };
```

Previously those didn't work and had to run a `systemctl restart jenkins' when no jobs where actually running
--> Also in this scenario, adding additional executors allowed new attempts to work.
