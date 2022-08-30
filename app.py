from flask import Flask, render_template
from items import items

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/<item_type>')
def products(item_type):
    item_list = items[item_type]
    return render_template('products.html', item_type_template=item_type, items_template=item_list)



@app.route('/products/<item_type>/<int:item_id>')
def item (item_type,item_id):
    item_profile = items[item_type][item_id]

    return render_template('item.html',item_profile=item_profile)


if __name__== "__main__":
    app.run(debug=True)
