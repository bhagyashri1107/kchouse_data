import pickle as pkl
import numpy as np
import config1


class HousePrice():
    def __init__(self):
        print('we r in init of kc_house_price_pred')

        with open(config1.model_path , 'rb') as f:
            self.model = pkl.load(f)

    
    def pred_price(self , date , bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade, 
                   sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,
                   sqft_lot15):
        
        test_array = np.zeros(self.model.n_features_in_)

        test_array[0] = date
        test_array[1] = bedrooms
        test_array[2] = bathrooms
        test_array[3] = sqft_living
        test_array[4] = sqft_lot
        test_array[5] = floors
        test_array[6] = waterfront
        test_array[7] = view
        test_array[8] = condition
        test_array[9] = grade
        test_array[10] = sqft_above
        test_array[11] = sqft_basement
        test_array[12] = yr_built
        test_array[13] = yr_renovated
        test_array[14] = zipcode
        test_array[15] = lat
        test_array[16] = long
        test_array[17] = sqft_living15
        test_array[18] = sqft_lot15

        result = self.model.predict([test_array])[0]

        return result
            
