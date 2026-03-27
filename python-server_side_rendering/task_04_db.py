from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """Lit et retourne les produits depuis products.json"""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Lit et retourne les produits depuis products.csv"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    """Lit et retourne les produits depuis products.db"""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
    except sqlite3.Error as e:
        return None

    return products


@app.route('/products')
def products():
    # 1. Récupère les paramètres de l'URL
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 2. Vérifie la source et lit les données
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html',
                                   error="Database error occurred")
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    # 3. Filtre par id si fourni
    if product_id:
        data = [p for p in data if p['id'] == int(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
