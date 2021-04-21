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
        \tdouble boil = {(w[i]["boil"], -1.) [w[i]["boil"] == None]};\n\
        \tstring boil_s = "{str(w[i]["boil"]) + " K"}";\n\
        \tdouble melt = {(w[i]["melt"], -1.) [w[i]["melt"] == None]};\n\
        \tstring melt_s = "{str(w[i]["melt"]) + " K"}";\n\
        \tdouble molar_hc = {(w[i]["molar_heat"], -1.) [w[i]["molar_heat"] == None]};\n\
        \tstring molar_hc_s = "{str(w[i]["molar_heat"]) + " J/(K*mol)"}";\n\
        \tint atomic_number = {w[i]["number"]};\n\
        \tstring symbol = "{w[i]["symbol"]}";\n\
        \tint valence_e = {(-1, w[i]["xpos"]%10) [w[i]["xpos"] < 3 or w[i]["xpos"] > 12] };\n\n\
        \tstring getName(){"{"}return name;{"};"}\n\
        \tdouble getAtomicMass(){"{"}return atomic_mass;{"};"}\n\
        \tdouble getBoilingTemp(){"{"}return boil;{"};"}\n\
        \tdouble getMeltingTemp(){"{"}return melt;{"};"}\n\
        \tdouble getMolarHeatCapacity(){"{"}return molar_hc;{"};"}\n\
        \tint getAtomicNumber(){"{"}return atomic_number;{"};"}\n\
        \tstring getSymbol(){"{"}return symbol;{"};"}\n\
        \tint getValenceNumber(){"{"}return valence_e;{"};"}\n\n\
        string toString(){"{"}return name + " " + symbol + "\\n\\t" + "atomic mass: " + std::to_string(atomic_mass) + "\\n\\t" + "Boiling Point: " + boil_s + "\\n\\t" + "Melting Point " + melt_s + "\\n\\t" + "Molar Heat Capacity: " + molar_hc_s + "\\n\\t" + "atomic number: " + std::to_string(atomic_number) + "\\n\\t" + "valence: " + std::to_string(valence_e) + "\\n\\t";{"};"}\n\
        {"};"}\n\n')
#print(w[w["order"][0]]["xpos"])