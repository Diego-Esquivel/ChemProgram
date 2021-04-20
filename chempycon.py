import json

f = open('chem.json')

w = json.load(f)
#w = json.loads(w)

e = open('Elements.h', "w")
e.write("#include <string>\n\
using std::string;\n\n")
for i in w["order"] :
    e.write(f'struct {w[i]["name"]} {"{"}\n\
        \tstring name = "{w[i]["name"]}";\n\
        \tdouble atomic_mass = {w[i]["atomic_mass"]};\n\
        \tdouble boil = {w[i]["boil"]};\n\
        \tstring boil_s = "{str(w[i]["boil"]) + " K"}";\n\
        \tdouble melt = {w[i]["melt"]};\n\
        \tstring melt_s = "{str(w[i]["melt"]) + " K"}";\n\
        \tdouble molar_hc = {w[i]["molar_heat"]};\n\
        \tstring molar_hc_s = "{str(w[i]["molar_heat"]) + " K"}";\n\
        \tint atomic_number = {w[i]["number"]};\n\
        \tstring symbol = "{w[i]["symbol"]}";\n\
        \tint valence_e = {(-1, w[i]["xpos"]%10) [w[i]["xpos"] < 3 or w[i]["xpos"] > 12] };\n\
        {"};"}\n\n')
#print(w[w["order"][0]]["xpos"])