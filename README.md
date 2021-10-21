# RDA >>><<< UDP
RDA5807M Over MicroPython UDP Protocol.
## Usage
Simple, Just Send `Command` Below.
### `Command:`
```bash
f+  for  Increasing Frequency
f-  for  Decreasing Frequency
v+  for  Increasing Volume
v-  for  Decreasing Volume
rt  for  Flat Audio Output
bs  for  BassBoost Mode ON
oi  for  Power Toggle (on\off)
mt  for  Mute Toggle (mute\unmute)
mn  for  Stereo Toggle (stereo\force mono)
=<freq>  for  Directly Frequency (760 - 1080)

```
## Installation
```python
exec(open("rdaudp.py").read(), globals())
```
## Run While Boot
```python
import uos

uos.rename("rdaudp.py", "main.py")
```
##
![View Control Using UDP Comtroller App](https://raw.githubusercontent.com/walulas/rdaudp/master/udp.jpg)
## Info
More Support, Contact Me On [Twitter](https://twitter.com/satguz) or
[Instagram](https://instagram.com/walulas).
