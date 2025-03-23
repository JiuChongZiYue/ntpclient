#!/usr/bin/env python
'''
CS352 Assignment 1: Network Time Protocol
You can work with 1 other CS352 student
DO NOT CHANGE ANY OF THE FUNCTION SIGNATURES BELOW
'''
from socket import socket, AF_INET, SOCK_DGRAM
import struct
from datetime import datetime




def getNTPTimeValue(server="time.apple.com", port=123) -> (bytes, float, float):

    sock = socket(AF_INET, SOCK_DGRAM)



    pkt_q = b'\x1b' + 47 * b'\0'
    
    sock.sendto(pkt_q, (server, port))

    time_difference = datetime.utcnow() - datetime(1970, 1, 1, 0, 0, 0)
    secs = time_difference.days*24.0*60.0*60.0 + time_difference.seconds
    T1 = secs + float(time_difference.microseconds / 1000000.0)

    
    time_difference = datetime.utcnow() - datetime(1970, 1, 1, 0, 0, 0)
    secs = time_difference.days*24.0*60.0*60.0 + time_difference.seconds
    T4 = secs + float(time_difference.microseconds / 1000000.0)

    data, _ = sock.recvfrom(1024)#is what is this 1024 means? bit or byte? and why there are 2 return
    
    #pkt = data[0:48]
    #ntp_response = '!12I'      #why 12I?
    #ntp_response = struct.unpack('!12I', pkt[0:48])
    

    
    
    
    
    return (data, T1, T4)



def ntpPktToRTTandOffset(pkt: bytes, T1: float, T4: float) -> (float, float):


    pkttt = pkt[0:48]
    ntpr = '!12I'      #why 12I?
    ntpr = struct.unpack('!12I', pkttt[0:48])

    TIME_1970 = 2208988800
    T2 = ntpr[8] + ntpr[9] / 2.**32 - TIME_1970
    T3 = ntpr[10] + ntpr[11] / 2.**32 - TIME_1970

    rtt = T4 - T1
    offset = ((T2 - T1) + (T3 - T4)) / 2

    
    return (rtt, offset)



def getCurrentTime(server="time.apple.com", port=123, iters=20) -> (float):

    for x in range(iters):#what is the iter means?

        time_difference = datetime.utcnow() - datetime(1970, 1, 1, 0, 0, 0)
        secs = time_difference.days*24.0*60.0*60.0 + time_difference.seconds
        T1 = secs + float(time_difference.microseconds / 1000000.0)


        pkt, T1, T4 = getNTPTimeValue(server, port)
    
        rtt, offset = ntpPktToRTTandOffset(pkt, T1, T4)
        
        sumoffset = 0.0
        sumoffset = sumoffset + offset
    
        currentTime = T4 + offset
    
    currentTime = sumoffset + currentTime
    
    
    return currentTime



if __name__ == "__main__":
    current_time = getCurrentTime()
    print(getCurrentTime())






