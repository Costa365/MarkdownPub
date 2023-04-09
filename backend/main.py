import uvicorn

app_name="app.main:app"
host="0.0.0.0"
port=8000

if __name__ == '__main__':
    uvicorn.run(app_name, host=host, port=port)
