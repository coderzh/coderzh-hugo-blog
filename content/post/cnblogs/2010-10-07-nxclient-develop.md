---
categories:
- 技术文章
date: '2010-10-07'
title: NX Client开发步骤
url: /2010/10/07/nxclient-develop/

---


在freenx的svn库里有好几个NX Client工程，比如：qtnx，还有Python的实现版本gnx（仅限linux系统），因此，可以参照这些工程的实现。

Svn co http://svn.berlios.de/svnroot/repos/freenx/trunk freenx

1. Connect to the server using nxssh

nxssh -nx -i /usr/NX/share/client.id_dsa.key nx@&lt;host address&gt;

If you are using encrypted session:

nxssh -nx -i /usr/NX/share/client.id_dsa.key nx@&lt;host address&gt; -B

for Windows client, you have to include the -v switch for encrypted sessions to work.

nxssh -nx -i /usr/NX/share/client.id_dsa.key nx@&lt;host address&gt; -v -B

You will get the following response:

NX&gt; 203 NXSSH running with pid &lt;some pid&gt;

NX&gt; 285 Enabling check on switch command

NX&gt; 200 Connected to address: &lt;address&gt; on port: &lt;port&gt;

NX&gt; 202 Authenticating user: nx

NX&gt; 208 Using auth method: publickey

HELLO NXSERVER - Version 1.4.0-02 OS_(GPL)

NX&gt; 105

3. NX&gt; 105 is kind of like a shell prompt. Now you respond with the client version

type: hello NXCLIENT - Version 1.4.0

You will get the following response:

NX&gt; 105 hello NXCLIENT - Version 1.4.0

NX&gt; 134 Accepted protocol: 1.4.0

NX&gt; 105

4. I think the production client then sends the following:

SET SHELL_MODE SHELL

response:

NX&gt; 105 SET SHELL_MODE SHELL

NX&gt; 105

SET AUTH_MODE PASSWORD

NX&gt; 105 SET AUTH_MODE PASSWORD

NX&gt; 105

5. Then you send the login command

type: login

response:

NX&gt; 105 login

NX&gt; 101 User:

type: &lt;username&gt;

repsonse:

NX&gt; 102 Password:

type: &lt;your password&gt;

If you type &lt;enter&gt; instead, you will get the following from the commercial server (but not freenx)

NX&gt; 109 MD5 Password:

type: &lt;md5 of usernamepassword&gt;

You can get this password value by using the nxpassgen utility I have for moznx

response:

NX&gt; 103 Welcome to: &lt;host&gt; user: &lt;username&gt;

NX&gt; 105

6. Now you can request a session

type: startsession --session="&lt;session&gt;" --type="unix-kde" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cache="8M" --images="32M" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cookie="6726ad07a80d73c69a74c5f341b52a68" --link="adsl" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; render="1" --encryption="0" --backingstore="when_requested" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; imagecompressionmethod="2" --geometry="1024x768+188+118" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; keyboard="defkeymap" --kbtype="pc102/defkeymap" --media="0" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; agent_server="" --agent_user="" --agent_password="" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; screeninfo="1024x768x16+render"

For encrypted session, send --encryption="1"

note: I have always had trouble getting this to work and have to use '&amp;' as a delimeter instead of ' --'. It seems this issue is solved if you SET SHELL_MODE and SET AUTH_MODE as described above. I have not confirmed yet.

response:

NX&gt; 105 startsession --session="&lt;session&gt;" --type="unix-kde" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cache="8M" --images="32M" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cookie="6726ad07a80d73c69a74c5f341b52a68" --link="adsl" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; render="1" --encryption="0" --backingstore="when_requested" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; imagecompressionmethod="2" --geometry="1024x768+188+118" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; keyboard="defkeymap" --kbtype="pc102/defkeymap" --media="0" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; agent_server="" --agent_user="" --agent_password="" --

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; screeninfo="1024x768x16+render"

you can also just type startsession&lt;enter&gt; then the response will be

NX&gt; 106 Parameters:

Then you type all the parameters

You can replace startsession with restoresession if you want to restore an existing session. You add the additional attribute --id="&lt;session id you want to restore&gt;".

A good explanation of restoring sessions is here: http://www.nomachine.com/developers/archives/nxdevelopers/0323.php

7. Now the server sends back all of its parameters followed by a 105

NX&gt; 700 Session id: &lt;hostname&gt;-1058-CA3511103B37ADB2ABDAAF3EB510E99D

NX&gt; 705 Session display: 1058

NX&gt; 703 Session type: unix-kde

NX&gt; 701 Proxy cookie: A4BFD3EAE09B28A0EB0399A3EFD26392

NX&gt; 702 Proxy IP: 127.0.0.1

NX&gt; 706 Agent cookie: 6fff2cd4222776acd605d42fbb4bdfb5

NX&gt; 704 Session cache: unix-kde

NX&gt; 707 SSL tunneling: 0

NX&gt; 710 Session status: running

NX&gt; 105

For encrypted sessions, NX&gt; 707 SSL tunneling: 1

8. Now in another session invoke nxproxy with the proper parameters on the command line and in the options file.

nxproxy -S options=&lt;path to options file&gt;/options:&lt;Session display&gt;

for example above: nxproxy -S options=/.nx/S-hostname-1058-CA3511103B37ADB2ABDAAF3EB510E99D/options:1058

Then, in the options file:

nx,session=&lt;sesname&gt;,cookie=A4BFD3EAE09B28A0EB0399A3EFD26392,root=/.nx,id=hostname-1058-CA3511103B37ADB2ABDAAF3EB510E99D,listen=33057:1058

listen=&lt;port:display&gt; is only needed for encrypted sessions. Also, all these parameters can be sent on the command line instead of the options file.

For the listen=&lt;port:display&gt;, I always just hardcode a port number. I am not sure where the commercial client gets the port number. I have asked but not gotten a response.

9. Now back to our NXSSH session.

type 'bye'

Response:

999&gt; Bye

10. For encrypted sessions, now enter the switch command

type: NX&gt; 299 Switching connection to 127.0.0.1:33507 cookie: A4BFD3EAE09B28A0EB0399A3EFD26392

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/10/07/nxclient-develop.html](http://www.cnblogs.com/coderzh/archive/2010/10/07/nxclient-develop.html)**