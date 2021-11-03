def avgvel(time, distance):
    vellist = []
    for index, val in enumerate(time):
        if time[index]==time[-1]:
            break
        velocity = (distance[index+1]-distance[index])/(time[index+1]-time[index])
        vellist.append(velocity)
    return  vellist