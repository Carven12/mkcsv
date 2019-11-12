# encoding=utf-8

import getopt
import sys
import time
import csv


def main(argv):
    file_name = ''
    project_id = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["fileName=", "projectId="])
    except getopt.GetoptError:
        print('mkcsv.py -n <fileName> -p <projectId>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('mkcsv.py -i <fileName> -p <projectId>')
            sys.exit()
        elif opt in ("-i", "--fileName"):
            file_name = arg
            print("file_name: ", file_name)
        elif opt in ("-p", "--projectId"):
            project_id = arg
            print("project_id: ", project_id)
    create_csv(file_name, project_id)
    # print("error args: {0}".format(args))


def create_csv(file_name, project_id):
    datetime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print("时间：", datetime)
    csv_file_name = file_name + '_' + datetime + '_000.csv'
    csv_head = datetime + ' | 90'
    csv_tail = datetime + ' | 20 | '
    # 1. 创建文件对象
    f = open(csv_file_name, 'w', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建CSV头
    csv_writer.writerow(csv_head)
    # 4. 构建CSV内容
    csv_body = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    loop_count = 10000
    count = 0
    while(count < loop_count):
        csv_writer.writerow(csv_body)
        count = count + 1
    # 4. 构建CSV尾内容
    csv_tail = csv_tail + loop_count
    csv_writer.writerow(csv_tail)
    f.close()


if __name__ == "__main__":
   main(sys.argv[1:])
