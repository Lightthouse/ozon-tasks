from typing import List, Dict


def sort_zones_map(table: List[str], columns_len: int, rows_len: int) -> Dict:
    zones_dick: Dict[str, Dict] = dict()

    for row_num in range(rows_len):

        for col_num in range(columns_len):
            current_zone = table[row_num][col_num]
            if current_zone == '.':
                continue

            current_coords = [row_num, col_num]
            if not zones_dick.get(current_zone):
                zones_dick[current_zone] = {'related': [current_coords], 'unrelated': []}
                continue

            related_zones = zones_dick[current_zone]['related']

            # проверяем, связанность гекса с предыдущими в цепи
            if [current_coords[0] + 0, current_coords[1] - 2] in related_zones or \
                    [current_coords[0] - 1, current_coords[1] + 1] in related_zones or \
                    [current_coords[0] - 1, current_coords[1] - 1] in related_zones:

                zones_dick[current_zone]['related'].append(current_coords)
            else:
                zones_dick[current_zone]['unrelated'].append(current_coords)

    return zones_dick


def rematch_unrelated_zones(zones: Dict) -> bool:
    def rematch(related_geks: List[List[int]], unrelated_geks: List[List[int]]) -> bool:

        for gek_index, unr_gek in enumerate(unrelated_geks):

            if [unr_gek[0] + 0, unr_gek[1] + 2] in related_geks or \
                    [unr_gek[0] + 0, unr_gek[1] - 2] in related_geks or \
                    [unr_gek[0] + 1, unr_gek[1] - 1] in related_geks or \
                    [unr_gek[0] + 1, unr_gek[1] + 1] in related_geks or \
                    [unr_gek[0] - 1, unr_gek[1] - 1] in related_geks or \
                    [unr_gek[0] - 1, unr_gek[1] + 1] in related_geks:
                related_geks.append(unr_gek)
                del unrelated_geks[gek_index]

                return rematch(related_geks, unrelated_geks)

        return len(unrelated_geks) == 0

    for _, zone in zones.items():

        rematched_success = rematch(zone['related'], zone['unrelated'])
        if not rematched_success:
            return False

    return True


def validate_map(geks_map: List[str], columns_len: int, rows_len: int) -> str:
    sorted_zones = sort_zones_map(geks_map, columns_len, rows_len)
    unrelated_zones = {k: v for k, v in sorted_zones.items() if v['unrelated']}
    all_zones_matched = rematch_unrelated_zones(unrelated_zones)

    return 'YES' if all_zones_matched else 'NO'


def get_input_nums_array() -> List[int]:
    return [int(inp) for inp in input().split()]


def start_task() -> None:
    iters_num = int(input())  # 3
    res = []
    for _ in range(iters_num):
        n_rows, m_cols = get_input_nums_array()

        current_map = []
        for _n_row in range(n_rows):
            current_map.append(input())

        res.append(validate_map(current_map, m_cols, n_rows))

    for r in res:
        print(r)


if __name__ == 'h':
    start_task()
