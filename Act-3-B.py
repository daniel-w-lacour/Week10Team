# version using statistics library
def minmeanmax(list):
    from statistics import mean
    return min(list),mean(list),max(list)
# version not using statistics library
def minmeanmax2(list):
    count = 0
    sum = 0
    for i in list:
        sum += i
        count += 1
    return min(list),sum/count,max(list)