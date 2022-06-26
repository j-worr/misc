## List all EC2 Instances with various key parameters into a tabbed separated value

aws ec2 describe-instances --output text --query 'Reservations[*].Instances[*].[InstanceId, InstanceType, KeyName, State.Name, LaunchTime, VpcId, SubnetId, Placement.AvailabilityZone,  PrivateIpAddress, PrivateDnsName, PublicDnsName, [Tags[?Key==`Name`].Value] [0][0], [Tags[?Key==`environment`].Value] [0][0], [Tags[?Key==`team`].Value] [0][0] ]' > instances.tsv

Sample output:

[root@centos7-docker ~]# cat instances.tsv
i-00000000000000000     t2.micro        key1        stopped 2022-04-23T10:16:25.000Z        vpc-12345678    subnet-12345678 us-east-1a      172.31.58.123   ip-172-31-58-123.ec2.internal   ec2-51-42-131-11.compute-1.amazonaws.com Server1 None    None
i-00000000000000001     t2.small        key2  stopped 2022-12-21T10:22:07.000Z        vpc-12345678    subnet-12345678 us-east-1d      172.31.64.20    ip-172-31-64-20.ec2.internal            Server2 None    None

If you want to convert from tsv to csv: 

sed 's/\t/,/g' instances.tsv > instances.csv

^that works on linux, maybe not on mac![image]
