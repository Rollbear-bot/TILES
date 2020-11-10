# 通过TILES的执行日志分析算法运行的时间开销
# Rollbear - 2020.11.10

import re
import csv


def parse_exc_log(log_path, csv_dump_path):
    # regular expression
    # pattern_init_time = "Started! () "
    pattern_general = "Started Slice () .*Starting .* ending .* - ().*Edge Added: (\d+)	Edge removed: \d+"
    compiled_general = re.compile(pattern_general)
    # compiled_init_time = re.compile(pattern_init_time)

    with open(log_path, "r") as rf:
        log_string = rf.read()
        # alg_init_time = compiled_init_time.findall(log_string)
        clusters = compiled_general.findall(log_string)

    # 计算每个观察点开始到下一个观察点开始的时间差，即为时间片的执行耗时
    # todo::从日期的字符串表示转化为时间戳
    gap = [clusters[index+1] - clusters[index] for index, _ in enumerate(clusters[:-1])]

    # dump to csv table
    with open(csv_dump_path, "w", newline="") as wf:
        writer = csv.writer(wf)
        csv_header = ["slice_id", "#added_edges", "exc_time"]
        writer.writerow(csv_header)
        writer.writerows(clusters)


def local_test():
    pass


def online_procedure():
    datasets = []
    for dataset in datasets:
        working_dir = f"{dataset}/"
        log = working_dir + "extraction_status.txt"
        csv_dump = working_dir + f"{dataset}_exc_time.csv"
        parse_exc_log(log_path=log, csv_dump_path=csv_dump)


if __name__ == '__main__':
    local_test()
