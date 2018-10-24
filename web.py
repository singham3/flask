from flask import Flask,render_template, request
import pymysql.cursors




app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='flask',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)










@app.route('/')
def hello_world():
    return render_template('slider.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        message = request.form.get('message')
        connection = pymysql.connect(host='localhost', user='root', password='root', db='flask')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO contact ( name, phone_number,email, message) VALUES ( name, phone_number,email,message);")
            connection.commit()
        print(name,phone_number,email,message)
    return render_template('contact.html')



@app.route('/404')
def _404():
    return render_template('404.html')

@app.route('/blog-home-1')
def blog_home_1():
    return render_template('blog-home-1.html')

@app.route('/blog-home-2')
def blog_home_2():
    return render_template('blog-home-2.html')

@app.route('/blog-post')
def blog_post():
    return render_template('blog-post.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/full-width')
def full_width():
    return render_template('full-width.html')

@app.route('/portfolio-1')
def portfolio_1():
    return render_template('portfolio-1-col.html')

@app.route('/portfolio-2')
def portfolio_2():
    return render_template('portfolio-2-col.html')

@app.route('/portfolio-3')
def portfolio_3():
    return render_template('portfolio-3-col.html')

@app.route('/portfolio-4')
def portfolio_4():
    return render_template('portfolio-4-col.html')

@app.route('/portfolio-item')
def portfolio_item():
    return render_template('portfolio-item.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')



@app.route('/<username>')
def profile(username):
    return render_template('profile.html',name=username)

if __name__ == '__main__':
    app.run(debug=True)
