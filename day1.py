def read_data(txt_file_path: str) -> int:
    with open(txt_file_path) as f:
        lines = f.readlines()

    return lines

def max_calories(data_list: list) -> int:

    accum_aux, max_calories = 0, 0
    for i in data_list:
        i_cleaned = i.replace('\n', '')
        if i_cleaned:
            accum_aux += int(i)
        else:
            if max_calories < accum_aux:
                max_calories = accum_aux
            accum_aux = 0

    return max_calories

def max_3_calories(data_list: list) -> int:

    accum_aux = 0
    top_3 = {1: 0,
             2: 0,
             3: 0}
    for pos, i in enumerate(data_list):
        i_cleaned = i.replace('\n', '')
        if i_cleaned:
            accum_aux += int(i)
        if not i_cleaned or pos+1 == len(data_list):
            _top1 = top_3[1]
            _top2 = top_3[2]
            _top3 = top_3[3]
            if _top1 < accum_aux:
                top_3[1] = accum_aux
                top_3[2] = _top1
                top_3[3] = _top2

            elif _top2 < accum_aux:
                top_3[2] = accum_aux
                top_3[3] = _top2

            elif _top3 < accum_aux:
                top_3[3] = accum_aux
            accum_aux = 0

    return sum(top_3.values())



if __name__ == '__main__':
    data_list = read_data('day1.txt')

    _data_list =['1000',
'2000',
'3000',
'',
'4000',
'',
'5000',
'6000',
'',
'7000',
'8000',
'9000',
'',
'10000']  # 24000  # 45000

    max_cal = max_3_calories(data_list)
    print(max_cal)