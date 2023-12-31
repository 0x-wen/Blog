# 理解常见分布式系统模型的划分

## 网络链路模型分类

1. 可靠链路
   - 可靠传递: 两个节点或进程都正常工作,则a <-> b发送的消息都会被链路传递
   - 没有重复: 每条消息最多传递一次
   - 不会无中生有: 链路不会自己生成消息。它不会传递一个从未发送过的消息
2. 公平损失链路
   - 公平损失: 如果发送方和接收方都正常工作,且发送方不断重复发送消息,则消息最终会被送达
   - 有限重复: 消息只会重复发送有限次数
   - 不会无中生有
3. 任意链路
   - 允许任意的网络链路执行任何操作,可能有恶意软件修改网络数据包和流量

## 节点故障类型分类

1. 崩溃-停止
    - 节点停止工作,不会恢复,有些情况下也许可以通过重启机器来恢复,但这种模型主要意味着算法不能依赖与节点恢复
2. 崩溃-恢复
    - 允许节点重新启动并继续执行剩余的步骤,一般通过持久化存储必要的状态信息来容忍这种故障类型
3. 拜占庭故障
    - 故障节点可能不只会宕机,还可能以任意方式偏离算法,甚至恶意破坏系统

## 按时间划分系统模型

1. 同步系统
    - 系统中的所有节点都有相同的时钟,且消息传递的延迟有上限,一个消息的响应时间在一个有限且已知的时间范围内
2. 异步系统
    - 一个消息的响应时间是无限的,无法知道一条消息什么时候会到达
3. 部分同步系统
    - 设计一个完全异步的系统难以找到一个满足要求的共识算法,根据FLP(FLP impossibility)不可能定理,引出部分同步系统
    - 假设系统在大部分时间都是同步的,但偶尔会因为故障转变为异步系统,需要将异步系统转换为部分同步系统

## 消息传递的语义

1. 最多一次
2. 至少一次
3. 精确一次

关心消息被处理的次数,而不是消息发送的次数,通过消息重复发送,但是处理时只处理一次忽略后续重复的消息来达到3的效果

## 幂等性

- 同样的消息被多次处理,得到的结果是一致的
