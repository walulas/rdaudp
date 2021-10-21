


###=====================================================================###
 ###========================= UDP>><<RDA5807M =========================###
###=====================================================================###



import rda, socket
from network import WLAN

udp = socket.socket(2, 2)
fpss = bytearray(4)
fpss[0] = 88
frq = int(str(fpss[0]) + str(fpss[1]))
udp.bind((WLAN(0).ifconfig()[0], 10894))

while True:
	cmd, ips = udp.recvfrom(1024)
	if cmd:
		if cmd == b'oi':
			if not(fpss[2]):
				fpss[2] = 1
				rda.urip()
			else:
				fpss[2] = 0
				rda.mati()
		if cmd == b'sm':
			if fpss[3]:
				fpss[3] = 0
				rda.loro()
			else:
				fpss[3] = 1
				rda.siji()
		if cmd == b'mt':
			rda.mute()
		if cmd == b'v+':
			rda.volU()
		if cmd == b'v-':
			rda.volD()
		if cmd == b'bs':
			rda.bass()
		if cmd == b'rt':
			rda.rata()
		if cmd[0] == 61:
			rda.freq(int(cmd[1:].decode()))
			udp.sendto(cmd[1:], (ips[0], 10894))
		if cmd[0] == 99:
			fpss[0] = int(cmd[1:].decode())
			frq = int(str(fpss[0]) + str(fpss[1]))
			rda.freq(frq)
		if cmd[0] == 112:
			fpss[1] = int(cmd[1:].decode())
			frq = int(str(fpss[0]) + str(fpss[1]))
			rda.freq(frq)
		if cmd[0] == 120:
			rda.volN(int(cmd[1:].decode()))
		if cmd == b'f+':
			frq += 1
			rda.freq(frq)
			udp.sendto(str(frq).encode(), (ips[0], 10894))
		if cmd == b'f-':
			frq -= 1
			rda.freq(frq)
			udp.sendto(str(frq).encode(), (ips[0], 10894))




###===©=========================================================ls.18===###
