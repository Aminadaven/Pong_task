import subprocess

from python_on_whales import docker
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pong-cli.py <command>")
        sys.exit(1)
    if sys.argv[1] == "start":
        if len(sys.argv) < 3:
            print("Please specify wait time between pings in milliseconds")
            sys.exit(1)
        try:
            int(sys.argv[2])
        except ValueError:
            print("Please specify wait time between pings as a number")
            sys.exit(1)
        subprocess.run(f"echo PONG_TIME_MS={sys.argv[2]}>.env", shell=True)
        docker.compose.up(detach=True)
    elif sys.argv[1] == "pause":
        docker.compose.pause()
    elif sys.argv[1] == "resume":
        docker.compose.unpause()
    elif sys.argv[1] == "stop":
        docker.compose.down()
    else:
        print("Usage: pong-cli.py start|pause|resume|stop [pong_time_ms]")
