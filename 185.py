api_request = requests.get(" https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=cfff1092c3ed447298e75c3d2222cc74")
api_output_json = json.loads(api_request.content)
open_bbc_page["article"][0]["title"]