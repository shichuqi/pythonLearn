# LOG
- logging
- logging模块提供模块级别的函数记录日志
- 四大模块

## 1. 日志相关概念
- 日志
- 日志的级别（level）
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作->不要太频繁
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2. Logging模块
- 日志级别
    - 级别可自定义
- 初始化日志实例需要指定级别,只有当级别等于或高于指定级别才被记录
- 使用方法
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接制定
    
## 2.1 logging模块级别的日志
- 使用一下函数
    - 具体看教学项目        

- logging.basicConfig(**kwargs)
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr
        - 级别：WARNING
        - 格式：level:log_name:content
- format参数
    - 具体见教学项目 
    
## 2.2 logging模块的处理流程
- 四大组件
    - 日志器（logger）：产生日志的接口
    - 处理器（handler）：把产生的日志发送到相应的目的地
    - 过滤器（filter）：更精细地控制日志输出
    - 格式器（formatter）：对输出信息进行格式化 
- Logger
    - 产生一个日志
    - 操作
            
            Logger.setLevel()
            Logger.addHandler()
            Logger.addFilter              
            ......
            详情见教学项目

    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()

- Handler  
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter
    - 不需要直接使用，Handler是基类                  
    
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt
        - datefmt
        - style    

- Filter类
    - 可以被handler和Logger使用
    - 控制传递过来的信息具体内容
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    