# Parking lot license plate recognition
停车场车牌识别+数据分析统计
# 开发环境要求
本系统的软件开发及运行环境具体如下。
操作系统：Windows 7、Windows 10。
Python版本：Python 3.7。
开发工具：PyCharm 2018。
Python内置模块：os、time、datetime。
第三方模块：opencv-python、pandas、matplotlib、pygame、baidu-aip、xlrd。
注意：在使用第三方模块时，首先需要使用pip install命令安装该模块，例如，安装pygame模块，可以在Python命令窗口中执行以下命令： 
## pip install pygame
# 运行方法
说明：在运行程序前，先将当前的计算机连接互联网，并且需要先申请百度AI开放平台的图片识别需要的Key，并且复制该Key到项目根目录下的file子目录的key.txt文件中替换相应的内容即可。替换时需要注意不要把原来的单引号删除。
1.打开PyCharm开发环境，然后在主菜单上选择File→Open菜单项，在打开的Open File or Project对话框中，选择项目CarNumber
2.单击OK按钮，将弹出 Open Project对话框，在该对话框，如果想要在新的窗体中打开项目，则选中Open in new window单选按钮，否则在当前窗体中打开，则选中Open in current window单选按钮。这里在新窗体中打开文件
3.打开项目后，在右侧的Project面板中选中程序的主文件main.py，并且单击鼠标右键，在弹出的快捷菜单中选择“Run 'main'”菜单项运行项目
