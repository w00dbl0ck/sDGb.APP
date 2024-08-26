from flask import Flask, render_template, request, redirect, url_for

print(__name__)

app = Flask(__name__)


@app.route('/')
def helloworld():
  return 'render_template, hello .,.,.,.,. wo .  rld'


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
