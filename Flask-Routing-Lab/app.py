from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/product3')
def product3():
    return render_template('product.html', product='Blood', description='My own blood.', price='0.005$', img='../static/blood.jpeg')

@app.route('/product1')
def product1():
    return render_template('product.html', product='God Bless America Cap', description='A cap that celebrates the glory of the United States and the freedom and democracy they spread across the globe.', price='100000000$', img='https://rlv.zcache.com/god_bless_america_trucker_hat-r4fa7e5f225024b66a5499e8f488b090e_eahw0_8byvr_704.webp')

@app.route('/product2')
def product2():
    return render_template('product.html', product='Poster', description='Live love laugh poster featuring Kim Jung Un.', price='800000000000$', img='https://cdn.shopify.com/s/files/1/2666/1642/products/Rocket_Man_1200x1200.png')

@app.route('/product4')
def product4():
    return render_template('product.html', product='Crack', description='Totalee lygal.', price='909999$', img='../static/drugs.jpeg')

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
