from cooling_data import TEMPERATURE_SPIKE
from cooling_detectors import calculate_rise_per_minute, detect_by_window_rate

rate_limit = 20


for index in range(len(TEMPERATURE_SPIKE) - 1):
    current_row = TEMPERATURE_SPIKE[index]
    next_row = TEMPERATURE_SPIKE[index + 1]

    rise_per_minute = calculate_rise_per_minute(current_row, next_row)
    rising_too_fast = rise_per_minute >= rate_limit

    print(index, rise_per_minute, rising_too_fast)


print("逐段速度規則：", detect_by_window_rate(TEMPERATURE_SPIKE))
