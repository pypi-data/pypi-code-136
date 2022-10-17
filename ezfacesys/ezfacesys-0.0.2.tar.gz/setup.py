from setuptools import setup, find_packages

setup(
    name="ezfacesys",
    version="0.0.2",
    author="HeShengLi",
    author_email="2794404684@qq.com",

    description="Face entry, training and recognition library",
    # 项目主页
    url="https://gitee.com/hhslyyds/face_identification.git",
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    # packages=find_packages(),
    install_requires=['certifi==2022.9.24',
                      'charset-normalizer==2.1.1',
                      'idna==3.4',
                      'numpy==1.21.6',
                      'opencv-contrib-python==4.6.0.66',
                      'opencv-python==4.6.0.66',
                      'PIL-Tools==1.1.0',
                      'Pillow==9.2.0',
                      'requests==2.28.1',
                      'urllib3==1.26.12']
)
