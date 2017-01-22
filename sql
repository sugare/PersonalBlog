标题
日期
文章
访问量


CREATE DATABASE blog DEFAULT CHARACTER SET utf8;
USE blog;
CREATE TABLE blog(
`id` int not null primary key,
`title` varchar(100) not null,
`date` DATE not null,
`essay` MEDIUMTEXT,
`view` int not null default 0
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE test(
`id` int not null primary key,
`title` char(100) not null,
`date` DATE not null,
`essay` char(100),
`view` int not null default 0
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
insert into test(id,title,date, essay, view) values(1, '集群的相关内容','2017-01-01','1234566', '10');



<h3>一、集群的定义</h3>

<p style="letter-spacing:2px;font-family:'楷体';">集群是一种并行或分布式系统，该系统包括一个互连的整体计算机集合作为一种单一、统一的计算机资源使用。通过集群技术，我们可以在付出低成本的情况下获得在性能、可靠性、灵活性方面更高的利益。
计算机集群简称集群，是一组计算机系统，它通过一组松散集成的计算机软件和硬件连接起来，高度紧密地协作完成计算相关工作。
集群，是指一组相互独立的计算机，利用高速通信网络组成的一个计算机系统，每个集群节点（即集群中的每台计算机）都是运行其在即进程的一个独立服务器。这些进程可以彼此通信，对网络客户机来说就像形成了一个单一系统，协同起来向用户提供应用程序、系统资源和数据，并以单一系统的模式加以管理。一个客户与集群相互作用时，集群像是一个独立的服务器。</p>
<p>集群是一种并行或分布式系统，该系统包括一个互连的整体计算机集合作为一种单一、统一的计算机资源使用。通过集群技术，我们可以在付出低成本的情况下获得在性能、可靠性、灵活性方面更高的利益。
计算机集群简称集群，是一组计算机系统，它通过一组松散集成的计算机软件和硬件连接起来，高度紧密地协作完成计算相关工作。
集群，是指一组相互独立的计算机，利用高速通信网络组成的一个计算机系统，每个集群节点（即集群中的每台计算机）都是运行其在即进程的一个独立服务器。这些进程可以彼此通信，对网络客户机来说就像形成了一个单一系统，协同起来向用户提供应用程序、系统资源和数据，并以单一系统的模式加以管理。一个客户与集群相互作用时，集群像是一个独立的服务器。</p>

<h3>二、集群的基本特点</h3>
<p style="background-color: rgba(128,128,128,0.15);font-style: inherit;letter-spacing:2px;font-family: '微软雅黑';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.高性能
一些计算密集型应用，如天气预报、核试验模拟等，需要计算机要有很强的运算处理能力，现有的技术，即使普通的大型机其计算也很难胜任。这时，一般使用集群，集中多台计算机的运算能力来满足
2.低成本
通常一套集群配置，只需要若干台服务器主机即可。与价值上百万的专用超级计算机相比便宜了很多。
3.高可扩展性
通常情况下，用户若想扩展系统能力，不得不购买更高性能服务器，才能获得额外所需的CPU和存储器。若采用集群，只需将新的单个服务器加入现有集群中即可，
4.高可靠性
集群技术使系统在故障发生时扔可以继续工作，将系统停机时间减到最小。</p>

<h3>三、集群的分类</h3>

<p style="font: 12px/1.5 Tahoma,Helvetica,Arial,'宋体',sans-serif;">负载均衡集群（LB）
负载均衡集群为企业提供了更为实用、性价比更高的系统解决方案。负载均衡集群使客户访问请求压力及负载可以在计算机集群中尽可能平均地分摊处理。负载通常包括应用程序处理负载和网络流量负载。这样的系统非常适合向使用同一组应用程序的大量用户提供服务。每个节点都可以承担一定的访问请求负载压力，并且可以实现访问请求在个点之间动态分配，以实现负载均衡。
负载均衡集群运行时，一般通过一个或者多个前端负载均衡器将客户访问请求分发到后端的一组服务器上，从而达到整个系统的高性能和高可用性。这样的计算机集群有时也被称为服务器集群。一般高可用性集群和负载均衡集群会使用类似的技术，或同时具有高可用性与负载均衡的特点。
负载均衡的作用：</p>


<p style="font-family: 'Arial','Microsoft YaHei','黑体','宋体',sans-serif;">分担用户访问请求或数据流量</p>
<p style="font: 14px/1.5 'Microsoft YaHei',arial,tahoma,\5b8b\4f53,sans-serif;">分担用户访问请求或数据流量</p>
<p style="font: 12px/1 Tahoma,Helvetica,Arial,'\5b8b\4f53',sans-serif;">分担用户访问请求或数据流量</p>
<p style="font-family:Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', 微软雅黑, Arial, sans-serif;">分担用户访问请求或数据流量</p>
<p style="font: 12px/1 Tahoma,Helvetica,Arial,'\5b8b\4f53',sans-serif;">分担用户访问请求或数据流量</p>"