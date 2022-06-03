import os
from mcstatus import JavaServer
from dashboard.awscontroller import AWSController

class MCQueryController():

    def __init__(self, mcAws: AWSController ):
        self.url = os.environ.get('SERVER_URL')
        self.aws = mcAws
    
    def isOn(self):
        return self.aws.getState() == 'running'

    def players(self):
        if self.isOn():
            try:
                server = JavaServer("mc.sebaorrego.net", 25565, 3)
                return server.query().players.names
            except Exception as e:
                print(e)
                return None
        else:
            return None
