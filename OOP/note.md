# 面向对象的概述（Object Oriented，OO）
- 几个名词
    - OO：面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：面向对象的实现
    - OOP：面向对象的编程
    - OOA-->OOD-->OOI：面向对象的实现过程
    
    
# 类的基本实现
- 类的命名
    - 大驼峰
    - 尽量避开与系统命名相似的命名
- 声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，允许使用None
    - 案例 01.py
- 实例化类
        
        变量 = 类名() # 实例化了一个对象
- 访问对象成员
    - 使用点操作符
    
        ojb.成员属性名称
        obj.成员方法
- 检查类和对象的所有成员
    - 对象所有成员检查
        # dict前后各有两个下划线
        obj.__dict__        
    - 类的所有的成员
        # dict前后各有两个下划线
        class_name.__dict__           
     
    
    
# anaconda 基本使用
- anaconda 主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list ：显示anaconda安装的包
- conda env list : 显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6  ：创建python版本为3.6的虚拟环境，名称为xxx