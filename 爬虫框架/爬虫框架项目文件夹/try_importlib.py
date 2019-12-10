

import importlib


# path  = "test"
# ret = importlib.import_module(path)
# print(ret)
#
# cls = getattr(ret,"Test") # 得到模块中的类对象
# print(cls)
#
# func = getattr(cls(),"test") # 得到类中方法的对象
# print(func)
#
# func()


PIPELINES = [
    "pipelines.BaiduPipeline",
    "pipelines.DoubanPipeline",
]

for pipeline in PIPELINES:
    module_name = pipeline.split(".")[0]  # module的名字，路径
    cls_name = pipeline.split(".")[-1]  # 类名
    module = importlib.import_module(module_name) # 导入module
    cls = getattr(module,cls_name) # 获取module下的类
