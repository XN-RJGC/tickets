## 一、实验简介
Python编写的命令行版火车票查看器
#### 1.1 知识点
* Python2.7基础知识的综合运用
* docopt、request及prettytable等库的使用
* Python正则表达式

## 二、总体设计
#### 2.1 接口设计
> 脚本名称: tickets
> 使用方法: tickets [-gdtkz] < from> < to> < date>
> 参数:
> -h, --help 帮助
> -v, --version 版本
> -g 高铁
> -d 动车
> -t 特快
> -k 快速
> -z 直达

#### 2.2 详细设计
* 解析命令行参数，利用docopt库
* 获取数据，[余票查询地址](https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-07-01&from_station=SHH&to_station=BJP)，例如上海到北京日期为2016-07-01的地址 https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-07-01&from_station=SHH&to_station=BJP
* 所有车站信息地址：https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955
* 颜色控制（color.py）与格式输出