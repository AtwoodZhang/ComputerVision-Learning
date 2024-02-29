# %% [markdown]
# # 1. 自动更新
# #### 1） 正常定义并初始化类

# %%
class A():
    def __init__(self, dicts):
        self.name = dicts["name"]
        self.age = dicts["age"]
        self.sex = dicts["sex"]
        self.hobby = dicts["hobby"]
    
if __name__ == "__main__":
    dicts = {"name": "lisa", "age": 23, "sex": "women", "hobby":"hardstyle"}
    a = A(dicts)
    print(a)

# %% [markdown]
# #### 2）自动更新

# %%
class A():
    def __init__(self, dicts):
        self.__dict__.update(dicts)
        print(self.__dict__)
        
if __name__ == "__main__":
    dicts = {"name": "lisa", "age": 23, "sex": "women", "hobby":"hardstyle"}
    a = A(dicts)
    print(a)

# %% [markdown]
# 1) 出现了一个问题。关于自动更新。设置_defaults之后，__init__不走_defaults的问题。
# --> 具体现象如下： 如下是标准的自动更新设置过程；

# %%
class MyClass:
    # 定义默认值字典
    _defaults = {
        'key1': 'value1',
        'key2': 'value2',
    }

    def __init__(self, **kwargs):
        # 将默认值字典更新到实例的属性中
        self.__dict__.update(self._defaults)
        # 更新传入参数的值
        self.__dict__.update(kwargs)

# 创建 MyClass 实例并传入参数
my_instance = MyClass(key2='new_value2', key3='value3')

# 输出实例的属性
print(my_instance.key1)  # 输出: value1
print(my_instance.key2)  # 输出: new_value2
print(my_instance.key3)  # 输出: value3

# %% [markdown]
# 2) 但是我在使用python3.10.4的时候，情况发生了变化。_defaults里面的值传递不到__init__里面；但我换了python版本就可以了。

# %% [markdown]
# python 3.7.16 --> ok

# %% [markdown]
# python 3.8.0--> OK

# %% [markdown]
# python 3.10.4 --> NG

# %% [markdown]
# python 3.7.0-->NG

# %% [markdown]
# python 3.9.18 --> NG

# %% [markdown]
# 3. 但是又出现了很奇怪的现象，不管什么编译器，他运行了之后，再用不能运行的跑一次，又能跑了。

# %%



