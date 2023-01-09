import requests
def main(FOOD):
		url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"
		querystring = {"ingr":FOOD}
		headers = {
			"X-RapidAPI-Key": "28e40c48c8msh1a0277db73794f2p10da08jsn19cae3428389",
			"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		return response.text["totalNutrients"]["CA"]["quantity"]+response.text["totalNutrients"]["CA"]["unit"], response.text["totalNutrients"]["FAT"]["quantity"]+response.text["totalNutrients"]["FAT"]["unit"], response.text["totalNutrients"]["VITD"]["quantity"]+response.text["totalNutrients"]["VITD"]["unit"], response.text["totalNutrients"]["PROCNT"]["quantity"]+response.text["totalNutrients"]["PROCNT"]["unit"], response.text["totalNutrients"]["WATER"]["quantity"]+response.text["totalNutrients"]["WATER"]["unit"], response.text["totalNutrients"]["K"]["quantity"]+response.text["totalNutrients"]["K"]["unit"]

