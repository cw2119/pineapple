from flask import Flask, render_template, request
import requests
app = Flask ("MyApp")

def send_simple_message(email_variable):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox2a20858c8faa46aea09522cb57134dea.mailgun.org/messages",
		auth=("api", "1ebb831d8a43f86b60b93926ea6657f9-de7062c6-9de671ea"),
		data={"from": "Excited User <mailgun@sandbox2a20858c8faa46aea09522cb57134dea.mailgun.org>",
			"to": [email_variable],
			"subject": "Hello ",
			"text": ";alskdfjasdf"})

@app.route("/")
def hello():
    return "Hello!"
@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())
@app.route("/signup",methods = ["POST"])
def sign_up():
    form_data= request.form
    send_simple_message(form_data["email"])
    print form_data["email"]
    return "all OK"

app.run(debug=True)
