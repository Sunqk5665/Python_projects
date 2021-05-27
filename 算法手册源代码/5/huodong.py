class task():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return "['%s',%d,%d]" % (self.name, self.start, self.end)

    def __repr__(self):
        return self.__str__()


def QuickSort(mylist, start, end):
    if start < end:
        i, j = start, end
        base = mylist[i]
        while i < j:
            while (i < j) and (mylist[j].end >= base.end):
                j -= 1
            mylist[i] = mylist[j]
            while (i < j) and (mylist[i].end <= base.end):
                i += 1
            mylist[j] = mylist[i]
        mylist[i] = base
        QuickSort(mylist, start, i - 1)
        QuickSort(mylist, j + 1, end)
    return mylist


def get_max(joblist):
    job_schedule = []
    num_jobs = len(joblist)
    for n in range(num_jobs):
        if not job_schedule:
            job_schedule.append(joblist[n])
        else:
            if job_schedule[-1].end <= joblist[n].start:
                job_schedule.append(joblist[n])
    return job_schedule


if __name__ == "__main__":
    joblist = [task('1', 3, 5), task('2', 1, 4), task('3', 0, 6), task('4', 3, 8), task('5', 5, 7), task('6', 6, 10),
               task('7', 5, 9), task('8', 8, 11), task('9', 2, 13), task('10', 8, 12)]
    list_final = QuickSort(joblist, 0, len(joblist) - 1)
    print(get_max(list_final))
