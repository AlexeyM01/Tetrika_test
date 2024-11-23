def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']  # Время урока
    pupil_intervals = intervals['pupil']  # Интервалы ученика
    tutor_intervals = intervals['tutor']  # Интервалы учителя

    # Функция для объединения перекрывающихся интервалов
    def merge_intervals(intervals, lesson):
        lesson_start, lesson_end = lesson
        if not intervals:
            return []

        merged = []
        current_start, current_end = max(intervals[0], lesson_start), min(intervals[1], lesson_end)
        for i in range(2, len(intervals), 2):
            start, end = max(intervals[i], lesson_start), min(intervals[i + 1], lesson_end)  # Есть пересечение с
            # началом урока
            if intervals[i] < current_end:  # Есть пересечение
                current_end = max(current_end, end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = start, end

        merged.append((current_start, current_end))  # Добавляем последний интервал
        return merged

    # Объединяем интервалы для ученика и учителя
    pupil_merged = merge_intervals(pupil_intervals, (lesson_start, lesson_end))
    tutor_merged = merge_intervals(tutor_intervals, (lesson_start, lesson_end))
    # Функция для вычисления времени пересечения
    def calculate_overlap(pupil_segments, tutor_segments):
        total_overlap_time = 0
        p = 0
        t = 0
        while p < len(pupil_segments) and t < len(tutor_segments):
            p_start, p_end = pupil_segments[p]
            t_start, t_end = tutor_segments[t]
            overlap_start = max(p_start, t_start)
            overlap_end = min(p_end, t_end)
            if overlap_start <= overlap_end:  # Если есть пересечение
                total_overlap_time += overlap_end - overlap_start
            if t_end < p_end:
                t += 1
            else:
                p += 1
        return total_overlap_time

    # Находим общее время присутствия
    total_time = calculate_overlap(pupil_merged, tutor_merged)

    return total_time


# Тесты
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389,
                             1594663390, 1594663395,
                             1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430,
                             1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500,
                             1594702807, 1594704542,
                             1594704512, 1594704513,
                             1594704564, 1594705150,
                             1594704581, 1594704582,
                             1594704734, 1594705009,
                             1594705095, 1594705096,
                             1594705106, 1594706480,
                             1594705158, 1594705773,
                             1594705849, 1594706480,
                             1594706500, 1594706875,
                             1594706502, 1594706503,
                             1594706524, 1594706524,
                             1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364,
                             1594702749, 1594705148,
                             1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066,
                             1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print('Все тесты выполнены')
