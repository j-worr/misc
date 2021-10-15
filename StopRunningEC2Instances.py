#!/usr/bin/python3

#A simple script to find running instances and stop them.
#Use case: 
#Assumes default region is specified in ~/.aws/config
#Confirmed Working on Python 3.8.10

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == 'running':
            response2stop = ec2.stop_instances(InstanceIds=[instance["InstanceId"]])
            print(response2stop)
