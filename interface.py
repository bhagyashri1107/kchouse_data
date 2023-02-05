from flask import Flask ,request , jsonify
import numpy as np
from test import HousePrice
import config1

app = Flask(__name__)

@app.route('/house_price')
def house_price():
    data = request.form
    print(data)

    # date = eval(data['date'])
    bedrooms = eval(data['bedrooms'])
    bathrooms = eval(data['bathrooms'])
    sqft_living = eval(data['sqft_living'])
    sqft_lot = eval(data['sqft_lot'])
    floors = eval(data['floors'])
    waterfront = eval(data['waterfront'])
    view = eval(data['view'])
    condition = eval(data['condition'])
    grade = eval(data['grade'])
    sqft_above = eval(data['sqft_above'])
    sqft_basement = eval(data['sqft_basement'])
    yr_built = eval(data['yr_built'])
    yr_renovated = eval(data['yr_renovated'])
    zipcode = eval(data['zipcode'])
    lat = eval(data['lat'])
    long = eval(data['long'])
    sqft_living15 = eval(data['sqft_living15'])
    sqft_lot15 = eval(data['sqft_lot15'])

    MyObj = HousePrice()

    price  = MyObj.pred_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,
    waterfront,view,condition,grade, sqft_above,sqft_basement,yr_built,yr_renovated,
    zipcode,lat,long,sqft_living15,sqft_lot15)

    return jsonify({'Price of house by prediction is :': price})

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = 5500 , debug = False)