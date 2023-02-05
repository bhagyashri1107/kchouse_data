from flask import Flask , request , jsonify , render_template
import numpy as np
from test import HousePrice
import config1
import traceback


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('house_price.html')


@app.route('/house_price' , methods = ['GET' , 'POST'])
def house_price():
    try:
        if request.method == 'POST':
            data = request.form.get
            print(data)

            # date =  data('date' )
            bedrooms = data('bedrooms')
            bathrooms =  data('bathrooms' )
            sqft_living =  data('sqft_living' )
            sqft_lot =  data('sqft_lot' )
            floors =  data('floors' )
            waterfront =  data('waterfront' )
            view =  data('view' )
            condition =  data('condition' )
            grade =  data('grade' )
            sqft_above =  data('sqft_above' )
            sqft_basement =  data('sqft_basement' )
            yr_built =  data('yr_built' )
            yr_renovated =  data('yr_renovated' )
            zipcode =  data('zipcode' )
            lat =  data('lat' )
            long =  data('long' )
            sqft_living15 =  data('sqft_living15' )
            sqft_lot15 =  data('sqft_lot15' )

            MyObj = HousePrice()

            price  = MyObj.pred_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade, 
                        sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,
                        sqft_lot15)

            return render_template('house_price.html' , prediction = price)

    
        else:
            data = request.args.get
            print(data)

            # date =  data('date')
            bedrooms = data('bedrooms')
            bathrooms =  data('bathrooms' )
            sqft_living =  data('sqft_living' )
            sqft_lot =  data('sqft_lot' )
            floors =  data('floors' )
            waterfront =  data('waterfront' )
            view =  data('view' )
            condition =  data('condition' )
            grade =  data('grade' )
            sqft_above =  data('sqft_above' )
            sqft_basement =  data('sqft_basement' )
            yr_built =  data('yr_built' )
            yr_renovated =  data('yr_renovated' )
            zipcode =  data('zipcode' )
            lat =  data('lat' )
            long =  data('long' )
            sqft_living15 =  data('sqft_living15' )
            sqft_lot15 =  data('sqft_lot15' )

            MyObj = HousePrice()

            price  = MyObj.pred_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade, 
                        sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,
                        sqft_lot15)

            return render_template('house_price.html' , prediction = price)

    except:
        print(traceback.print_exc( ))
        return  jsonify({"Message" : "Unsuccessful"})


if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = config1.PORT , debug = False)