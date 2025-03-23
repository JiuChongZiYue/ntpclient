
Kanran Peng

File: ntpclient.py

Features: 
    Sends an NTP request to a time server (default: time.apple.com)

    Receives the NTP response and extracts timestamp fields

    Computes the RTT and offset between local time and server time

    Returns an estimate of the current accurate UTC time



1. getNTPTimeValue(server, port)
    Sends a binary-formatted NTP request packet to the server.

    Records timestamps T1 (send time) and T4 (receive time).

    Receives the 48-byte NTP response.


2. ntpPktToRTTandOffset(pkt, T1, T4)
    Unpacks 12 unsigned 32-bit integers from the 48-byte response.

    Extracts timestamps T2 (server receive time) and T3 (server transmit time).

    Computes RTT and offset using the standard NTP formula.


3. getCurrentTime(server, port, iters)
    Repeats the request iters times (default: 20).

    Averages the offset to improve accuracy.

    Returns the adjusted time estimate.