import time
def do_my_sum(l):
    sum=0
    for x in l:
        sum+=x
        return sum
    size=10000000
    data=range(size)
    t0=time.perf_counter()
    my_result=do_my_sum(data)
    t1=time.perf_counter()
    t2=time.perf_counter()
    builtin_result=sum(data)
    t3=time.perf_counter()
    print("sum using builit in function={0}(timetaken{0:4f}seconds)".format(builtin_result,t3-t2))
    print("sum using user defined function={0}(timetaken{0:4f}seconds)".format(my_result,t1-t0))