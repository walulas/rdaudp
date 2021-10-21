

###===========================================================###
 ###================ RDA5807M>><<MicroPython ================###
###===========================================================###


from machine import I2C, Pin

iic = I2C(sda = Pin(4), scl = Pin(5), freq = 400000)
reg = {2:0xc001, 3:0x0008, 5:0x0081, 7:0x4201}
i2r = iic.readfrom_mem
i2w = iic.writeto_mem
bit = bytearray(2)
stf = 880
rda = 17
vmx = 15

def urip():
	for b in reg:
		i2w(17, b, int.to_bytes(reg[b], 2, 'big'))
	freq(stf)

def freq(mhz):
	mhz = (mhz * 100) - 76000
	i2w(17, 8, int.to_bytes(mhz, 2, 'big'))

def mute():
	val = i2r(17, 2, 2)
	bit[1] = val[1]
	if ((val[0] >> 4) >> 2) & 1:
		bit[0] = val[0] - 64
	else:
		bit[0] = val[0] + 64
	i2w(17, 2, bit)

def bass():
	val = i2r(17, 2, 2)
	bit[1] = val[1]
	if not((val[0] >> 4) & 1):
		bit[0] = val[0] + 16
	i2w(17, 2, bit)

def siji():
	val = i2r(17, 2, 2)
	bit[1] = val[1]
	if not((val[0] >> 4) & 2):
		bit[0] = val[0] + 32
	i2w(17, 2, bit)

def loro():
	val = i2r(17, 2, 2)
	bit[1] = val[1]
	if ((val[0] >> 4) & 2) > 1:
		bit[0] = val[0] - 32
	i2w(17, 2, bit)

def rata():
	val = i2r(17, 2, 2)
	bit[1] = val[1]
	if (val[0] >> 4) & 1:
		bit[0] = val[0] - 16
	i2w(17, 2, bit)

def mati():
	i2w(17, 2, b'\x00\x00')

def volN(N):
	val = i2r(17, 5, 2)
	bit[0] = val[0]
	bit[1] = 128 + N
	i2w(17, 5, bit)

def volU():
	val = i2r(17, 5, 2)
	bit[1] = val[1]+1
	if val[1]&15 == vmx:
		bit[1] -= 1
	i2w(17, 5, bit)

def volD():
	val = i2r(17, 5, 2)
	bit[1] = val[1]
	if val[1]&15 > 0:
		bit[1] -= 1
	i2w(17, 5, bit)



###===©===============================================ls.18===###
