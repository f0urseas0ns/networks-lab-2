#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

'''
Custom Topology with 6 hosts and 9 switches
'''
class CustomTopo(Topo):
    def build(self):
        
        # Create nine switches to a topology
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        
        # Create six hosts to a topology        
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        
        
        # Create links (host-switch, switch-switch) in a topology
        self.addLink(h1, s1, bw = 12, delay = '6ms', loss = 2)
        self.addLink(h2, s6, bw = 18, delay = '2ms', loss = 3)
        self.addLink(h3, s7, bw = 18, delay = '6ms', loss = 6)
        self.addLink(h4, s3, bw = 13, delay = '3ms', loss = 5)
        self.addLink(h6, s5, bw = 15, delay = '4ms', loss = 3)
        self.addLink(h5, s4, bw = 14, delay = '5ms', loss = 2)
        
        self.addLink(s1,s8,bw=20,delay='7ms',loss=15)
        self.addLink(s6,s8,bw=30,delay='1ms',loss=12)
        self.addLink(s4,s8,bw=23,delay='6ms',loss=10)
        self.addLink(s8,s2,bw=25,delay='6ms',loss=14)
        self.addLink(s2,s9,bw=30,delay='3ms',loss=18)
        self.addLink(s9,s7,bw=33,delay='8ms',loss=10)
        self.addLink(s9,s5,bw=30,delay='3ms',loss=20)
        self.addLink(s9,s3,bw=35,delay='2ms',loss=17)
        
       
        
'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 6 hosts and 9 switches
    topo = CustomTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Dump every hosts' and switches' connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
#    # Test connectivity by trying to have all nodes ping each other
#    print("Testing network connectivity")
#    net.pingAll()
    # Open mininet
    CLI(net)
    # Stop the network
    net.stop()

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()