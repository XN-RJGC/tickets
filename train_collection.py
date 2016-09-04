# coding: utf-8
from prettytable import PrettyTable
import color

class train_collection(object):

    header = 'train station time duration first second softsleep hardsleep hardsit'.split()

    def __init__(self, datas):
        self.datas = datas
        #print self.header

    def duration(self):
        # 历时
        print ''

    def get_information(self):
        for data in self.datas:
            trains = [
                # 车次
                data["station_train_code"],
                # 出发站/到达站
                '\n'.join([color.colored('red', data["start_station_name"]), color.colored('red', data["end_station_name"])]),
                # 出发时间/到达时间
                '\n'.join([color.colored('green', data["start_time"]), color.colored('green', data["arrive_time"])]),
                # 历时
                data["lishi"],
                # 一等坐
                data['zy_num'],
                # 二等坐
                data['ze_num'],
                # 软卧
                data['rw_num'],
                # 软坐
                data['yw_num'],
                # 硬坐
                data['yz_num']
            ]
            #print data["station_train_code"], data["start_station_name"]
            yield trains

    def pretty_print(self):
        """
        显示数据
        """
        pt = PrettyTable()
        # 设置每一列的标题
        pt._set_field_names(self.header)
        #print 'test'
        for train in self.get_information():
            pt.add_row(train)
        print pt

if __name__ == '__main__':
    train_collection('1')
