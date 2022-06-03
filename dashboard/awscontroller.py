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
        self.ec2 = boto3.resource('ec2')
        self.instanceID = os.environ.get('INSTANCE_ID')

    def getState(self):
        status = self.getInstance().state
        return status['Name']

    def getStatusCode(self):
        status = self.getInstance().state
        print('aws code',status['Code'])
        return status['Code']

    def stop(self):
        self.getInstance().stop()

    def start(self):
        self.getInstance().start()
    
    def getInstance(self):
        return self.ec2.Instance(self.instanceID)