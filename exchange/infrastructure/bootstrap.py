from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world!"


def main():
    home()
    app.run(port=7000, debug=True)


if __name__ == "__main__":
    main()
