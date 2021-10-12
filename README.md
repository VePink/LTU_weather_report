# eismoinfo-weather-conditions-service-scraper
 Script EIW_scraper.py every 10 minutes checks http://eismoinfo.lt/weather-conditions-service website and downloads JSON 
 Later data is structured as Pandas dataframe, redundant attributes are removed. Other attributes are saved as coded values. 
 Finaly data is saved as CSV for later analysis.

<img src="/images/datasample.PNG" width="600"/>
 
Script EIW_visualizer.py plots logged data as contour map using Plotly interactive visualization library. 
Live sample of air temperature interactictive plot: https://vepink.github.io/eismoinfo-weather/

<img src="/images/mapsample_airtemp.png" width="600"/>
<img src="/images/mapsample_wind.png" width="600"/>

More info about weather open data service: https://maps.eismoinfo.lt/portal/apps/sites/#/npp/pages/weather