# cisco-ssh-pubkey
How to decode the public key of cisco devices.

Unfortunately IOS XR and IOS Xe don't display the RSA public key in 
a very friendly format. This repository provides a helper script to 
convert the output to more usable openssl .pem or openssh format.

The 'Data' part is actually the hex representation of an openssl PKCS#8 pem key.
To convert this data to a more convenient format we can use the script [pubkey.py](pubkey.py) and ssh-keygen utility.

```
Router# crypto key generate rsa general-keys myspecialkey

Router# show crypto key mypubkey rsa 
Fri Mar  1 17:07:22.810 UTC
Key label: myspecialkey
Type     : RSA General purpose
Size     : 3072
Created  : 16:33:44 UTC Fri Mar 01 2024
Data     : 
 308201A2 300D0609 2A864886 F70D0101 01050003 82018F00 3082018A 02820181 
 00DFAB36 3B3DA5C3 1D7A0AC0 C694FD6D 62D82F3E 4F77FB84 D4AC5B3F B56DFA87 
 036EA4E7 0472AE49 190F0EF1 6D07FB35 54844671 4B47ACEF 1B7FB264 B737FECB 
 7AACBEDA AD886931 7E49A526 5F9B3FDA 0FCAA38C 737F9429 14251DE7 B98655E3 
 44C2707A 8E927E0F CA7ECEBA 4889BFA3 0EF06D49 E50F7C0A 95561550 F0963C2D 
 3B3558BF FD7D8241 ACFE9352 1B99F403 80BABDE2 41687983 8F83DECA 503E0186 
 324CD572 6F7EF5E4 B201AEBE 9F0D067F 5CDD2458 0D41D83B A0BD98A3 E5AB559D 
 E87C387A E9428F65 F227A29C 0CBAD09D FC6901C5 DA49C946 4C64EF94 C888E54F 
 F64C06B4 4EB8E7EB D28D990A 32DE59CE 9C25705C 1570A220 CC6D00AA F6C6AF4D 
 37422A08 22D9EAD6 8EB40B74 5EA3C308 7B5C266F 6B93A1EA E221BD74 89DFCAE7 
 199A360D B47B0480 0629ECDB B4AB3B56 E6A6A287 9CA137F8 EDCF5C45 E59707A3 
 90019A76 FC6378CC 15C5C140 B1EE3F68 BCBABD9C 1E755607 F8202374 0D3818D1 
 4869B271 35282284 40EA5C29 219F47B9 1CCDDD41 BFEC9A01 EC45D1C9 C83C0129 
 BD020301 0001
 
```


The use the python script in this repo to convert. The script by default
writes the pem key to STDOUT, so you can simply redirect to write it to a file.

The 'Data' part can be copy pasted.

```
$ python3 pubkey.py > keyfile.pem
Please enter/paste the Cisco key 'Data'. Ctrl-D or Ctrl-Z ( windows ) or empty newline to save it.
 308201A2 300D0609 2A864886 F70D0101 01050003 82018F00 3082018A 02820181 
 00DFAB36 3B3DA5C3 1D7A0AC0 C694FD6D 62D82F3E 4F77FB84 D4AC5B3F B56DFA87 
 036EA4E7 0472AE49 190F0EF1 6D07FB35 54844671 4B47ACEF 1B7FB264 B737FECB 
 7AACBEDA AD886931 7E49A526 5F9B3FDA 0FCAA38C 737F9429 14251DE7 B98655E3 
 44C2707A 8E927E0F CA7ECEBA 4889BFA3 0EF06D49 E50F7C0A 95561550 F0963C2D 
 3B3558BF FD7D8241 ACFE9352 1B99F403 80BABDE2 41687983 8F83DECA 503E0186 
 324CD572 6F7EF5E4 B201AEBE 9F0D067F 5CDD2458 0D41D83B A0BD98A3 E5AB559D 
 E87C387A E9428F65 F227A29C 0CBAD09D FC6901C5 DA49C946 4C64EF94 C888E54F 
 F64C06B4 4EB8E7EB D28D990A 32DE59CE 9C25705C 1570A220 CC6D00AA F6C6AF4D 
 37422A08 22D9EAD6 8EB40B74 5EA3C308 7B5C266F 6B93A1EA E221BD74 89DFCAE7 
 199A360D B47B0480 0629ECDB B4AB3B56 E6A6A287 9CA137F8 EDCF5C45 E59707A3 
 90019A76 FC6378CC 15C5C140 B1EE3F68 BCBABD9C 1E755607 F8202374 0D3818D1 
 4869B271 35282284 40EA5C29 219F47B9 1CCDDD41 BFEC9A01 EC45D1C9 C83C0129 
 BD020301 0001

Use followng to convert the key and get the fingerprint:
OpenSSH format:      ssh-keygen -i -m PKCS8 -f keyfile.pem > rsa.pub
SHA256 fingerprint:  ssh-keygen -lf rsa.pub
MD5 fingerprint:     ssh-keygen -E md5 -lf rsa.pub

$ cat keyfile.pem 
-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA36s2Oz2lwx16CsDGlP1tY
tgvPk93+4TUrFs/tW36hwNupOcEcq5JGQ8O8W0H+zVUhEZxS0es7xt/smS3N/7Leq
y+2q2IaTF+SaUmX5s/2g/Ko4xzf5QpFCUd57mGVeNEwnB6jpJ+D8p+zrpIib+jDvB
tSeUPfAqVVhVQ8JY8LTs1WL/9fYJBrP6TUhuZ9AOAur3iQWh5g4+D3spQPgGGMkzV
cm9+9eSyAa6+nw0Gf1zdJFgNQdg7oL2Yo+WrVZ3ofDh66UKPZfInopwMutCd/GkBx
dpJyUZMZO+UyIjlT/ZMBrROuOfr0o2ZCjLeWc6cJXBcFXCiIMxtAKr2xq9NN0IqCC
LZ6taOtAt0XqPDCHtcJm9rk6Hq4iG9dInfyucZmjYNtHsEgAYp7Nu0qztW5qaih5y
hN/jtz1xF5ZcHo5ABmnb8Y3jMFcXBQLHuP2i8ur2cHnVWB/ggI3QNOBjRSGmycTUo
IoRA6lwpIZ9HuRzN3UG/7JoB7EXRycg8ASm9AgMBAAE=
-----END PUBLIC KEY-----

$ ssh-keygen -i -m PKCS8 -f keyfile.pem > rsa.pub
$ cat rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfqzY7PaXDHXoKwMaU/W1i2C8+T3f7hNSsWz+1bfqHA26k5wRyrkkZDw7xbQf7NVSERnFLR6zvG3+yZLc3/st6rL7arYhpMX5JpSZfmz/aD8qjjHN/lCkUJR3nuYZV40TCcHqOkn4Pyn7OukiJv6MO8G1J5Q98CpVWFVDwljwtOzVYv/19gkGs/pNSG5n0A4C6veJBaHmDj4PeylA+AYYyTNVyb3715LIBrr6fDQZ/XN0kWA1B2DugvZij5atVneh8OHrpQo9l8ieinAy60J38aQHF2knJRkxk75TIiOVP9kwGtE645+vSjZkKMt5ZzpwlcFwVcKIgzG0AqvbGr003QioIItnq1o60C3Reo8MIe1wmb2uToeriIb10id/K5xmaNg20ewSABins27SrO1bmpqKHnKE3+O3PXEXllwejkAGadvxjeMwVxcFAse4/aLy6vZwedVYH+CAjdA04GNFIabJxNSgihEDqXCkhn0e5HM3dQb/smgHsRdHJyDwBKb0=
$ ssh-keygen -lf rsa.pub
3072 SHA256:CGyhQmvF56RID+UDZyMc1jNXrZrvPq5RsKu2miaqVTg no comment (RSA)
$ ssh-keygen -E md5 -lf rsa.pub
3072 MD5:e5:4d:9a:b0:7b:e2:a0:a8:f2:e8:e5:85:2a:0b:3c:39 no comment (RSA)
```


NX-OS is a bit more user friendly and shows the key directly in the ssh format, so we don't need the script above:

```
N9K# show ssh key 
**************************************
rsa Keys generated:Fri Jul 13 16:42:02 2018

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC6zINHCebW84QvfmtqgiNkTUJNq7TQ4RqNsrqKhfRuTbK+q6f9it8Hb+M8+aWEYueweaH3viyF5quSIIeithQXBmD1/6dAF9PfE9mtqHUbkvawNSrWL3+Y8EZKtzd9NdzQnv4xJ17Iyb5yxdVSND89BrqfokRYSIKyoTOQV6VOdw==

bitcount:1024
fingerprint:
SHA256:z8UjzespN2Si+w7bLILYrIpT6XX4Wa24ErJN4bP6abc
**************************************
could not retrieve dsa key information
**************************************
could not retrieve ecdsa key information
**************************************
N9K-IPN2# 
```