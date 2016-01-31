---
categories:
- 技术文章
- 读书笔记
date: '2010-01-24'
title: 《xUnit Test Patterns》学习笔记5 - xUnit基础
url: /2010/01/24/xUnit-Test-Patterns-5/

---


这几节我看的比较快一些，因为内容之间其实是有联系的，所以合在一起做一个笔记。6-10节主要介绍了什么是Fixture，如何保证一个Fresh Fixture，如何使用Setup，Tearndown，如何进行验证(Verify)，等等。

#### 什么是Fixture？

<font color="#ff0000">The test ﬁxture is everything we need to have in place to exercise the SUT.</font>

从作者的英文解释来看，Fixture确实是一个比较难定义的东西，所以作者用了everything这个词。

#### 什么是Fresh Fixture？

一个测试案例一般都包含以下几个步骤：

1.  Setup
2.  Exercise
3.  Verify
4.  Teardown  

Fresh Fixture是指每个案例执行时，都会生成一个全新的Fixture，好处是不受其他案例的影响。避免了Interacting Tests(之前有提到的)。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_thumb.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_2.png) 

#### 什么是Setup？

Setup是案例的准备阶段，主要有三种实现方式：In-line Fixture Setup, Delegated Setup, Implicit Setup。推荐使用的是Implicit Setup。

**In-line Fixture Setup**

直接在测试方法内部做一些具体的Setup操作 ：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testStatus_initial()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;In-line&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Airport&nbsp;departureAirport&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Airport(</span><span style="color: #000000;">"</span><span style="color: #000000;">Calgary</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">YYC</span><span style="color: #000000;">"</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Airport&nbsp;destinationAirport&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Airport(</span><span style="color: #000000;">"</span><span style="color: #000000;">Toronto</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">YYZ</span><span style="color: #000000;">"</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flight&nbsp;ﬂight&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Flight(&nbsp;ﬂightNumber,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;departureAirport,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinationAirport);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise&nbsp;SUT&nbsp;and&nbsp;verify&nbsp;outcome</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(FlightState.PROPOSED,&nbsp;ﬂight.getStatus());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;tearDown:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;&nbsp;Garbage-collected</span><span style="color: #008000;">
</span><span style="color: #000000;">}</span></div></div>

缺点是容易造成很多重复的代码，不易维护。

**Delegated Setup**

相比In-line Fixture Setup，将里面具体的Setup操作提取出来，作为一个公用的方法，提高了复用性。
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testGetStatus_inital()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flight&nbsp;ﬂight&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;createAnonymousFlight();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise&nbsp;SUT&nbsp;and&nbsp;verify&nbsp;outcome</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(FlightState.PROPOSED,&nbsp;ﬂight.getStatus());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Teardown
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Garbage-collected</span><span style="color: #008000;">
</span><span style="color: #000000;">}</span></div></div>

**Implicit Setup**

几乎所有的xUnit家族的框架都支持SetUp，比如，使用Google Test中指定的函数名SetUp，NUnit使用[Setup]Attribute。这种方法，不需要我们自己去调用Setup方法，框架会在创建Fresh Fixture后调用Setup。因此，我们只管实现SetUp方法。
  <div class="cnblogs_code"><div><span style="color: #000000;">Airport&nbsp;departureAirport;
Airport&nbsp;destinationAirport;
Flight&nbsp;ﬂight;
</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testGetStatus_inital()&nbsp;{
&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Implicit&nbsp;setup
&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise&nbsp;SUT&nbsp;and&nbsp;verify&nbsp;outcome</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;assertEquals(FlightState.PROPOSED,&nbsp;ﬂight.getStatus());
}
</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;setUp()&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception{
&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">super</span><span style="color: #000000;">.setUp();&nbsp;
&nbsp;&nbsp;&nbsp;departureAirport&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Airport(</span><span style="color: #000000;">"</span><span style="color: #000000;">Calgary</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">YYC</span><span style="color: #000000;">"</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;destinationAirport&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Airport(</span><span style="color: #000000;">"</span><span style="color: #000000;">Toronto</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">YYZ</span><span style="color: #000000;">"</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;BigDecimal&nbsp;ﬂightNumber&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;BigDecimal(</span><span style="color: #000000;">"</span><span style="color: #000000;">999</span><span style="color: #000000;">"</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;ﬂight&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Flight(&nbsp;ﬂightNumber&nbsp;,&nbsp;departureAirport,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinationAirport);
}
</span></div></div>

#### 
什么是Teardown？

为了保证每个案例都拥有一个Fresh Fixture，必须在案例的结束时做一些清理操作，这就是Teardown。和Setup一样，Teardown也有三种实现方式：In-line Fixture Teardown, Delegated Teardown, Implicit Teardown。同样，推荐使用Implicit Teardown。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_thumb_5.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_12.png) 

#### 
什么是Shared Fixture？

多个测试方法共用一个Fixture，这时，Setup只会在第一个测试方法执行时被执行。gtest中，同时还拥有一个公共的TearDownTestCases方法。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_thumb_6.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_14.png) 

#### 
Result Verification

前面说过，测试案例必须拥有Self-Checking的能力。Verification分两种：State Verification和Behavior Verification。

**State Verification**

执行SUT后，验证SUT的状态：
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_thumb_7.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_16.png) 

验证时，可以使用Build-in Assertions，比如xUnit框架提供的assertTrue, assertEquals等方法。或者Custom Assertion等等。

**Behavior Verification**

不仅仅验证SUT的状态，同时还对SUT的行为对外部因素造成的影响进行验证。
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_thumb_8.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns5xUnit_D75E/image_18.png) 

比如下面这个例子：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testRemoveFlightLogging_recordingTestStub()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;ﬁxture&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightDto&nbsp;expectedFlightDto&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;createAnUnregFlight();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightManagementFacade&nbsp;facade&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;FlightManagementFacadeImpl();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;Double&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AuditLogSpy&nbsp;logSpy&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;AuditLogSpy();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.setAuditLog(logSpy);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.removeFlight(expectedFlightDto.getFlightNumber());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;verify</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">number&nbsp;of&nbsp;calls</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logSpy.getNumberOfCalls());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">action&nbsp;code</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Helper.REMOVE_FLIGHT_ACTION_CODE,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logSpy.getActionCode());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">date</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;helper.getTodaysDateWithoutTime(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logSpy.getDate());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">user</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;Helper.TEST_USER_NAME,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logSpy.getUser());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">detail</span><span style="color: #000000;">"</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expectedFlightDto.getFlightNumber(),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logSpy.getDetail());
}</span></div></div>  

除此之外，我们还可以使用一些Mock框架，使用基于行为的验证方式，这种方式，不需要我们显式的调用验证的方法。(Expected Behaivor Specification)
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testRemoveFlight_JMock()&nbsp;</span><span style="color: #0000ff;">throws</span><span style="color: #000000;">&nbsp;Exception&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;ﬁxture&nbsp;setup</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightDto&nbsp;expectedFlightDto&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;createAnonRegFlight();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FlightManagementFacade&nbsp;facade&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;FlightManagementFacadeImpl();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;mock&nbsp;conﬁguration</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mock&nbsp;mockLog&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;mock(AuditLog.</span><span style="color: #0000ff;">class</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">mockLog.expects(once()).method(</span><span style="color: red;">"</span><span style="color: red;">logMessage</span><span style="color: red;">"</span><span style="color: red;">)
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.with(eq(helper.getTodaysDateWithoutTime()),
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eq(Helper.TEST_USER_NAME),
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eq(Helper.REMOVE_FLIGHT_ACTION_CODE),
</span><span style="color: red;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eq(expectedFlightDto.getFlightNumber()));</span><span style="color: red;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;mock&nbsp;installation</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.setAuditLog((AuditLog)&nbsp;mockLog.proxy());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facade.removeFlight(expectedFlightDto.getFlightNumber());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;verify
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;verify()&nbsp;method&nbsp;called&nbsp;automatically&nbsp;by&nbsp;JMock</span><span style="color: #008000;">
</span><span style="color: #000000;">}</span></div></div>  

#### 
如何使测试代码变得简洁，减少重复？

**Expected Object**

需要比较对象内部很多属性时，使用对象比较会更简单。

原有案例代码：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testInvoice_addLineItem7()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;expItem&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;LineItem(inv,&nbsp;product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inv.addItemQuantity(product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List&nbsp;lineItems&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;inv.getLineItems();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;actual&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(expItem.getInv(),&nbsp;actual.getInv());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(expItem.getProd(),&nbsp;actual.getProd());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(expItem.getQuantity(),&nbsp;actual.getQuantity());
}</span></div></div>  

改进后：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;testInvoice_addLineItem8()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;expItem&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;LineItem(inv,&nbsp;product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Exercise</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inv.addItemQuantity(product,&nbsp;QUANTITY);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;Verify</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List&nbsp;lineItems&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;inv.getLineItems();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;actual&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">assertEquals(</span><span style="color: red;">"</span><span style="color: red;">Item</span><span style="color: red;">"</span><span style="color: red;">,&nbsp;expItem,&nbsp;actual);</span><span style="color: #000000;">
}</span></div></div>

&nbsp;

**Custom Assersions**

需要验证的细节很多时，可以自己定义一个Assersion，隐藏掉这些细节。比如：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">static</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;assertLineItemsEqual(
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String&nbsp;&nbsp;msg,&nbsp;LineItem&nbsp;exp,&nbsp;LineItem&nbsp;act)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals&nbsp;(msg</span><span style="color: #000000;">+</span><span style="color: #000000;">"</span><span style="color: #000000;">&nbsp;Inv</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;&nbsp;exp.getInv(),&nbsp;act.getInv());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals&nbsp;(msg</span><span style="color: #000000;">+</span><span style="color: #000000;">"</span><span style="color: #000000;">&nbsp;Prod</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;exp.getProd(),&nbsp;act.getProd());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals&nbsp;(msg</span><span style="color: #000000;">+</span><span style="color: #000000;">"</span><span style="color: #000000;">&nbsp;Quan</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;exp.getQuantity(),&nbsp;act.getQuantity());
}</span></div></div>

&nbsp;

**Verification Methods**

和Custom Asserions很像，唯一不同的是，Custom Assertion只包含验证的代码，Verification Methods同时还包含对SUT的操作。比如：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;assertInvoiceContainsOnlyThisLineItem(
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invoice&nbsp;inv,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;expItem)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: red;">List&nbsp;lineItems&nbsp;</span><span style="color: red;">=</span><span style="color: red;">&nbsp;inv.getLineItems();</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">number&nbsp;of&nbsp;items</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;lineItems.size(),&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LineItem&nbsp;actual&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertLineItemsEqual(</span><span style="color: #000000;">""</span><span style="color: #000000;">,expItem,&nbsp;actual);
}</span></div></div>

&nbsp;

**Parameterized and Data-Driven Tests**

对于测试逻辑一致，只是测试数据有不同的测试案例，适合使用参数化测试，或者叫数据驱动测试。比如，Google Test就很好的提供了参数化的测试，见：
  
[玩转 Google开源C++单元测试框架Google Test系列(gtest)之四 - 参数化](http://www.cnblogs.com/coderzh/archive/2009/04/08/1431297.html)

通过参数化，可以简化测试代码，不需要为大量不同的输入数据分别编写测试案例。

#### Avoiding Conditional Test Logic

验证时，不要使用一些条件相关的逻辑！比如，<span style="color: red;">不要使用if</span>, loop之类的语句！下面是一个例子：

使用if的情况：
  <div class="cnblogs_code"><div><span style="color: #000000;">List&nbsp;lineItems&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;invoice.getLineItems();
</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;(lineItems.size()&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">)&nbsp;{
&nbsp;&nbsp;&nbsp;LineItem&nbsp;expected&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;LineItem(invoice,&nbsp;product,</span><span style="color: #000000;">5</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;BigDecimal(</span><span style="color: #000000;">"</span><span style="color: #000000;">30</span><span style="color: #000000;">"</span><span style="color: #000000;">),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;BigDecimal(</span><span style="color: #000000;">"</span><span style="color: #000000;">69.96</span><span style="color: #000000;">"</span><span style="color: #000000;">));
&nbsp;&nbsp;&nbsp;LineItem&nbsp;actItem&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)&nbsp;lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">invoice</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;expected,&nbsp;actItem);
}&nbsp;</span><span style="color: #0000ff;">else</span><span style="color: #000000;">&nbsp;{
&nbsp;&nbsp;&nbsp;fail(</span><span style="color: #000000;">"</span><span style="color: #000000;">Invoice&nbsp;should&nbsp;have&nbsp;exactly&nbsp;one&nbsp;line&nbsp;item</span><span style="color: #000000;">"</span><span style="color: #000000;">);
}</span></div></div>

可以看出，上面的写法是不好的，验证中有逻辑判断意味着有可能案例不够单一，使得案例难以理解。因此，比较好的是改成下面的方式：
  <div class="cnblogs_code"><div><span style="color: #000000;">List&nbsp;lineItems&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;invoice.getLineItems();
</span><span style="color: red;">assertEquals(</span><span style="color: red;">"</span><span style="color: red;">number&nbsp;of&nbsp;items</span><span style="color: red;">"</span><span style="color: red;">,&nbsp;lineItems.size(),&nbsp;</span><span style="color: red;">1</span><span style="color: red;">);</span><span style="color: #000000;">
LineItem&nbsp;expected&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;LineItem(invoice,&nbsp;product,&nbsp;</span><span style="color: #000000;">5</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;BigDecimal(</span><span style="color: #000000;">"</span><span style="color: #000000;">30</span><span style="color: #000000;">"</span><span style="color: #000000;">),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;BigDecimal(</span><span style="color: #000000;">"</span><span style="color: #000000;">69.96</span><span style="color: #000000;">"</span><span style="color: #000000;">));
LineItem&nbsp;actItem&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(LineItem)&nbsp;lineItems.get(</span><span style="color: #000000;">0</span><span style="color: #000000;">);
assertEquals(</span><span style="color: #000000;">"</span><span style="color: #000000;">invoice</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;expected,&nbsp;actItem);</span></div></div>

&nbsp;

#### Working Backward

一个编写测试案例的小技巧或者说是习惯吧，就是<span style="color: red;">实现一个测试案例时，从最后一行开始写起</span>，比如，先写Assertions。可以一试。

#### Using Test-Driven Development to Write Test Utility Method

我们经常实现一些测试用的辅助方法，这些方法在实现过程中，使用TDD的方式去实现，编写一些简单的测试案例，保证辅助方法也是正确的。也就是说，<span style="color: red;">测试案例代码本身也是需要被测试的。</span>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/24/xUnit-Test-Patterns-5.html](http://www.cnblogs.com/coderzh/archive/2010/01/24/xUnit-Test-Patterns-5.html)**
