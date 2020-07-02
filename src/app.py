from flask import Flask

app = Flask(__name__)


def get_message():
    return """
  <h1>Hello!</h1>
  <p>This is a test flask application</p>
  """


@app.route("/")
def index():
    return get_message()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
