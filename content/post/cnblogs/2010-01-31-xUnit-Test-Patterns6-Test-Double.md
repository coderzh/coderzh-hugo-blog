---
categories:
- 技术文章
- 读书笔记
date: '2010-01-31'
title: 《xUnit Test Patterns》学习笔记6 - Test Double
url: /2010/01/31/xUnit-Test-Patterns6-Test-Double/

---


我不知道Test Double翻译成中文是什么，测试替身？Test Double就像是陈龙大哥电影里的替身，起到以假乱真的作用。在单元测试时，使用Test Double减少对被测对象的依赖，使得测试更加单一，同时，让测试案例执行的时间更短，运行更加稳定，同时能对SUT内部的输入输出进行验证，让测试更加彻底深入。但是，Test Double也不是万能的，Test Double不能被过度使用，因为实际交付的产品是使用实际对象的，过度使用Test Double会让测试变得越来越脱离实际。

我感觉，Test Double这玩意比较适合在Java，C#等完全面向对象的语言中使用。并且需要很好的使用依赖注入([Dependency injection](http://en.wikipedia.org/wiki/Dependency_injection))设计。如果被测系统是使用C或C++开发，使用Test Double将是一个非常困难和痛苦的事情。

要理解Test Double，必须非常清楚以下几个东西的关系，本文的重点也是说明一下他们之间的关系。他们分别是：

1.  Dummy Object
2.  Test Stub
3.  Test Spy
4.  Mock Object
5.  Fake Object  
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_thumb.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_2.png) 

#### Dummy Object

Dummy Objects泛指在测试中必须传入的对象，而传入的这些对象实际上并不会产出任何作用，仅仅是为了能够调用被测对象而必须传入的一个东西。

使用Dummy Object的例子：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testInvoice_addLineItem_DO()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ﬁnal&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;QUANTITY&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product&nbsp;product&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Product(</span><span style="color: #000000;">"</span><span style="color: red;">Dummy&nbsp;Product&nbsp;Name</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getUniqueNumber());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invoice&nbsp;inv&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Invoice(&nbsp;</span><span style="color: red;">new</span><span style="color: red;">&nbsp;DummyCustomer()</span><span style="color: #000000;">&nbsp;);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;expItem&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;LineItem(inv,&nbsp;product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inv.addItemQuantity(product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List&nbsp;lineItems&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;inv.getLineItems();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">number&nbsp;of&nbsp;items</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;lineItems.size(),&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;actual&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertLineItemsEqual(</span><span style="color: #000000;">""</span><span style="color: #000000;">,&nbsp;expItem,&nbsp;actual);
}</span></div></div>

&nbsp;

#### Test Stub

测试桩是用来接受SUT内部的间接输入(indirect inputs)，并返回特定的值给SUT。可以理解Test Stub是在SUT内部打的一个桩，可以按照我们的要求返回特定的内容给SUT，Test Stub的交互完全在SUT内部，因此，它不会返回内容给测试案例，也不会对SUT内部的输入进行验证。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_thumb_1.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_4.png) 

使用Test Stub的例子：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testDisplayCurrentTime_exception()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Fixture&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;Testing&nbsp;with&nbsp;Doubles&nbsp;</span><span style="color: #000000;">136</span><span style="color: #000000;">&nbsp;Chapter&nbsp;</span><span style="color: #000000;">11</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;Using&nbsp;Test&nbsp;Doubles
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;Deﬁne&nbsp;and&nbsp;instantiate&nbsp;Test&nbsp;Stub</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">TimeProvider&nbsp;testStub&nbsp;</span><span style="color: red;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: red;">new</span><span style="color: red;">&nbsp;TimeProvider()
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;</span><span style="color: red;">//</span><span style="color: red;">&nbsp;Anonymous&nbsp;inner&nbsp;Test&nbsp;Stub</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">public</span><span style="color: red;">&nbsp;Calendar&nbsp;getTime()&nbsp;</span><span style="color: red;">throws</span><span style="color: red;">&nbsp;TimeProviderEx&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">throw</span><span style="color: #000000;">&nbsp;</span><span style="color: red;">new</span><span style="color: red;">&nbsp;TimeProviderEx(</span><span style="color: red;">"</span><span style="color: red;">Sample</span><span style="color: red;">"</span><span style="color: red;">);
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};</span><span style="color: red;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;Instantiate&nbsp;SUT</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimeDisplay&nbsp;sut&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;TimeDisplay();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sut.setTimeProvider(testStub);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise&nbsp;SUT</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;sut.getCurrentTimeAsHtmlFragment();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify&nbsp;direct&nbsp;output</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String&nbsp;expectedTimeString&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">&lt;span&nbsp;class=\</span><span style="color: #000000;">"</span><span style="color: #000000;">error\</span><span style="color: #000000;">"</span><span style="color: #000000;">&gt;Invalid&nbsp;Time&lt;/span&gt;</span><span style="color: #000000;">"</span><span style="color: #000000;">;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">Exception</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;expectedTimeString,&nbsp;result);
}</span></div></div>

&nbsp;

#### Test Spy

Test Spy像一个间谍，安插在了SUT内部，专门负责将SUT内部的间接输出(indirect outputs)传到外部。它的特点是将内部的间接输出返回给测试案例，由测试案例进行验证，<font color="#ff0000">Test Spy只负责获取内部情报，并把情报发出去，不负责验证情报的正确性</font>。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_thumb_2.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_6.png) 

使用Test Spy的例子：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testRemoveFlightLogging_recordingTestStub()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Fixture&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightDto&nbsp;expectedFlightDto&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;createAnUnregFlight();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightManagementFacade&nbsp;facade&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;FlightManagementFacadeImpl();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;Double&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">AuditLogSpy&nbsp;logSpy&nbsp;</span><span style="color: red;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: red;">new</span><span style="color: red;">&nbsp;AuditLogSpy();</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.setAuditLog(logSpy);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.removeFlight(expectedFlightDto.getFlightNumber());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify&nbsp;state</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertFalse(</span><span style="color: #000000;">"</span><span style="color: #000000;">ﬂight&nbsp;still&nbsp;exists&nbsp;after&nbsp;being&nbsp;removed</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.ﬂightExists(&nbsp;expectedFlightDto.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getFlightNumber()));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify&nbsp;indirect&nbsp;outputs&nbsp;using&nbsp;retrieval&nbsp;interface&nbsp;of&nbsp;spy</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">number&nbsp;of&nbsp;calls</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">logSpy.getNumberOfCalls()</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">action&nbsp;code</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Helper.REMOVE_FLIGHT_ACTION_CODE,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">logSpy.getActionCode()</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">date</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;helper.getTodaysDateWithoutTime(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">logSpy.getDate()</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">user</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;Helper.TEST_USER_NAME,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">logSpy.getUser()</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">detail</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expectedFlightDto.getFlightNumber(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">logSpy.getDetail()</span><span style="color: #000000;">);
}</span></div></div>

#### Mock Object

Mock Object和Test Spy有类似的地方，它也是安插在SUT内部，获取到SUT内部的间接输出(indirect outputs)，不同的是，<font color="#ff0000">Mock Object还负责对情报(indirect outputs)进行验证</font>，总部(外部的测试案例)信任Mock Object的验证结果。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_thumb_3.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns6TestDouble_106E8/image_8.png) 

Mock的测试框架有很多，比如：NMock，JMock等等。如果使用Mock Object，建议使用现成的Mock框架，因为框架为我们做了很多琐碎的事情，我们只需要对Mock对象进行一些描述。比如，通常Mock框架都会使用基于行为(Behavior)的描述性调用方法，即，在调用SUT前，只需要描述Mock对象预期会接收什么参数，会执行什么操作，返回什么内容等，这样的案例更加具有可读性。比如下面使用Mock的测试案例：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testRemoveFlight_Mock()&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Fixture&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightDto&nbsp;expectedFlightDto&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;createAnonRegFlight();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Mock&nbsp;conﬁguration</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">ConﬁgurableMockAuditLog&nbsp;mockLog&nbsp;</span><span style="color: red;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">new</span><span style="color: red;">&nbsp;ConﬁgurableMockAuditLog();
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mockLog.setExpectedLogMessage(
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;helper.getTodaysDateWithoutTime(),
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Helper.TEST_USER_NAME,
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Helper.REMOVE_FLIGHT_ACTION_CODE,
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expectedFlightDto.getFlightNumber());
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mockLog.setExpectedNumberCalls(</span><span style="color: red;">1</span><span style="color: red;">);</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Mock&nbsp;installation</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightManagementFacade&nbsp;facade&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;FlightManagementFacadeImpl();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.setAuditLog(mockLog);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.removeFlight(expectedFlightDto.getFlightNumber());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertFalse(</span><span style="color: #000000;">"</span><span style="color: #000000;">ﬂight&nbsp;still&nbsp;exists&nbsp;after&nbsp;being&nbsp;removed</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.ﬂightExists(&nbsp;expectedFlightDto.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getFlightNumber()));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mockLog.verify();
}</span></div></div>  

#### 
Fake Object

经常，我们会把Fake Object和Test Stub搞混，因为它们都和外部没有交互，对内部的输入输出也不进行验证。不同的是，<font color="#ff0000">Fake Object并不关注SUT内部的间接输入(indirect inputs)或间接输出(indirect outputs)，它仅仅是用来替代一个实际的对象，并且拥有几乎和实际对象一样的功能，保证SUT能够正常工作</font>。实际对象过分依赖外部环境，Fake Object可以减少这样的依赖。需要使用Fake Object通常符合以下情形：

1.  实际对象还未实现出来，先用一个简单的Fake Object代替它。
2.  实际对象执行需要太长的时间
3.  实际对象在实际环境下可能会有不稳定的情况。比如，网络发送数据包，不能保证每次都能成功发送。
4.  实际对象在实际系统环境下不可用，或者很难让它变得可用。比如，使用一个依赖实际数据库的数据库访问层对象，必须安装数据库，并且进行大量的配置，才能生效。  

一个使用Fake Object的例子是，将一个依赖实际数据库的数据库访问层对象替换成一个基于内存，使用Hash Table对数据进行管理的数据访问层对象，它具有和实际数据库访问层一样的接口实现。
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;InMemoryDatabase&nbsp;</span><span style="color: #0000ff;">implements</span><span style="color: #000000;">&nbsp;</span><span style="color: red;">FlightDao{</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">private</span><span style="color: #000000;">&nbsp;List&nbsp;airports&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Vector();
&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;Airport&nbsp;</span><span style="color: red;">createAirport</span><span style="color: #000000;">(String&nbsp;airportCode,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String&nbsp;name,&nbsp;String&nbsp;nearbyCity)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;DataException,&nbsp;InvalidArgumentException&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertParamtersAreValid(&nbsp;&nbsp;airportCode,&nbsp;name,&nbsp;nearbyCity);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertAirportDoesntExist(&nbsp;airportCode);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Airport&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Airport(getNextAirportId(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;airportCode,&nbsp;name,&nbsp;createCity(nearbyCity));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;airports.add(result);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;result;
&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;Airport&nbsp;</span><span style="color: red;">getAirportByPrimaryKey</span><span style="color: #000000;">(BigDecimal&nbsp;airportId)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;DataException,&nbsp;InvalidArgumentException&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertAirportNotNull(airportId);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Airport&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">null</span><span style="color: #000000;">;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterator&nbsp;i&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;airports.iterator();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">while</span><span style="color: #000000;">&nbsp;(i.hasNext())&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Airport&nbsp;airport&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(Airport)&nbsp;i.next();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;(airport.getId().equals(airportId))&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;airport;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throw</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;DataException(</span><span style="color: #000000;">"</span><span style="color: #000000;">Airport&nbsp;not&nbsp;found:</span><span style="color: #000000;">"</span><span style="color: #000000;">+</span><span style="color: #000000;">airportId);
}</span></div></div>

说了这么多，可能更加糊涂了。在实际使用时，并不需要过分在意使用的是哪种Test Double。当然，作为思考，可以想一想，以前测试过程中做的一些所谓的&#8220;假的&#8221;东西，到底是Dummy Object, Test Stub, Test Spy, Mock Object, 还是Fake Object呢？

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/31/xUnit-Test-Patterns6-Test-Double.html](http://www.cnblogs.com/coderzh/archive/2010/01/31/xUnit-Test-Patterns6-Test-Double.html)**
