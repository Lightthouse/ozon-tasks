# Готовые задачи в попке done

input_table = [
    ['R.R.R.G', '.Y.G.G.', 'B.Y.V.V', ],
    ['Y.R.B.B.', '.R.R.B.V', 'B.R.B.R.', '.B.B.R.R'],
    ['G.B.R.G', '.G.G.G.', ],
]

correct_answer = ['YES', 'NO', 'YES']


def validate_map(table: [[str]]):
    n = len(table)  # input
    m = len(table[0])  # input

    def sort_zones_map(table: [[str]]):
        zones_dick = dict()
        for row_num in range(n):

            for col_num in range(m):
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
                    # print(last_related_zone, current_coords)
                    zones_dick[current_zone]['unrelated'].append(current_coords)

        return zones_dick

    def rematch_unrelated_zones(zones: dict):
        # Можно сразу возращать YES, NO
        # Можно сразу принимать list, а не dict
        for _, zone in zones.items():
            related_zones = zone['related']
            unrelated_zones = zone['unrelated']

            # мб часть проверок сделали раньше
            for unr_z in unrelated_zones:
                if [unr_z[0] + 0, unr_z[1] + 2] in related_zones or \
                        [unr_z[0] + 0, unr_z[1] - 2] in related_zones or \
                        [unr_z[0] + 1, unr_z[1] - 1] in related_zones or \
                        [unr_z[0] + 1, unr_z[1] + 1] in related_zones or \
                        [unr_z[0] - 1, unr_z[1] - 1] in related_zones or \
                        [unr_z[0] - 1, unr_z[1] + 1] in related_zones:
                    related_zones.append(unr_z)
                    continue

                # print('gg ', zone_name, '<>', related_zones, '<>', unrelated_zones, '<>', unr_z)
                return False
        return True

    sorted_zones = sort_zones_map(table)
    unrelated_zones = {k: v for k, v in sorted_zones.items() if v['unrelated']}
    all_zones_matched = rematch_unrelated_zones(unrelated_zones)

    return 'YES' if all_zones_matched else 'NO'


def whole_validation(table: list):
    res = []
    for i_map in table:
        res.append(validate_map(i_map))
    return res


print(whole_validation(input_table))
print(correct_answer)
