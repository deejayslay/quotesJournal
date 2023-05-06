from website import create_app


app = create_app()

if __name__ == "__main__":  # only when main.py is ran
    app.run(debug=True)  # run flask application, start web server
    # debug=True == whenever change to code is made, server will be re-run automatically
