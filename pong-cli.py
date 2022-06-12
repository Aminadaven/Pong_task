import subprocess

from python_on_whales import docker
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pong-cli.py <command>")
        sys.exit(1)
    status = "NOT_STARTED"
    if sys.argv[1] == "start":
        if status not in ["NOT_STARTED", "STOPPED"]:
            print("Pong is already running")
            sys.exit(1)
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
        status = "STARTED"
    elif sys.argv[1] == "pause":
        if status not in ["STARTED", "RESUMED"]:
            print("Pong is not running")
            sys.exit(1)
        docker.compose.pause()
        status = "PAUSED"
    elif sys.argv[1] == "resume":
        if status != "PAUSED":
            print("Pong is not paused")
            sys.exit(1)
        docker.compose.unpause()
        status = "RESUMED"
    elif sys.argv[1] == "stop":
        if status not in ["STARTED", "PAUSED", "RESUMED"]:
            print("Pong is not running")
            sys.exit(1)
        docker.compose.down()
        status = "STOPPED"
    else:
        print("Usage: pong-cli.py start|pause|resume|stop [pong_time_ms]")
