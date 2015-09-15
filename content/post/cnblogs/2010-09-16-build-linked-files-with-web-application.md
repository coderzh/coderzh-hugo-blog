---
categories:
- 技术文章
date: '2010-09-16'
title: ASP.NET Web Application中使用链接文件
url: /2010/09/16/build-linked-files-with-web-application/

---


最近重构一个内部的平台系统，作为一个平台，其下有几个子系统，每个子系统有自己的网站系统。而每个网站使用的是统一的风格，统一的验证机制，反馈系统，等等。所以，为了避免几个子系统中重复出现相同的资源或文件，我打算将以前的ASP.NET Web Site全部转换为ASP.NET Web Application，然后通过链接外部公共文件的方式解决这个问题。同时：

1. Web Application是Web Site的升级产品。
2. Web Application允许添加链接方式，把其他目录的文件作为链接加入工程，更具备灵活性。
3. Web Application编译，构建，部署更加简单，快速，便捷。

当然，Web Application和Web Site还有很多不同的地方，比如：

1. Web Application有designer.cs文件，Web Site没有。
2. Web Application有命名空间，Web Site默认没有。
3. Web Application默认没有App_Code目录，需手工添加，且添加的cs文件默认属性为Content，需手工修改为Compile才加入编译。
...

等等。本文主要讲述，在ASP.NET Web Application中使用链接文件时，遇到的一些问题，以及解决办法。

首先，介绍一下将Web Site页面转换为Web Application页面的方法。如果了解了两者的区别，将会非常容易。主要分为几步：
1. 新建一个Web Application工程，将原Web Site页面添加到该工程中。
2. 在aspx.cs文件中，给类加上命名空间。同时，aspx文件头部的Inherits属性也加上命名空间。
3. 右键aspx文件或工程名，点击"Convert to Web Application"。这时，自动生成的designer.cs文件了。（aspx页面中的控件的定义。）

![](http://images.cnblogs.com/cnblogs_com/coderzh/convert-to-web-app.jpg)

好了，添加外部的链接文件：

![](http://images.cnblogs.com/cnblogs_com/coderzh/add-exist-item.jpg)

![](http://images.cnblogs.com/cnblogs_com/coderzh/addlink.jpg)

添加链接的文件很简单，也很方便。但是调试过程中，会遇到很大的麻烦。因为调试时，默认使用VS内置的Web Server，网站的根目录是源代码目录，调试时，遇到链接文件时，会因为找不到文件而出错。

而如果使用&#8221;publish&#8220;菜单发布网站时，会将链接的资源文件拷贝过去，这才是我们想要的。每次调试都需要进行发布，然后在本机的iis里设置虚拟目录，太麻烦了。

同时，我们希望通过MSBuild自动构建和发布网站，构建时也希望能自动的将链接的文件拷贝一份过去。MSBuild中编译ASP.NET Web Application工程的命令是：

<div class="cnblogs_code"><div><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">MSBuild&nbsp;</span><span style="color: #ff0000;">Projects</span><span style="color: #0000ff;">="d:\Demo\Web.csproj"</span><span style="color: #ff0000;">&nbsp;Targets</span><span style="color: #ff6600;">="</span><span style="color: #339966;">ResolveReferences;_CopyWebApplication;"</span><span style="color: #ff0000;">&nbsp;Properties</span><span style="color: #0000ff;">="WebProjectOutputDir=d:\Publish\;OutDir=d:\Publish\Bin\;Configuration=Release"</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">MSBuild</span><span style="color: #0000ff;">&gt;</span></div></div>
但是，上面的命令不会把链接的文件拷贝过去。这个问题困扰了我，难道要我写一个Copy的Task，自己将需要的文件拷贝过去？后来google了一下，发现也有人遇到我一样的问题，并且提供了一个绝佳的解决方案，同时解决了调试和发布的问题，真是太完美了！
<br />
方法是，修改csproj文件，重新定义默认的_CopyWebApplication Target，同时，增加拷贝链接文件的Target。将下面这段代码加入到csproj文件中：
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp; 
&nbsp; ============================================================
&nbsp;&nbsp;_CopyWebApplication
&nbsp;&nbsp;MODIFIED:&nbsp;Ignores&nbsp;linked&nbsp;files&nbsp;as&nbsp;part&nbsp;of&nbsp;normal&nbsp;deployment&nbsp;logic.&nbsp;
&nbsp;&nbsp;This&nbsp;target&nbsp;will&nbsp;copy&nbsp;the&nbsp;build&nbsp;outputs&nbsp;along&nbsp;with&nbsp;the
&nbsp;&nbsp;content&nbsp;files&nbsp;into&nbsp;a&nbsp;_PublishedWebsites&nbsp;folder.
&nbsp;&nbsp;This&nbsp;Task&nbsp;is&nbsp;only&nbsp;necessary&nbsp;when&nbsp;$(OutDir)&nbsp;has&nbsp;been&nbsp;redirected
&nbsp;&nbsp;to&nbsp;a&nbsp;folder&nbsp;other&nbsp;than&nbsp;~\bin&nbsp;such&nbsp;as&nbsp;is&nbsp;the&nbsp;case&nbsp;with&nbsp;Team&nbsp;Build.&nbsp; 
&nbsp; ============================================================
&nbsp;&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Target&nbsp;</span><span style="color: #ff0000;">Name</span><span style="color: #0000ff;">="_CopyWebApplication"</span><span style="color: #ff0000;">&nbsp;Condition</span><span style="color: #0000ff;">="'$(OutDir)'&nbsp;!=&nbsp;'$(OutputPath)'"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Log&nbsp;tasks&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Message&nbsp;</span><span style="color: #ff0000;">Text</span><span style="color: #0000ff;">="Copying&nbsp;Web&nbsp;Application&nbsp;Project&nbsp;Files&nbsp;for&nbsp;$(MSBuildProjectName)"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Create&nbsp;the&nbsp;_PublishedWebsites\app\bin&nbsp;folder&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">MakeDir&nbsp;</span><span style="color: #ff0000;">Directories</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Copy&nbsp;build&nbsp;outputs&nbsp;to&nbsp;_PublishedWebsites\app\bin&nbsp;folder&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(IntermediateAssembly)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(AddModules)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="$(IntermediateOutputPath)$(_SGenDllName)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\%(Content.SubFolder)%(Content.RecursiveDir)"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;Condition</span><span style="color: #0000ff;">="'$(_SGenDllCreated)'=='true'"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="$(IntermediateOutputPath)$(TargetName).pdb"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;Condition</span><span style="color: #0000ff;">="'$(_DebugSymbolsProduced)'=='true'"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(DocFileItem)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;Condition</span><span style="color: #0000ff;">="'$(_DocumentationFileProduced)'=='true'"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(IntermediateSatelliteAssembliesWithTargetPath)"</span><span style="color: #ff0000;">&nbsp;DestinationFiles</span><span style="color: #0000ff;">="@(IntermediateSatelliteAssembliesWithTargetPath-&gt;'$(WebProjectOutputDir)\bin\%(Culture)\$(TargetName).resources.dll')"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(ReferenceComWrappersToCopyLocal);&nbsp;@(ResolvedIsolatedComModules);&nbsp;@(_DeploymentLooseManifestFile);&nbsp;@(NativeReferenceFile)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;copy&nbsp;any&nbsp;referenced&nbsp;assemblies&nbsp;to&nbsp;_PublishedWebsites\app\bin&nbsp;folder&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">SourceFiles</span><span style="color: #0000ff;">="@(ReferenceCopyLocalPaths)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\bin"</span><span style="color: #ff0000;">&nbsp;SkipUnchangedFiles</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;MODIFICATION&nbsp;HERE:&nbsp;Copy&nbsp;local&nbsp;content&nbsp;files&nbsp;(i.e.&nbsp;non-linked&nbsp;files)&nbsp;recursively&nbsp;to&nbsp;_PublishedWebsites\app\&nbsp;folder&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">Condition</span><span style="color: #0000ff;">="&nbsp;'%(Content.Link)'&nbsp;==&nbsp;''&nbsp;"</span><span style="color: #ff0000;">&nbsp;SourceFiles</span><span style="color: #0000ff;">="%(Content.Identity)"</span><span style="color: #ff0000;">&nbsp;DestinationFolder</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\%(Content.RelativeDir)"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">Target</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">
============================================================
&nbsp;&nbsp;CopyLinkedContentFiles
&nbsp;&nbsp;A&nbsp;new&nbsp;target&nbsp;to&nbsp;copy&nbsp;any&nbsp;linked&nbsp;content&nbsp;files&nbsp;into&nbsp;the
&nbsp;&nbsp;web&nbsp;application&nbsp;output&nbsp;folder.&nbsp;
&nbsp;&nbsp;NOTE:&nbsp;This&nbsp;is&nbsp;necessary&nbsp;even&nbsp;when&nbsp;'$(OutDir)'&nbsp;has&nbsp;not&nbsp;been&nbsp;redirected.
============================================================
&nbsp;&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Target&nbsp;</span><span style="color: #ff0000;">Name</span><span style="color: #0000ff;">="CopyLinkedContentFiles"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Remove&nbsp;any&nbsp;old&nbsp;copies&nbsp;of&nbsp;the&nbsp;files&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Delete&nbsp;</span><span style="color: #ff0000;">Condition</span><span style="color: #0000ff;">="&nbsp;'%(Content.Link)'&nbsp;!=&nbsp;''&nbsp;AND&nbsp;Exists('$(WebProjectOutputDir)\%(Content.Link)')&nbsp;"</span><span style="color: #ff0000;">&nbsp;Files</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\%(Content.Link)"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Copy&nbsp;linked&nbsp;content&nbsp;files&nbsp;recursively&nbsp;to&nbsp;the&nbsp;project&nbsp;folder&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">Copy&nbsp;</span><span style="color: #ff0000;">Condition</span><span style="color: #0000ff;">="&nbsp;'%(Content.Link)'&nbsp;!=&nbsp;''&nbsp;"</span><span style="color: #ff0000;">&nbsp;SourceFiles</span><span style="color: #0000ff;">="%(Content.Identity)"</span><span style="color: #ff0000;">&nbsp;DestinationFiles</span><span style="color: #0000ff;">="$(WebProjectOutputDir)\%(Content.Link)"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">Target</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;Override&nbsp;the&nbsp;default&nbsp;target&nbsp;dependencies&nbsp;to&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">&nbsp;include&nbsp;the&nbsp;new&nbsp;_CopyLinkedContentFiles&nbsp;target.&nbsp;</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">PropertyGroup</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">PrepareForRunDependsOn</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$(PrepareForRunDependsOn);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_CopyWebApplication;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CopyLinkedContentFiles;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_BuiltWebOutputGroupOutput
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">PrepareForRunDependsOn</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">PropertyGroup</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">Project</span><span style="color: #0000ff;">&gt;</span></div></div>
其实就是写了一些通用的Copy，而不必手工指定哪些需要拷贝。然后，在MSBuild脚本中，增加CopyLinkedContentFiles Target：

<div class="cnblogs_code"><div><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">MSBuild&nbsp;</span><span style="color: #ff0000;">Projects</span><span style="color: #0000ff;">="D:\Demo\Web.csproj"</span><span style="color: #ff0000;">&nbsp;Targets</span><span style="color: #0000ff;">="</span>**<span style="color: #339966;">ResolveReferences;_CopyWebApplication;CopyLinkedContentFiles<span style="color: #0000ff;">"</span></span>**<span style="color: #ff0000;">&nbsp;Properties</span><span style="color: #0000ff;">="WebProjectOutputDir=D:\Publish\;OutDir=D:\Publish\Bin\;Configuration=Release"</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">MSBuild</span><span style="color: #0000ff;">&gt;</span></div></div>
搞定！这时MSBuild编译出来的文件将会包括所有我们需要的文件了。同时，在VS里点击&#8221;Build&#8220;编译，会将链接的文件也复制一份过来源码目录，这样就能非常方便的使用内置的Web Server进行调试了！ 
<br />
参考链接：  
[http://consultingblogs.emc.com/jamesdawson/archive/2008/06/03/using-linked-files-with-web-application-projects.aspx](http://consultingblogs.emc.com/jamesdawson/archive/2008/06/03/using-linked-files-with-web-application-projects.aspx)

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/09/16/build-linked-files-with-web-application.html](http://www.cnblogs.com/coderzh/archive/2010/09/16/build-linked-files-with-web-application.html)**