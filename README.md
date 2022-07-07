1st Api: - /countries - get all countries in the dataset (names, ids and their possible values for startYear and endYear)

  Live link for 1st Api - https://gh-api-1.herokuapp.com/countries

  I have tested this API on postman for better presentation. Some screenshots are attached: -
 
 

2nd Api: - /country/id?queries=explained-below
    o	temporal queries - startYear | endYear
    o	parameters queries - one or parameters (e.g, CO2 or CO2 and NO2)
    o	should return all values for the selected parameters between startYear and endYear
    
  Live link for 2nd Api - https://gh-api-1.herokuapp.com/country/30?startYear=2009&endYear=2014&category=n2o%20and%20co2
  
  The above link can be modified accordingly. Some rules for using this endpoint: -
    •	startYear and endYear can be tweaked between 1990 and 2014.
    •	There are overall 43 different countries each of them having unique “country_id” which can be viewed from the 1st Api result.
    •	Category is cleaned and shortened in dataset to following format: -
        CH4, CO2, GHGS, HFCS, N2O, NF3, PFCS, SF6
        They can be passed in URL as single or multiple parameters.
        Eg: - category=CO2 and N20,
                 category=HFCS or
                 category=ch4 and co2
