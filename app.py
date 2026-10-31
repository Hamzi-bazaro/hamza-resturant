
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hamza Restaurant | Taste of Happiness</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #111;
    color: white;
}

header {
    background: #171717;
    padding: 18px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.logo {
    color: #f5a623;
    font-size: 25px;
    font-weight: bold;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 8px;
    font-size: 14px;
}

nav a:hover {
    color: #f5a623;
}

.hero {
    min-height: 540px;
    display: flex;
    align-items: center;
    padding: 60px 8%;
    background:
    linear-gradient(90deg, rgba(0,0,0,.9), rgba(0,0,0,.3)),
    url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600")
    center/cover;
}

.hero-content {
    max-width: 600px;
}

.hero h1 {
    font-size: clamp(40px, 7vw, 65px);
    margin-bottom: 20px;
}

.hero h1 span {
    color: #f5a623;
}

.hero p {
    color: #ddd;
    font-size: 18px;
    line-height: 1.7;
    margin-bottom: 25px;
}

.btn {
    display: inline-block;
    background: #f5a623;
    color: #111;
    padding: 14px 27px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
}

.btn:hover {
    background: white;
}

section {
    padding: 65px 7%;
}

.section-title {
    text-align: center;
    font-size: 34px;
    margin-bottom: 12px;
    color: #f5a623;
}

.subtitle {
    text-align: center;
    color: #bbb;
    margin-bottom: 35px;
}

.menu {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
}

.food-card {
    background: #202020;
    border-radius: 12px;
    overflow: hidden;
    transition: .3s;
}

.food-card:hover {
    transform: translateY(-7px);
}

.food-card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
}

.food-info {
    padding: 18px;
}

.food-info h3 {
    margin-bottom: 10px;
}

.food-info p {
    color: #bbb;
    font-size: 14px;
    line-height: 1.5;
}

.price {
    color: #f5a623;
    font-size: 20px;
    font-weight: bold;
    margin: 14px 0;
}

.about {
    background: #1c1c1c;
    text-align: center;
}

.about p {
    max-width: 750px;
    margin: auto;
    color: #ccc;
    line-height: 1.9;
    font-size: 17px;
}

.contact {
    text-align: center;
}

.contact p {
    color: #ccc;
    line-height: 2;
    margin: 15px 0 25px;
}

footer {
    background: #080808;
    text-align: center;
    padding: 25px;
    color: #aaa;
}

footer span {
    color: #f5a623;
}

@media(max-width: 600px) {
    header {
        justify-content: center;
        gap: 15px;
    }

    nav {
        text-align: center;
    }

    nav a {
        display: inline-block;
        margin: 7px;
    }

    .hero {
        min-height: 470px;
    }

    section {
        padding: 50px 6%;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">🍽️ HAMZA RESTAURANT</div>
    <nav>
        <a href="#home">Home</a>
        <a href="#menu">Menu</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<div class="hero" id="home">
    <div class="hero-content">
        <h1>Welcome to <span>Hamza Restaurant</span></h1>
        <p>
        Enjoy delicious food, amazing flavours and
        unforgettable moments. Fresh food, great taste
        and excellent service!
        </p>
        <a class="btn" href="#menu">Explore Our Menu</a>
    </div>
</div>

<section id="menu">
    <h2 class="section-title">Our Special Menu</h2>
    <p class="subtitle">Fresh, delicious and made with love ❤️</p>

    <div class="menu">

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=700" alt="Burger">
            <div class="food-info">
                <h3>Special Burger</h3>
                <p>Juicy burger with fresh vegetables and cheese.</p>
                <div class="price">Rs. 450</div>
            </div>
        </div>

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=700" alt="Pizza">
            <div class="food-info">
                <h3>Italian Pizza</h3>
                <p>Delicious pizza with cheese and fresh toppings.</p>
                <div class="price">Rs. 1200</div>
            </div>
        </div>

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1600891964599-f61ba0e24092?w=700" alt="Steak">
            <div class="food-info">
                <h3>Special Steak</h3>
                <p>Tender steak with a delicious special sauce.</p>
                <div class="price">Rs. 1500</div>
            </div>
        </div>

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=700" alt="Noodles">
            <div class="food-info">
                <h3>Chicken Noodles</h3>
                <p>Hot and tasty noodles with fresh chicken.</p>
                <div class="price">Rs. 550</div>
            </div>
        </div>

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=700" alt="BBQ">
            <div class="food-info">
                <h3>BBQ Platter</h3>
                <p>Delicious grilled meat with special spices.</p>
                <div class="price">Rs. 1800</div>
            </div>
        </div>

        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=700" alt="Milkshake">
            <div class="food-info">
                <h3>Chocolate Shake</h3>
                <p>Cold and creamy chocolate milkshake.</p>
                <div class="price">Rs. 350</div>
            </div>
        </div>

    </div>
</section>

<section class="about" id="about">
    <h2 class="section-title">About Hamza Restaurant</h2>
    <p>
    Welcome to Hamza Restaurant! We believe that great food
    brings people together. Our goal is to serve delicious,
    fresh and high-quality meals in a friendly environment.
    Visit us with your family and friends and enjoy a
    wonderful dining experience.
    </p>
</section>

<section class="contact" id="contact">
    <h2 class="section-title">Contact Us</h2>
    <p>
    📍 Address: Add your restaurant address here<br>
    📞 Phone: Add your phone number here<br>
    🕒 Opening Hours: 10:00 AM - 11:00 PM
    </p>

    <a class="btn"
       href="https://wa.me/923001234567"
       target="_blank">
       Order on WhatsApp
    </a>
</section>

<footer>
    <p>© 2026 <span>Hamza Restaurant</span>. All Rights Reserved.</p>
    <p>Made with ❤️ for food lovers</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
