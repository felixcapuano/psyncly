def dev():
    import uvicorn

    uvicorn.run("psyncly.app:app", port=8080, reload=True)


def format():
    import subprocess

    subprocess.run(["isort", "."])
    subprocess.run(["black", "."])
