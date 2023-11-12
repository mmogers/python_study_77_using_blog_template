from flask import Flask , redirect
import datetime
app = Flask(__name__)


@app.route('/latvianwalk/blog/80')
def eighty():
  blogname = "My Walking Blog"
  heading = "Walking Latvia"
  date = datetime.date.today()
  text = "Embarked on a serene journey around Ummis Lake today. The calm waters, the surrounding nature, and the soothing breeze created a peaceful atmosphere. It was a perfect day for a leisurely walk."


  page = ""
  f = open("template/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{heading}", heading)
  page = page.replace("{date}", str(date))
  page = page.replace("{text}", text)
  page = page.replace("{name of the blog}", blogname)

  return page

@app.route('/blog/latvianwalk/80')
def eightyRedirect():
  return redirect('/latvianwalk/blog/80')

@app.route('/foodblog/blog/1')
def first():
  blogname = "My Food Blog"
  heading = "A Culinary Adventure Begins"
  date = datetime.date.today()
  text = """Today marks the inception of my culinary journey, a venture into the vibrant world of flavors and gastronomic delights. In my first culinary exploration, I delved into the art of crafting a classic Italian dish — Spaghetti Bolognese.

The kitchen buzzed with the aromatic symphony of tomatoes, garlic, and basil as I meticulously prepared the rich tomato sauce. The sizzle of ground beef in the pan added a savory note to the air, creating an anticipation for the feast that was about to unfold.

As the spaghetti boiled to al dente perfection, I marveled at the harmony of ingredients coming together. The final creation, adorned with a sprinkle of Parmesan, promised a taste of Italy in every forkful.

Join me on this delectable journey as I document my culinary adventures, savoring the diverse tastes and aromas that the world of food has to offer."""

  page = ""
  f = open("template/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{heading}", heading)
  page = page.replace("{date}", str(date))
  page = page.replace("{text}", text)
  page = page.replace("{name of the blog}", blogname)

  return page

@app.route('/blog/foodblog/1')
def firstRedirect():
  return redirect('/foodblog/blog/1')

  

app.run(host='0.0.0.0', port=81)