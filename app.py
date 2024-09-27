from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Definisikan set data minuman
drinks = [
    {'name': 'Americano', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit', 'image': 'americano.webp', 'description': 'A strong and bold iced coffee.'},
    {'name': 'Espresso', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit', 'image': 'espresso.jpg', 'description': 'A rich and intense iced espresso.'},
    {'name': 'V60', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit', 'image': 'v60.jpg', 'description': 'A smooth and flavorful iced V60 coffee.'},
    {'name': 'Latte', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis', 'image': 'latte.jpg', 'description': 'A refreshing iced latte with a smooth and creamy texture.'},
    {'name': 'Affogato', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis', 'image': 'affogato.webp', 'description': 'A classic Italian dessert with hot espresso poured over vanilla ice cream.'},
    {'name': 'Caramel Macchiato', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis', 'image': 'caramel.webp', 'description': 'An iced coffee drink with caramel and milk.'},
    {'name': 'Americano', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit', 'image': 'americano.webp', 'description': 'A strong and bold hot coffee made with espresso and hot water.'},
    {'name': 'Espresso', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit', 'image': 'espresso.jpg', 'description': 'A small but intense shot of pure coffee.'},
    {'name': 'V60', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit', 'image': 'v60.jpg', 'description': 'A hand-brewed coffee using the V60 method, known for its clean and bright flavor.'},
    {'name': 'Latte', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'manis', 'image': 'latte.jpg', 'description': 'A smooth and creamy hot latte with a balanced coffee flavor.'},
    {'name': 'Fresh Milk', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis', 'image': 'fresh_milk_ice.webp', 'description': 'Cold and refreshing milk, served chilled.'},
    {'name': 'Hot Fresh Milk', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis', 'image': 'fresh_milk_hot.jpg', 'description': 'Warm and comforting hot milk.'},
    {'name': 'Matcha Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis', 'image': 'matcha_latte_ice.jpg', 'description': 'An iced latte with matcha green tea and milk.'},
    {'name': 'Matcha Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis', 'image': 'matcha_latte_hot.webp', 'description': 'A hot latte made with matcha green tea and milk.'},
    {'name': 'Red Velvet Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis', 'image': 'red_velvet_ice.jpg', 'description': 'An iced latte with the rich and creamy flavor of red velvet cake.'},
    {'name': 'Red Velvet Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis', 'image': 'red_velvet_hot.jpg', 'description': 'A hot latte with the rich and creamy flavor of red velvet cake.'},
    {'name': 'Taro Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis', 'image': 'taro_latte_ice.jpg', 'description': 'An iced latte with a sweet and nutty taro flavor.'},
    {'name': 'Taro Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis', 'image': 'taro_latte_hot.png', 'description': 'A hot latte with a sweet and nutty taro flavor.'},
    {'name': 'Lychee Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut', 'image': 'leci.jpg', 'description': 'An iced mojito with a refreshing lychee flavor.'},
    {'name': 'Lime Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut', 'image': 'lime.jpg', 'description': 'An iced mojito with a tangy lime flavor.'},
    {'name': 'Strawberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut', 'image': 'strawberry.jpg', 'description': 'An iced mojito with a sweet and tangy strawberry flavor.'},
    {'name': 'Blackberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut', 'image': 'blackberry.jpg', 'description': 'An iced mojito with a sweet and tangy blackberry flavor.'},
    {'name': 'Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis', 'image': 'iced_tea.jpg', 'description': 'Iced tea, sweetened and refreshing.'},
    {'name': 'Hot Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis', 'image': 'hot_tea.jpg', 'description': 'Hot tea, sweetened and comforting.'},
    {'name': 'Lemon Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'kecut', 'image': 'lemon_tea_ice.jpg', 'description': 'Iced tea with a tangy lemon flavor.'},
    {'name': 'Lemon Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'kecut', 'image': 'lemon_tea_hot.jpg', 'description': 'Hot tea with a tangy lemon flavor.'},
    {'name': 'Lychee Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis', 'image': 'lychee_tea_ice.jpg', 'description': 'Iced tea with a sweet lychee flavor.'},
    {'name': 'Lychee Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis', 'image': 'lychee_tea_hot.webp', 'description': 'Hot tea with a sweet lychee flavor.'},
]

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/suhu')
def suhu():
    return render_template('suhu.html')

@app.route('/select_suhu', methods=['POST'])
def select_suhu():
    session['suhu'] = request.form['suhu']
    return redirect(url_for('based'))

@app.route('/based')
def based():
    return render_template('based.html')

@app.route('/select_based', methods=['POST'])
def select_based():
    session['based'] = request.form['based']
    return redirect(url_for('rasa'))

@app.route('/rasa')
def rasa():
    return render_template('rasa.html')

@app.route('/select_rasa', methods=['POST'])
def select_rasa():
    session['rasa'] = request.form['rasa']
    user_preferences = {
        'suhu': session.get('suhu'),
        'based': session.get('based'),
        'rasa': session.get('rasa')
    }
    recommendations = recommend_drinks(drinks, user_preferences)
    return render_template('result.html', recommendations=recommendations)


def recommend_drinks(data, preferences):
    filtered_drinks = data
    for attribute, value in preferences.items():
        filtered_drinks = [drink for drink in filtered_drinks if drink[attribute] == value]
    
    return filtered_drinks  # Return only up to 2 recommendations



if __name__ == '__main__':
    app.run(debug=True)
