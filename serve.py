from CTFd import create_app

app = create_app()
app.run(debug=False, threaded=True, host="0.0.0.0", port=4000)
