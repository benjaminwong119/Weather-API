# Weather-API

## Introduction
The purpose of this project is use AWS EC2 and build a Python script that interacts with an API. The API used for this project is the Visual Crossing Weather Data API which grabs historical and weather forecast data and can be found here: https://www.visualcrossing.com/weather-api. 

The script runs the weather forecast for a location (US ZIP code) for the current day and the next 14 days.  You can input the zip code and then how many days you want the forecast for (max 15) and it will show you various information about the weather for the specified number of days.

## Commands:
To build a docker image:

> docker build -t forecast:1.0 .

To run the code:

> docker run -e API_KEY= {api key} forecast:1.0 {zip code} {number of days}

Example:

> docker run -e API_KEY= {api key} forecast:1.0 12345 10
