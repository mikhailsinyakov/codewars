def pick_peaks(arr):
    reduced_arr = [[pos, num]
                   for pos, num in enumerate(arr) if pos == 0 or num != arr[pos-1]]
    peaks_data = [reduced_arr[i] for i in range(1, len(
        reduced_arr)-1) if reduced_arr[i+1][1] < reduced_arr[i][1] > reduced_arr[i-1][1]]

    peaks_data_t = [list(item) for item in zip(*peaks_data)]

    return {
        "pos": peaks_data_t[0] if peaks_data_t else [],
        "peaks": peaks_data_t[1] if peaks_data_t else []
    }
