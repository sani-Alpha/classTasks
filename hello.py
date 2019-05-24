#!/usr/bin/python3

import boto3

session=boto3.Session(profile_name='default')
sns=session.client('sns')
sns.publish(PhoneNumber='+919131810998', Message='hello from sanidhya'
