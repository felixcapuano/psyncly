def dev():
    import uvicorn

    uvicorn.run("psyncly.app:app", port=8080, reload=True)


def format():
    import subprocess

    subprocess.run(["isort", "."])
    subprocess.run(["black", "."])


def feed():
    from multiprocessing import Process

    import httpx
    import uvicorn

    url = "http://localhost:8080"

    server = Process(
        target=uvicorn.run,
        args=("psyncly.app:app",),
        kwargs={"port": 8080},
    )
    server.start()

    for i in range(1):
        res = httpx.post(
            url + "/v1/users",
            json={
                "username": f"user{i}",
                "email": f"user{i}@example.com",
            },
        )
        if res.status_code != 201:
            print(res.text)

        res = httpx.post(
            url + "/v1/playlists",
            json={
                "name": f"playlist{i}",
                "owner_id": i + 1,
            },
        )
        if res.status_code != 201:
            print(res.text)

    for i in range(4):
        res = httpx.post(
            url + "/v1/tracks",
            json={
                "title": f"track{i}",
                "isrc": f"isrc{i}",
                "artist": f"artist{i}",
            },
        )
        if res.status_code != 201:
            print(res.text)

    server.terminate()
