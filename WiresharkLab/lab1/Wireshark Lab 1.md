## Wireshark Lab 1

### 1. 获取并运行wireshark软件

[wireshark官网]( http://www.wireshark.org/download.html)获取wireshark软件。

安装后运行界面如下：

![Inital](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\Inital.png)

### 2. 数据包捕获界面解析

![GUI](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\GUI.png)

This looks more interesting! The Wireshark interface has five major components:

• The ```command menus``` are standard pulldown menus located at the top of the window. Of interest to us now are the File and Capture menus. The File menu allows you to save captured packet data or open a file containing previously captured packet data, and exit the Wireshark application. The Capture menu allows you to begin packet capture.

• The ```packet-listing window``` displays a one-line summary for each packet captured, including the packet number (assigned by Wireshark; this is not a packet number contained in any protocol’s header), the time at which the packet was captured, the packet’s source and destination addresses, the protocol type, and protocol-specific information contained in the packet. The packet listing can be sorted according to any of these categories by clicking on a column name. The protocol type field lists the highest-level protocol that sent or received this packet, i.e., the protocol that is the source or ultimate sink for this packet.

• The``` packet-header details window``` provides details about the packet selected (highlighted) in the packet-listing window. (To select a packet in the packet-listing window, place the cursor over the packet’s one-line summary in the packet-listing window and click with the left mouse button.). These details include information about the Ethernet frame (assuming the packet was sent/received over an Ethernet interface) and IP datagram that contains this packet. The amount of Ethernet and IP-layer detail displayed can be expanded or minimized by clicking on the plus minus boxes to the left of the Ethernet frame or IP datagram line in the packet details window. If the packet has been carried over TCP or UDP, TCP or UDP details will also be displayed, which can similarly be expanded or minimized. Finally, details about the highest-level protocol that sent or received this packet are also provided.

• The ```packet-contents window ```displays the entire contents of the captured frame, in both ASCII and hexadecimal format.

• Towards the top of the Wireshark graphical user interface, is the ```packet display filter field```, into which a protocol name or other information can be entered in order to filter the information displayed in the packet-listing window (and hence the packet-header and packet-contents windows). In the example below, we’ll use the packet-display filter field to have Wireshark hide (not display) packets except those that correspond to HTTP messages.

### 3. 利用wireshark软件进行实践

1. 打开你最喜欢的web浏览器，浏览器会显示你已选择的主页。

2. 启动wireshark软件，其窗口类似于上面运行界面。

3. 选择中要进行数据包捕捉的网络接口。

4. 如要停止进行捕获，选中界面左上方的停止捕获按钮。

5. 当wireshark运行时，在浏览器地址栏输入http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html，随后会出现一个结果页面；此时，wireshark已经对该http请求数据包和应答数据包进行的捕获。

   ![HomePage](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\HomePage.png)

6. 若想要在wireshark界面直接对http数据包进行分析，可以通过上方的过滤器进行过滤。

   ![filter](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\filter.png)

7. 选中信息栏中 为GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1的数据包。

   ![GET](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\GET.png)

8. 通过在中间的数据包头窗口查看细节信息，每个信息都可通过`>`符号来进行细节的查看。

   ![Details](C:\Users\admin\Desktop\杂项\CN\WiresharkLab\lab1\Details.png)

9. 如果需要进行保存则可对其进行保存后，再进行退出操作。





