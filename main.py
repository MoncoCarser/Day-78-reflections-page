from flask import Flask, redirect
import random

app = Flask(__name__, static_url_path="/static")

#web page shows a random image from this list
images = ["1.webp","2.webp","3.webp","4.webp","5.webp","6.webp","7.jpg","8.webp"]

#list containts comments for each day
storage_list = [
    ["78", "After #313 attempts eveything is working! ❤️ Flask is confusing, but slowly learning. "], 
    ["79", "What will the future bring"],
    ["80", "I don't know about this day yet"],
    ["81", "hmmmm"],
    ["82", "COOOOOOOOOL"],
    ["83", "whaz?"],
    ["84", "Donald Duck"],
    ["85", "Rebooting"],
    ["86", "Dany says AAAA"],
    ["87", "a-a-a--a-aa"],
    ["88", "html, css and js.."],
    ["89", "learning"],
    ["90", "Flask is different"],
    ["91", "html+css is surprisingly powerful"],
    ["92", "lalalala"],
    ["93", "going for 100!"],
    ["94", "So close"],
    ["95", "Nothing will stop me!"],
    ["96", "AAAAAAAAAA"],
    ["97", "I'm coming!"],
    ["98", "Keep learning"],
    ["99", "Geronimooooooo"],
    ["100", "100!"],
                ]

@app.route("/")
def index():
    image = random.choice(images)
    page = ""
    f = open("html/template.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{day_number}", "78-100") 
    page = page.replace("{reflections}", "Following pages will give details")
    page = page.replace("{random_image}", image)
    return page

@app.route("/<day_number>")
def day(day_number):
    image = random.choice(images)
    index_num = int(day_number) - 78
    page = ""
    f = open("html/template.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{day_number}", day_number) 
    page = page.replace("{reflections}", storage_list[index_num][1])
    page = page.replace("{random_image}", image)
    return page

app.run(host='0.0.0.0', port=81)
