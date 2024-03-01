import base64
import textwrap
import sys

print("Please enter/paste the Cisco key 'Data'. Ctrl-D or Ctrl-Z ( windows ) or empty newline to save it.", file=sys.stderr)
hexstring = ""
while True:
    try:
        line = input()
        if line == "":
            break
        hexstring += line
    except EOFError:
        break

binary_content = bytes.fromhex(hexstring)
pem_key = "-----BEGIN PUBLIC KEY-----\n"
pem_key += "\n".join(textwrap.wrap(base64.b64encode(binary_content).decode('ascii'), 64))
pem_key += "\n-----END PUBLIC KEY-----"
print(pem_key)
print("Use followng to convert the key and get the fingerprint:", file=sys.stderr)
print("OpenSSH format:      ssh-keygen -i -m PKCS8 -f keyfile.pem > rsa.pub", file=sys.stderr)
print("SHA256 fingerprint:  ssh-keygen -lf rsa.pub", file=sys.stderr)
print("MD5 fingerprint:     ssh-keygen -E md5 -lf rsa.pub", file=sys.stderr)


