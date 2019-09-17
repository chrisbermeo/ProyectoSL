#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='212.18.0.0/24')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='212.18.0.3', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='212.18.0.6', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='212.18.0.5', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='212.18.0.8', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='212.18.0.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='212.18.0.4', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='212.18.0.7', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='212.18.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s4, h7)
    net.addLink(s4, h8)
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s7)
    net.addLink(s2, s7)
    net.addLink(s5, s7)
    net.addLink(s6, s7)
    net.addLink(s3, s5)
    net.addLink(s4, s6)
    net.addLink(s3, h5)
    net.addLink(s3, h6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s3').start([])
    net.get('s6').start([])
    net.get('s7').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s2').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

