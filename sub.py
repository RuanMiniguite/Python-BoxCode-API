import zmq
import sys

IP_ADDRESS = "0.0.0.0"
TOPIC = "test"

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect(f"tcp://{IP_ADDRESS}:5501")

# Subscribe to the topic
sock.subscribe(f"{TOPIC}")

print(f"Starting receiver from topic(s) {TOPIC}...")

def validarCpf(cpf):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

while True:
    msg_string = sock.recv_string()
    msg_json = sock.recv_json()
    print(f"cpf: {msg_string}.")
    v = validarCpf(msg_string)
    sock.send(v)

sock.close()
ctx.term()
