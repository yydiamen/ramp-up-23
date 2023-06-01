def ave_spd(up_time, up_spd, down_spd):
    leng = up_spd*up_time
    downtime = leng/down_spd
    av = leng*2/(up_time+downtime)
    return av
