from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        products_list = json.load(f)
    return products_list

def read_csv():
    products_list = []
    with open('products.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products_list.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get('items', [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def product():
    source = request.args.get('source', 'json')
    id_param = request.args.get('id', None)

    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if id_param:
        filtered_products = [product for product in products_list if product['id'] == int(id_param)]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products_list = filtered_products

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)