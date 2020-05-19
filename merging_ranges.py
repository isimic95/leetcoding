def merge_ranges1(l):
    l.sort()
    merged_meetings = [l[0]]

    for start_time, end_time in l[1:]:
        last_start, last_end = merged_meetings[-1]

        if start_time <= last_end:
            merged_meetings[-1] = (last_start, max(last_end, end_time))
        else:
            merged_meetings.append((start_time, end_time))

    return merged_meetings

# copy pasted solution


def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append(
                (current_meeting_start, current_meeting_end))

    return merged_meetings


print(merge_ranges1([(0, 1), (0, 3), (3, 9), (12, 13),
                    (15, 18), (3, 5), (4, 8), (10, 12), (9, 10)]))

""" 
while i < len(l):
        f,s = l[i], l[i+1]
        if f[1] in range(s[0], s[1]+1) or f[0] in range(s[0], s[1]+1):
            n = (f[0], s[1])
            merged_meetings.append(n)
        else:
            for x in merged_meetings:
                if f[0] in range(x[0],x[1])
            merged_meetings.append(f)
    return merged_meetings """
