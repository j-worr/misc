Cron:
```
#need to add /usr/local/bin for or aws is not found when cron executes
PATH=/usr/bin:/usr/local/bin
* 19 * * * /usr/bin/bash /root/stop_ec2_instance >> /root/stop_ec2_instance.log 2>&1
```
Stop single instance:
```
#!/usr/bin/bash
aws ec2 stop-instances --instance-ids my_instanceid
```
Stop all running instances:
```
#!/usr/bin/bash

allrunning=$(aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query "Reservations[*].Instances[*].InstanceId" --output text)
aws ec2 stop-instances --instance-ids $allrunning
```
