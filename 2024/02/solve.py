def read_input() -> list[int]:
    l = []
    with open('input', 'r') as f:
        for line in f:
            values = line.strip().split(' ')
            t = []
            for value in values:
                t.append(int(value))
            l.append(t)
    return l

def check_report_increasing(report: list[int]) -> bool:
    for idx, element in enumerate(report):
        if idx == 0:
            continue
        if element <= report[idx - 1]:
            return False
        if element - 4 >= report[idx - 1]:
            return False
    return True

def check_report_decreasing(report: list[int]) -> bool:
    for idx, element in enumerate(report):
        if idx == 0:
            continue
        if element >= report[idx - 1]:
            return False
        if element + 4 <= report[idx - 1]:
            return False
    return True


def report_is_safe(report: list[int]) -> bool:
    if report[0] > report[1]:
        return check_report_decreasing(report)
    elif report[0] < report[1]:
        return check_report_increasing(report)
    return False

def check_report_increasing_tolerate_one(report: list[int]) -> bool:
    failures = [0] * len(report)
    for i in range (len(report)):
        new_report = report.copy()
        new_report.pop(i)
        for idx, element in enumerate(new_report):
            if idx == 0:
                continue
            if element <= new_report[idx - 1]:
                failures[i] += 1
                break
            if element - 4 >= new_report[idx - 1]:
                failures[i] += 1
                break
    if 0 in failures:
        return True
    return False

def check_report_decreasing_tolerate_one(report: list[int]) -> bool:
    failures = [0] * len(report)
    for i in range (len(report)):
        new_report = report.copy()
        new_report.pop(i)
        for idx, element in enumerate(new_report):
            if idx == 0:
                continue
            if element >= new_report[idx - 1]:
                failures[i] += 1
                break
            if element + 4 <= new_report[idx - 1]:
                failures[i] += 1
                break
    if 0 in failures:
        return True
    return False




def report_is_safe_tolerate_one(report: list[int]) -> bool:
    results = [0,0,0,0]
    if check_report_decreasing(report):
        return True
    elif check_report_increasing(report):
        return True
    elif check_report_increasing_tolerate_one(report):
        return True
    elif check_report_decreasing_tolerate_one(report):
        return True
    return False

def part_one(l: list[list]) -> int:
    safe_reports = 0
    for report in l:
        if report_is_safe(report):
            safe_reports += 1
    return safe_reports

def part_two(l: list[list]) -> int:
    safe_reports = 0
    for report in l:
        if report_is_safe_tolerate_one(report):
            safe_reports += 1
    return safe_reports
if __name__ == '__main__':
    l = read_input()
    # print(part_one(l))
    print(part_two(l))