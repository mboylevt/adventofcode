import re
import datetime
import operator

timestamp_re = r'\[(.*)\]'
shift_re = r'Guard #(\d+)'
fall_asleep_re = r'falls'
wake_up_re = r'wakes'

TYPE_NEW_SHIFT = 1
TYPE_FALL_ASLEEP = 2
TYPE_WAKE_UP = 3


class Entry():
    def __init__(self, line, guard_id=None):
        timestamp_search = re.search(timestamp_re, line)

        self.line = line
        self.timestamp = datetime.datetime.strptime(timestamp_search.group(1), '%Y-%m-%d %H:%M')
        self.type = None
        self.guard_id = None
        shift_search = re.search(shift_re, line)
        fall_asleep_search = re.search(fall_asleep_re, line)
        wake_up_search = re.search(wake_up_re, line)

        if shift_search:
            self.guard_id = int(shift_search.group(1))
            self.type = TYPE_NEW_SHIFT
        elif fall_asleep_search:
            self.guard_id=guard_id
            self.type = TYPE_FALL_ASLEEP
        elif wake_up_search:
            self.guard_id = guard_id
            self.type = TYPE_WAKE_UP
        else:
            raise(TypeError, "Failed to parse {}".format(line))

    def __repr__(self):
        return "Guard: {}, Action: {}".format(self.guard_id, self.type)


class Guard():
    def __init__(self, id):
        self.guard_id = id
        self.minutes = [0 for x in range(60)]
        self.sleepy_time = 0

    def __repr__(self):
        return "Guard {}, Sleep Count {}".format(self.guard_id, self.sleepy_time)

    def update_minutes(self, fell_asleep, woke_up):
        # if (fell_asleep > woke_up):
        #     self.sleepy_time += (60-fell_asleep + woke_up)
        #     for x in range(59, fell_asleep):
        #         self.minutes[x] += 1
        #     for x in range(0, woke_up):
        #         self.minutes[x] += 1
        # else:
            self.sleepy_time += (woke_up - fell_asleep)
            for x in range(fell_asleep, woke_up):
                self.minutes[x] += 1

entries = []
guards = {}
prev_id = None
with open('../data/p4_sorted.data', 'r') as f:
# with open('../data/p4_example.data', 'r') as f:
    for line in f.readlines():
        entry = Entry(line, prev_id)
        if entry.type == TYPE_NEW_SHIFT:
            guards[entry.guard_id] = Guard(entry.guard_id)
        entries.append(entry)
        prev_id = entry.guard_id

current_guard = None
fell_asleep_minute = None
for entry in entries:
    current_guard = entry.guard_id
    if entry.type == TYPE_NEW_SHIFT:
        continue
    elif entry.type == TYPE_FALL_ASLEEP:
        fell_asleep_minute = entry.timestamp.minute
    else:
        woke_up_minute = entry.timestamp.minute
        guards[current_guard].update_minutes(fell_asleep_minute, woke_up_minute)

max_time = 0
guard_max = 0
for guard in guards.values():
    if guard.sleepy_time > max_time:
        max_time = guard.sleepy_time
        guard_max = guard

print("Max: {}".format(guard_max))
max_min = 0
min_index = None
for x in range(0,60):
    if guard_max.minutes[x] > max_min:
        max_min = guard_max.minutes[x]
        min_index = x

print("Value: {}".format(guard_max.guard_id * min_index))


i = 1
### Used to make sorted entries
# f = open('../data/p4.data', 'r')
# data = f.readlines()
# f.close()
#
# entries = []
# for line in data:
#     entries.append(Entry(line))
#
# entries.sort(key=operator.attrgetter('timestamp'))
# with open('../data/p4_sorted.data', 'w') as f:
#     for entry in entries:
#         f.write(entry.line)


