from flask import Flask

app = Flask(__name__)

HOMEPAGE_HTML = """
<html>
<h1>Welcome to my personal homepage!
</h1>
<p>
My name's daniel. I'm a GIS professional based in NYC. I am passionate about improving access to active transportation
</p>
</html>
"""

@app.route('/', methods=['GET'])
def hello_world():
	return HOMEPAGE_HTML

ACTIVITIES_LIST = ['skiing','flying','working','shooting','screaming','living','training']
@app.route('/activities/<index>', methods=['GET'])
def activites(index):
	return ACTIVITIES_LIST[int(index)]


if __name__ == '__main__':
	app.run()