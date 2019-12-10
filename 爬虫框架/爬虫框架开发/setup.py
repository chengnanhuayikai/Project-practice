from os.path import dirname,join



from setuptools import (
    find_packages,
    setup
)


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]
#
# with open(join(dirname(__file__),"VERSION.txt"),"rb") as f:
#     version = f.read().decode("ascii").strip()



# with open(join(dirname(__file__),"VERSION.txt"),"rb") as f:
version = 1.0
setup(
    name = "scrapy-plus",# 模块名称
    version = version,  # 版本号
    description = "A mini spider frmework,like Scrapy", # 描述
    packages = find_packages(exclude=[]),
    author = "xixi",
    author_email = "xixi@email.com",
    license = "Apache License v2",
    package_data = {"":["*.*"]},
    url = "#",
    # install_requires = parse_requirements("requirements.txt"), # 所需环境
    install_requires = "requests>=2.18.4\n\tlxml>=4.2.1", # 所需环境
    zip_safe = False,
    classifiers= [
        "PRoramming Language :: Python",
        "Operating System :: MICrosoft :: Windows",
        "Operating System :: Unix",
        "PRoramming Language :: Python :: 2.7",
        "PRoramming Language :: Python :: 3.4",
        "PRoramming Language :: Python :: 3.5",
        "PRoramming Language :: Python :: 3.6",
    ]
)
# print(join(dirname(__file__),"VERSION.txt"))
# 安装 python setup.py install