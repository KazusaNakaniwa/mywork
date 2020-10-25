import datetime
import time

def get_h_m_s(t):
    m, s = divmod(t.seconds, 60)
    h, m = divmod(m, 60)
    ms = t.microseconds
    while ms >= 1:
        ms /= 10.0
    s += ms
    return h, m, s

print("---- My Counter ----")

cnt = 0

while True:
    if cnt == 0:
        limit = int(input("Count Limit:"))
        if limit < 0:
            break
        start = datetime.datetime.now()
        pb = 10 ** 7
     
    print("\033[36m{0:%Y-%m-%d %H:%M:%S }\033[0m".format(datetime.datetime.now()), end='')
    print(cnt, end=' ')

    if cnt >= 1:
        gap = t2 - t1
        hour, minute, seconds = get_h_m_s(gap)
        #print(seconds, mseconds)
        
        print("\033[33m{:02}h{:02}m{:02.2f}s \033[0m".format(hour, minute, seconds), end='')
        print("gap: ", end = '')

        if cnt >= 2:
            if pb.seconds > gap.seconds:
                hour, minute, seconds = get_h_m_s(pb-gap)
                pb = gap
                print("\033[32m-{:02}h{:02}m{:02.2f}s (PB)\033[0m".format(hour, minute, seconds), end='')
            else:
                hour, minute, seconds = get_h_m_s(gap-pb)
                print("\033[31m +{:02}h{:02}m{:02.2f}s \033[0m".format(hour, minute, seconds), end='')
        else:
            pb = gap
            print("{:02}h{:02}m{:02.2f}s (PB)".format(hour, minute, seconds), end='')

    t1 = datetime.datetime.now()

    if cnt == limit:
        end = datetime.datetime.now()
        hour, minute, seconds = get_h_m_s(end-start)
        print()
        print("Finish!")
        print("Total Time: {:02}h{:02}m{:02.2f}s".format(hour, minute, seconds))
        print("--------------------")
        cnt = 0
    else:
        cnt += 1

        s = input()
        t2 = datetime.datetime.now()
        if s == "0":
            cnt = 0
            print("--------------------")
        elif s == "-1":
            break
