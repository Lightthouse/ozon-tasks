mock_tables = [
    ['R.R.R.G', '.Y.G.G.', 'B.Y.V.V', ],
    ['Y.R.B.B.', '.R.R.B.V', 'B.R.B.R.', '.B.B.R.R'],
    ['G.B.R.G', '.G.G.G.', ],
]

correct_answer = ['YES', 'NO', 'YES']


# input
# 3
# 3 7
# R.R.R.G
# .Y.G.G.
# B.Y.V.V
# 4 8
# Y.R.B.B.
# .R.R.B.V
# B.R.B.R.
# .B.B.R.R
# 2 7
# G.B.R.G
# .G.G.G.

# output
# YES
# NO
# YES


def validate_map(geks_map: [[str]], columns: int, rows: int):

    def sort_zones_map(table: [[str]], clm_count, rws_count):
        zones_dick = dict()
        for row_num in range(rws_count):

            for col_num in range(clm_count):
                current_zone = table[row_num][col_num]
                if current_zone == '.':
                    continue

                current_coords = [row_num, col_num]
                if not zones_dick.get(current_zone):
                    zones_dick[current_zone] = {'related': [current_coords], 'unrelated': []}
                    continue

                last_related_zone = zones_dick[current_zone]['related'][:-2:-1][0]

                # проверяем, связанность гекса с предыдущими в цепи
                if [last_related_zone[0] + 0, last_related_zone[1] + 2] == current_coords or \
                        [last_related_zone[0] + 1, last_related_zone[1] + 1] == current_coords or \
                        [last_related_zone[0] + 1, last_related_zone[1] - 1] == current_coords:

                    zones_dick[current_zone]['related'].append(current_coords)
                else:
                    zones_dick[current_zone]['unrelated'].append(current_coords)

        return zones_dick

    def rematch_unrelated_zones(zones: dict):
        # Можно сразу возращать YES, NO
        # Можно сразу принимать list, а не dict
        for _, zone in zones.items():
            related_geks = zone['related']
            unrelated_geks = zone['unrelated']

            # мб часть проверок сделали раньше
            for unr_gek in unrelated_geks:
                if [unr_gek[0] + 0, unr_gek[1] + 2] in related_geks or \
                        [unr_gek[0] + 0, unr_gek[1] - 2] in related_geks or \
                        [unr_gek[0] + 1, unr_gek[1] - 1] in related_geks or \
                        [unr_gek[0] + 1, unr_gek[1] + 1] in related_geks or \
                        [unr_gek[0] - 1, unr_gek[1] - 1] in related_geks or \
                        [unr_gek[0] - 1, unr_gek[1] + 1] in related_geks:
                    related_geks.append(unr_gek)
                    continue

                # print('gg ', zone_name, '<>', related_zones, '<>', unrelated_zones, '<>', unr_z)
                return False
        return True

    sorted_zones = sort_zones_map(geks_map, columns, rows)
    unrelated_zones = {k: v for k, v in sorted_zones.items() if v['unrelated']}
    all_zones_matched = rematch_unrelated_zones(unrelated_zones)

    return 'YES' if all_zones_matched else 'NO'


def get_input_nums_array():
    return [int(inp) for inp in input().split()]


iters_num = int(input())  # 3
res = []
for i in range(iters_num):
    n_rows, m_cols = get_input_nums_array()

    current_map = []
    for n_row in range(n_rows):
        current_map.append(input())

    res.append(validate_map(current_map, m_cols, n_rows))

for r in res:
    print(r)

#local test variant
# def whole_validation(table: list):
#     res = []
#     for i_map in table:
#         res.append(validate_map(i_map, len(i_map), len(i_map[0])))
#     return res
#
#
# print(whole_validation(mock_tables))
# print(correct_answer)
