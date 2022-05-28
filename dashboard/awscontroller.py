import os
import boto3

EC2_STATE = {
    0 : 'pending',
    16 : 'running',
    32 : 'shutting-down',
    48 : 'terminated',
    64 : 'stopping',
    80 : 'stopped'
}

class AWSController():

    def __init__(self) -> None:
        self.boto = boto3.resource('ec2')
        self.instance = self.boto.Instance(os.environ.get('INSTANCE_ID'))

    def getState(self):
        status = self.instance.state
        return EC2_STATE[status['Code']]

    def getStatusCode(self):
        status = self.instance.state
        return status['Code']

    