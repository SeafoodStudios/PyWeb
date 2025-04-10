import regex as re
import httpcore

response = httpcore.request("GET", "https://www.example.com/")
print(response)
txt = "The rain in Spain"
x = re.findall("a", txt)
print(x)
