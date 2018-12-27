#!/usr/bin/env python
import os
import sys
import boto
from boto import ec2
#meta = boto.utils.get_instance_metadata()
#id = meta['instance-id']
from collections import defaultdict

class EC(object):
 def __init__(self):

  region_name = "us-west-2"
#  region = 'us-west-2'
  name1 = sys.argv[1]
  aws_access_key_id = ''
  aws_secret_access_key = ''
#  publicip = '54.244.43.203'
#  instanceid = 'i-008bdeddacdca6112'
#  instance_id = 'i-008bdeddacdca6112'
#  public_ip = '54.201.20.157'
  self.credentials = {}
  kw_params = self.credentials
  kw_params['aws_access_key_id'] = aws_access_key_id
  kw_params['aws_secret_access_key'] = aws_secret_access_key
#  kw_params['region'] = region_name
#  kw_params['instance_id'] = instance_id
#  kw_params['public_ip'] = public_ip
  temp1=boto.ec2.connect_to_region(region_name, **kw_params )
  temp92 = temp1.get_all_tags(filters={'tag:Name': name1})
  temp93 = temp1.get_all_tags(filters={'tag:Name': '7KubeAdm'})
  temp931 = temp1.get_all_reservations(filters={'tag:Name': name1})
  temp932 = temp1.get_all_reservations(filters={'ip_address':'54.218.53.20'})
#  temp94 = temp1.get_all_tags(filters={'ip_address': 50.112.33.59})
#  temp91 = temp1.get_all_tags(filters={'Tag': 'Name'})
#  temp91 = temp1.get_all_tags(filters={'Name': 'KubeAdm'})
#  temp91 = temp1.get_all_instance_status(filters={'describe-tags': 'Name/KubeAdm'},include_all_instances=True)
#  temp9=temp7.connect_to_region("us-west-2")
#  print(temp9)



#  temp5=boto.ec2.address.Address(**kw_params)
#  temp2 = boto.ec2.connect_to_aws(ec2,region_name)
#  temp1=boto.ec2.connect_to_region(region_name, **connect_args)
#  connect_args[0] = 'AKIAJVMO3KS7LSCUTQTA' 
#  connect_args[1] = '5vVcirtGdh8DpWarWG84wr6KK8THQ3M40I1c6sdQ'
#  print(temp1) 
  print(temp92)
#  print(temp931)
#  print(temp932)
#  print(name1)
#  print(temp91)
if __name__ == '__main__':
  EC()
