# 通过TILES的执行日志分析算法运行的时间开销
# Rollbear - 2020.11.10

import re
import csv
import datetime


def date2datetime(date_str):
    """Ubuntu date格式转化为datetime元组"""
    # date_str = "Tue Oct 20 03:43:48 2020"
    month_map = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sept": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    _, month, day, time, year = date_str.split(" ")
    hour, minute, sec = time.split(":")
    return datetime.datetime(int(year),
                             month_map[month],
                             int(day),
                             int(hour),
                             int(minute),
                             int(sec))


def get_sec_gap(datetime_a, datetime_b):
    """求两个Ubuntu date格式时间相差的秒数"""
    delta = date2datetime(datetime_a) - date2datetime(datetime_b)
    return delta.seconds


def parse_exc_log(log_path, csv_dump_path, debug=False):
    compiled_general = re.compile(
        "Saving Slice (\d+): Starting \d+-\d+-\d+ \d+:\d+:\d+ "
        "ending \d+-\d+-\d+ \d+:\d+:\d+ - \((.*)\)\nEdge Added: (\d+)")

    with open(log_path, "r") as rf:
        log_string = rf.read()
        # alg_init_time = compiled_init_time.findall(log_string)
        clusters = compiled_general.findall(log_string)

    # 计算每个观察点开始到下一个观察点开始的时间差，即为时间片的执行耗时
    sec_gap = [get_sec_gap(clusters[index + 1][1], clusters[index][1]) for index, _ in enumerate(clusters[:-1])]
    # 最后一行
    sec_gap.append(0)

    if debug:
        print(clusters)
        print(sec_gap)

    # dump to csv table
    with open(csv_dump_path, "w", newline="") as wf:
        writer = csv.writer(wf)
        csv_header = ["slice_id", "#added_edges", "exc_time"]
        writer.writerow(csv_header)
        rows = [(clusters[index][0], clusters[index][2], sec_gap[index]) for index in range(len(clusters))]
        writer.writerows(rows)


def local_test():
    log = "./output/article_tiles_output/extraction_status.txt"
    parse_exc_log(log, "./dump.csv", debug=True)


def online_procedure():
    datasets = [
        "phdthesis",
        "www",
        "book",
        # "incollection",
        # "article",
        # "inproceedings"
    ]
    out = "tiles_output_test3"

    for dataset in datasets:
        working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/" + out + "/"
        log = working_dir + "extraction_status.txt"
        csv_dump = working_dir + f"{dataset}_exc_time.csv"
        parse_exc_log(log_path=log, csv_dump_path=csv_dump)


if __name__ == '__main__':
    online_procedure()
