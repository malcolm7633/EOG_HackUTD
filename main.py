from websocket import create_connection
ws = create_connection("wss://2021-utd-hackathon.azurewebsites.net")
ws.send("Hello, World")
result = ws.recv()
print(result)
ws.close()
