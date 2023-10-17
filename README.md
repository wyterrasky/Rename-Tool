# Rename-tools
### 目录
- [特点](#特点)
- [简单上手](#简单上手)
- [用法说明](#用法说明)
- [命名公式](#命名公式)
-  [期待完善](#期待完善)
-  [后续](#多说几句)
## 特点

- **免费**：本项目所有代码开源，完全免费。

- **批量**: 可对文件进行批量命名。

- **方便**: 支持命令行操作

## 简单上手

### 解压

文件下载解压，运行~ RenameTool.pyw

### 界面
![image](https://github.com/wyterrasky/Rename-Tool/assets/147787793/ce543590-fe5d-45f5-9db2-c4c8ba519bef)


1.  命名规则公式编辑区;

2.  公式快捷输入区;

3.  文件收集区;

4.  生产按钮

## 用法说明
step1  :  导入文件名。可批量导入选定文件，导入的文件名列表位于工作区。
> 支持使用totalcommad带参数运行
> ![image](https://github.com/wyterrasky/Rename-Tool/assets/147787793/ffb994cb-74ae-4d6d-a64c-38cc75382024)




step2  :  编辑公式。可手动输入公式，也可结合公式快捷输入区输入。公式输入规则参[命名公式](#命名公式)

step3  :  生成。点击生成按钮，文件名批量修改状态与列表框内。

## 命名公式
- 【N】 原文件名称
-  【L】文件名列表
 利用输入列表框中字符串，将原文件名称列表批量改名。在输入列表框内，每行对应一个文件名，文件名称之间按顺序排列，若输入列表框的文字段数小于文件个数，则忽略后续文件名；若输入列表框的文字段数大于文件个数，则后面多出的文件名将忽略。
- 【C】 定义计数器
根据起步、步数、位数，给被命名文件添加计数器

## 期待完善
 - 支持文件拖入操作
 - 优化界面布局
 - 优化拓展公式类型
> 如补充日期、时间等
 - 待编辑修改的文件可调整顺序

## 多说几句
项目来源于在工作中，个人需要将打印的好的批量图纸文件，上传到系统平台中去，但平台上对文件命名的根式有着严格要求，经常处理这些文件命名工作，费时费力，变萌生了写个小程序来处理相关问题的想法。
