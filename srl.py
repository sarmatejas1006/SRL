import unirest as unirest
import json

data_file = open("input.txt", "r")
data = data_file.read()

response = unirest.post("https://pragmacraft-semantic-role-labeling-v1.p.mashape.com/srl",
                        headers={
                          "X-Mashape-Key": "Z7NAfUjMwgmshq9OpSlDMR5Uw37Pp1S0OOmjsnLfj0mUrwPtFR",
                          "Content-Type": "application/x-www-form-urlencoded",
                          "Accept": "application/json"
                        },
                        params={
                          "text": data}
                        )
returned_val = response.body
text = returned_val["inputText"]
with open('output.json', 'w') as outfile:
    json.dump(returned_val, outfile)
