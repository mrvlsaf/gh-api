from functools import cache
import pandas as pd
from flask import Flask, appcontext_popped, request
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# df1 = pd.read_sql_query("SELECT * from inputData", conn)
# df = df1._convert(numeric=True)
app.config.from_mapping(config)
cache = Cache(app)

df = pd.read_csv('greenhouse_gas_inventory_data_data.csv')

@app.route('/countries', methods=['GET', 'POST'])
def main(): 
    result_start_year = df.loc[df['year'] == 1990]
    result_end_year = df.loc[df['year'] == 2014]
    result = pd.merge(result_start_year, result_end_year, on=["country_id", "category", "country_or_area"])
    result = result.drop(['id_x', 'id_y', 'year_x', 'year_y'], axis=1)
    result.rename(columns = {'value_x':'start_year_value', 'value_y':'end_year_value'}, inplace = True)
    return result.to_json(orient="index")

@app.route('/country/<int:id>', methods=['GET'])
def getSpecificCountry(id):
    query = request.args.to_dict()
    catg_word = query['category'].upper()
    category = catg_word.split(' AND ')
    result = df.loc[(df['year'] >= int(query["startYear"])) & (df['year'] <= int(query["endYear"])) & (df['country_id'] == id) & (df['category'].isin(category))]
    result = result.drop(['id'], axis=1).sort_values('year')
    return result.to_json(orient="index")

if __name__ == '__main__':
    app.run(debug=True)
