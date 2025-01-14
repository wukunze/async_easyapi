from setuptools import setup, find_packages

setup(
    name='easyapi',
    version='1.0',
    description='一个方便拓展快速构建异步curd的后端api工具 基于 quart',
    packages=find_packages(exclude=[]),
    author='suchang zhengzhandong and wukunze',
    long_description=__doc__,
    long_description_content_type="text/markdown",
    zip_safe=False,
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[]
)
