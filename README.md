# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
1. Open pietty and connect to **`140.113.195.69 port 45078`**
2. Log in as **`root`** with the password **`cn2018`**
3. Navigate to the Network_Topology folder containing `topology.py` through the command `cd Network_Topology/src`
4. Execute `topology.py` through the command `./topology.py`
5. Wait for `topology.py` to run and and launch Mininet in the terminal
6. Once Mininet is launched, use iPerf to measure the TCP connection of **`h2`** and **`h4`**, and save the results to **`./out`** folder through the following commands:
  - `h4 iperf -s -u -i 1 > ./out/result &`
  - `h2 iperf -c 10.0.0.4 -u -i 1`
7. Wait for iPerf to finish running for the results to be displayed and saved
8. Exit Mininet through the command `exit` and wait for the network to be shut down

> * Show the screenshot of using iPerf command in Mininet
9. Result of running iPerf in Mininet:
![iPerf.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/src/out/iperf.PNG)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
1.
![init.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/screenshots/custom.PNG)
  - Define a custom topology for use in a network (topo1.png)

2.
![switch.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/screenshots/switch.PNG)
  - `self.addsSwitch`: Create and add a switch to the topology

3.
![host.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/screenshots/hosts.PNG)
  - `self.addHost`: Create and add a host to the topology

4.
![link.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/screenshots/links.PNG)
  - `self.addLink(host, switch, bw, delay, loss)`: Create a birectional link between the specified host/switch and switch in [topo1](https://github.com/f0urseas0ns/networks-lab-2/blob/master/src/topo/topo1.png), and specifies the bandwidth in Mbits, delay in ms and pecentage loss of that connection

5.
![simpletest.png](https://github.com/f0urseas0ns/networks-lab-2/blob/master/screenshots/simpletest.PNG)
  - Create a network using the custom topology
  - `topo = CustomTopo()`: Create an instance of the custom topology with 6 hosts and 9 switches
  - `net = Mininet(topo = topo, controller = OvSController, link = TCLink)`: Create a new network using the custom topo, OvS controller and TCLink
  - `net.start()`: Start the network by creating all required controllers, links, hosts and switches
  - `dumpNodeConnections(net.hosts)/dumpNodeConnections(net.switches)`: Dump the connections to and from every hosts/switches
  - `net.pingAll()`: Test the connectivity of the network by having the hosts ping each other
  - `CLI(net)`: Open Mininet CLI in the terminal to allow for viewing of network topology, testing of connectivity and measurement of performance with iPerf
  - `net.stop()`: Stops the network by stopping all controllers, links, hosts and switches


### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail
1. `h4 iperf -s -u -i 1 > ./out/result &`
  - `h4 iperf -s`: run iPerf server on h4
  - `-u`: use UDP instead of TCP
  - `-i 1`: set 1 second interval between periodic bandwidth, jitter and loss reports

2. `h2 iperf -c 10.0.0.4 -u -i 1`
  - `h2 iperf -c 10.0.0.4`: run iPerf client on h2 and connect to 10.0.0.4
  - `-u`: use UDP instead of TCP
  - `-i 1`: set 1 second interval between periodic bandwidth, jitter and loss reports


### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
  - I first connected to my container via Secure Shell (SSH) through PieTTY. Using the user and password credentials **`root`** and **`cn2018`**, I connected to IP address **`140.113.195.69`** on **`port 45078`**. Once I was successfully logged onto my container, I cloned my working GitHub repository to a new directory called **`"Network_Topology"`**. This was done using the command `git clone https://github.com/f0urseas0ns/networks-lab-2.git`. To confirm that my files were cloned successfully, I checked that the correct directory with right files existed using the command `ls`.
  - Once I have successfully cloned the GitHub repository, I then checked that Mininet was running properly. This was done through the command `sudo mn` which opens Mininet in the terminal. An error message appeared saying that there was an error in connecting to Open vSwith database server. Since this was an error due to Open vSwitch service not being started, this error was easily fixed with the command `open vswitch-switch start` which starts the affected service.
  - Once I have verified that Open vSwitch is running properly, I then changed the working directory to the **src** folder of **Network_Topology** through the command `cd /root/Network_Topology/src/`. I then changed the permission of **`example.py`** via the command `sudo chmod +x example.py` and then executed the python program with `sudo ./example.py`.

2. **Example of Mininet**
  - In this lab I make use of Mininet, which is a network emulator that allows the creation of a network comprising of hosts, switches, controllers and links.
  - Running `example.py` shows a simple example of how a network with custom topology is defined and started. In `example.py`, a single switch topology setup with 2 hosts can be seen. Links have been created between each host and the single switch, hence creating a linked network. In `example.py`, the links were created with bandwidths of 10Mbit, 5ms delay and 0% loss. These links were also created using a `for loop` which also creates each host to be linked with the switch.
  - From `example.py`, it can be seen that the important functions that would be required would be as the following:
    - `self.addSwitch`
    - `self.addHost`
    - `self.addLink`
  - In `example.py`, there is also a function to start a network using a predefined topology. First, an instance of the custom topology is created and defined. Following that, a new Mininet instance is then created with the custom topology, a OvS controller and TCLink. After starting the network, information about the connections of every hosts and switches are dumped, and the connectivity between each host is tested by pinging each other.

3. **Topology Generator**
  - I created the custom topology required by first duplicating `example.py` and renaming it as `topology.py`. I then removed the unnecessary parts of the code, such as `n` variable and `for loop` as I would be defining my hosts, switches and links manually. After stripping `topology.py` of its unessential parts, I then began creating the hosts and switches required in the custom topology. The custom topology was obtained by taking the result of my student id modulus 3, and cross referencing the specific setup for that result **(topo1.png)**. Once I had instantiated the required hosts and switches, I then began to create links between hosts and switches, and switches and switches as required in the custom topology. 
  - To check that my custom topology works correctly as defined, I ran `topology.py` without opening Mininet CLI in my code. Connectivity was tested by having all the hosts and switches to dump information related to their connection, as well as having the hosts ping each other. For example, having a 100% packet loss from running `topology.py` allowed me to pinpoint a duplicate host-switch link that I had mistakenly created, which upon fixing solved the issue of 100% packet loss.
  - Once I was sure my topology was working properly, I then ran Mininet CLI from `topology.py` after starting a new network with my custom topology. For this part, I removed part of `topology.py` that had to do with the hosts pinging each other as this portion had significant running time, and removing this portion would allow my program to run much faster. Furthermore, this portion had to do with testing the connectivity, which I had confirmed previously and hence had not much use for me at this point of the lab.

4. **Measurement**
  - The main objective of this lab is to measure the performance of my custom topology, which is done using iPerf. iPerf is a flexible tool that allows for active measurements of maximum achievable bandwidths on IP networks, while supporting the tuning for various parameters for varied purposes. In this case, we used it to determine the results of the network topology by returning the bandwidth and percentage loss over an interval of 1s for up to 10s.
  - In our iPerf test, I configured the iPerf server to hosted on h4 while the iPerf client would be connecting from h2. h2 would be connecting to the IP address 10.0.0.4, which is the IP address of the iPerf server hosted on h4. Once h2 has connected to h4, the server then sends 1470 byte datagrams to the client while recording the performance of the network. The results which can be seen in the screenshot in the previous section, is shown after 10 seconds have passed where I can observe the rate of packet loss. As the obtained rate of packet loss falls within the acceptable range of packet loss from 51% to 58%, it can be conclude that my network topology is working as intended. Upon obtaining these results, I saved the output to `./out/result`.
  - Once I have finished measurement, I then exited Mininet CLI and shut down the network.

---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [Thomas Ng](https://github.com/f0urseas0ns/networks-lab-2)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3