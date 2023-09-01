import faust

app=faust.App('demo-streaming',broker='kafka://kubernetes.docker.internal:9092')

topic = app.topic('hello_world', value_type=str,value_serializer='raw')

@app.agent(topic)
async def processor(stream):
    async for message in stream:
        print(f'Received {message}')