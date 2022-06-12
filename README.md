Server pong exercise
====================
In this exercise we will have two servers playing a pong game,
the servers can be coded using nodejs(express) or **python (FasAPI)**.

During the game there are two instances of the same server code running and a pong cli command line tool used to start,
pause,resume and stop the game.

## The game:
Once an instance of the server(lets call it instance1) receives a ping rest request it will reply
"pong" in the response body and send his ping request to the other server instance(instance2) after <pong_time_ms>
 has passed. The two servers will ping each other, where
  pong_time_ms milliseconds passes between each ping and the next ping is initiated by the last instance that responded to ping.

### CLI
The game will be controlled by a cli tool (nodejs or **python**)
CLI usage:
	`python pong-cli.py <command: string> <param: number>`
cli commands:
`python pong-cli.py start <pong_time_ms>` : start the game with pong_time_ms as the interval between pongs
`python pong-cli.py pause` : pause the game, servers are still alive
`python pong-cli.py resume` : resume the game from previous pause point.
`python pong-cli.py stop` : stop the game (and clean all resources)

example:
`python pong-cli.py start 1000` : start pong game with 1 second between pongs.
