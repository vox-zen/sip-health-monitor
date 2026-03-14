import json
import socket
import time


def check_sip(host, port, timeout=3):
    try:
        start = time.time()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        sock.connect((host, port))

        latency = (time.time() - start) * 1000

        sock.close()

        return True, round(latency, 2)

    except Exception:
        return False, None


def main():
    with open("monitor/config.json") as f:
        config = json.load(f)

    trunks = config["trunks"]

    for trunk in trunks:

        name = trunk["name"]
        host = trunk["host"]
        port = trunk["port"]

        status, latency = check_sip(host, port)

        print("\nTrunk:", name)

        if status:
            print("Status: OK")
            print("Latency:", latency, "ms")
        else:
            print("Status: DOWN")


if __name__ == "__main__":
    main()
