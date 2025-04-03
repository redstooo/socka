# import requests
# import time
#
#
#
# # PRE JEDNU CHEMIKALIU VSETKY REAKCIE(TREBA ESTE PRIDAT FOR LOOP ABY SA X(CHEMIKALIE) MENILI
# # (MOZU BYT AJ DUPLIKATY BO NEDA IBA TU CHEMIKALIU ALE ZLUCENINY KDE SA NACHADZA TA CHEMIKALIA))
#
# #
# # for x in range(1, 35):
# #     y = 0
# #     print("-"*40)
# #     while True:
# #         response = requests.get(f"https://chemequations.com/api/search-reactions-by-compound-ids?reactantIds={x}&productIds=&offset={y}")
# #         data = response.json()
# #         if data["resultCount"] < y:
# #             break
# #         for chemikalia in data["searchResults"]:
# #             nieco = chemikalia["equationStr"]
# #             chemikalie, reakcie = nieco.split("=")
# #             if chemikalie.count("+") == 1:
# #                 prva, druha = chemikalie.split("+")
# #                 print(f"1. chemikalia {prva} | 2. chemikalia {druha} | reackia {reakcie}")
# #         y += 10
#
# #
# #
# # def post_req(name):
# #     data = requests.post("http://127.0.0.1:5000/chemical", json={
# #         "name": name.strip()+;
# #     })
# #     if data.status_code == 201:
# #         print(f"{name} pridané")
# #     else:
# #         print(data.status_code)
# #
# # def post_req_reakcie(name, one, two):
# #     data = requests.post("http://127.0.0.1:5000/reaction", json={
# #         "name": name.strip(),
# #         "reactant_one_name": one.strip(),
# #         "reactant_two_name": two.strip()
# #     })
# #
# #     if data.status_code == 201:
# #         print(f"{name} pridané")
# #     else:
# #         print(data.status_code)
# #
# # def pridavanie(vec, rozsah1, rozshah2):
# #     for x in range(rozsah1, rozshah2):
# #         y = 0
# #         print("-"*40)
# #         response = requests.get(f"https://chemequations.com/api/search-reactions-by-compound-ids?reactantIds={x}&productIds=&offset={y}")
# #         data = response.json()
# #         for chemikalia in data["searchResults"]:
# #             nieco = chemikalia["equationStr"]
# #             chemikalie, reakcie = nieco.split("=")
# #             if chemikalie.count("+") == 1:
# #                 prva, druha = chemikalie.split("+")
# #                 if vec == "chemikalia":
# #                     post_req(prva)
# #                     post_req(druha)
# #                 elif vec == "reakcia":
# #                     post_req_reakcie(reakcie, prva, druha)
# #
# # pridavanie("chemikalia", 21, 40)
#
# base = "http://127.0.0.1:5000"
#
# chemikalie = [
#     { "name": "C2H5OH", "element": "Etanol", "state": "KVAPALINA", "desc": "Zložka alkoholických nápojov" },
#     { "name": "CH4", "element": "Metán", "state": "PLYN", "desc": "Hlavná zložka zemného plynu" },
#     { "name": "CO2", "element": "Oxid uhličitý", "state": "PLYN", "desc": "Rastliny ho využívajú" },
#     { "name": "H2SO4", "element": "Kyselina sírová", "state": "KVAPALINA", "desc": "Silná priemyselná kyselina" },
#     { "name": "NH3", "element": "Amoniak", "state": "PLYN", "desc": "Používa sa v hnojivách" },
#     { "name": "NaCl", "element": "Chlorid sodný", "state": "PEVNÁ LÁTKA", "desc": "Bežná kuchynská soľ" },
#     { "name": "CaCO3", "element": "Uhličitan vápenatý", "state": "PEVNÁ LÁTKA", "desc": "Hlavná zložka vápenca" },
#     { "name": "C3H6O", "element": "Acetón", "state": "KVAPALINA", "desc": "Odstraňovač laku na nechty" },
#     { "name": "C6H12O6", "element": "Glukóza", "state": "PEVNÁ LÁTKA", "desc": "Primárny zdroj energie" },
#     { "name": "HCl", "element": "Kyselina chlorovodíková", "state": "PLYN", "desc": "Žalúdočná tráviaca kyselina" },
#     { "name": "C6H6", "element": "Benzén", "state": "KVAPALINA", "desc": "Priemyselné rozpúšťadlo" },
#     { "name": "O2", "element": "Kyslík", "state": "PLYN", "desc": "Nezbytný na dýchanie" },
#     { "name": "H2O2", "element": "Peroxid vodíka", "state": "KVAPALINA", "desc": "Bežný dezinfekčný prostriedok" },
#     { "name": "NaOH", "element": "Hydroxid sodný", "state": "PEVNÁ LÁTKA", "desc": "Silný čistiaci prostriedok" },
#     { "name": "H3PO4", "element": "Kyselina fosforečná", "state": "KVAPALINA", "desc": "Používa sa v nápojoch" },
#     { "name": "CHCl3", "element": "Chloroform", "state": "KVAPALINA", "desc": "Historické anestetikum" },
#     { "name": "HNO3", "element": "Kyselina dusičná", "state": "KVAPALINA", "desc": "Výbušniny a hnojivá" },
#     { "name": "CH2O", "element": "Formaldehyd", "state": "PLYN", "desc": "Konzervačný prostriedok" },
#     { "name": "C7H8", "element": "Toluén", "state": "KVAPALINA", "desc": "Používa sa v riedidlách" }
# ]
#
#
# reakcie = [
#     { "name": "H2 + O2", "element": "Tvorba vody", "state": "PLYN", "desc": "Reakcia vodíka s kyslíkom", "reactant_one_name": "H2", "reactant_two_name": "O2" },
#     { "name": "CH4 + O2", "element": "Spaľovanie metánu", "state": "PLYN", "desc": "Vznik CO2 a vody", "reactant_one_name": "CH4", "reactant_two_name": "O2" },
#     { "name": "C2H5OH + O2", "element": "Spaľovanie etanolu", "state": "KVAPALINA", "desc": "Vznik CO2 a vody", "reactant_one_name": "C2H5OH", "reactant_two_name": "O2" },
#     { "name": "CaCO3 + O2", "element": "Rozklad vápenca", "state": "PEVNÁ LÁTKA", "desc": "Vznik oxidu vápenatého", "reactant_one_name": "CaCO3", "reactant_two_name": "O2" },
#     { "name": "NaCl + H2O", "element": "Elektrolýza solanky", "state": "KVAPALINA", "desc": "Tvorba chlóru a vodíka", "reactant_one_name": "NaCl", "reactant_two_name": "H2O" },
#     { "name": "H2SO4 + NaOH", "element": "Neutralizácia kyseliny", "state": "KVAPALINA", "desc": "Vznik síranu sodného", "reactant_one_name": "H2SO4", "reactant_two_name": "NaOH" },
#     { "name": "NH3 + HCl", "element": "Tvorba chloridu amónneho", "state": "PLYN", "desc": "Vznik bieleho dymu", "reactant_one_name": "NH3", "reactant_two_name": "HCl" },
#     { "name": "C6H12O6 + O2", "element": "Dýchanie buniek", "state": "KVAPALINA", "desc": "Produkuje energiu a CO2", "reactant_one_name": "C6H12O6", "reactant_two_name": "O2" },
#     { "name": "HCl + Zn", "element": "Reakcia kyseliny s kovom", "state": "PLYN", "desc": "Vzniká vodík", "reactant_one_name": "HCl", "reactant_two_name": "Zn" },
#     { "name": "Fe + O2", "element": "Hrdzavenie železa", "state": "PEVNÁ LÁTKA", "desc": "Tvorba oxidu železitého", "reactant_one_name": "Fe", "reactant_two_name": "O2" },
#     { "name": "C6H6 + O2", "element": "Spaľovanie benzénu", "state": "KVAPALINA", "desc": "Vznik CO2 a vody", "reactant_one_name": "C6H6", "reactant_two_name": "O2" },
#     { "name": "H2O2 + O2", "element": "Rozklad peroxidu vodíka", "state": "KVAPALINA", "desc": "Vznik kyslíka", "reactant_one_name": "H2O2", "reactant_two_name": "O2" },
#     { "name": "NaOH + CO2", "element": "Tvorba uhličitanu sodného", "state": "PEVNÁ LÁTKA", "desc": "Absorbuje CO2", "reactant_one_name": "NaOH", "reactant_two_name": "CO2" },
#     { "name": "H3PO4 + Ca(OH)2", "element": "Tvorba fosforečnanu vápenatého", "state": "PEVNÁ LÁTKA", "desc": "Používa sa v hnojivách", "reactant_one_name": "H3PO4", "reactant_two_name": "Ca(OH)2" },
#     { "name": "CHCl3 + O2", "element": "Oxidácia chloroformu", "state": "KVAPALINA", "desc": "Vznik fosgénu", "reactant_one_name": "CHCl3", "reactant_two_name": "O2" },
#     { "name": "HNO3 + Cu", "element": "Reakcia medi s kyselinou", "state": "KVAPALINA", "desc": "Tvorba dusičnanu meďnatého", "reactant_one_name": "HNO3", "reactant_two_name": "Cu" },
#     { "name": "CH2O + O2", "element": "Oxidácia formaldehydu", "state": "PLYN", "desc": "Vznik kyseliny mravčej", "reactant_one_name": "CH2O", "reactant_two_name": "O2" },
#     { "name": "C7H8 + O2", "element": "Spaľovanie toluénu", "state": "KVAPALINA", "desc": "Tvorba CO2 a vody", "reactant_one_name": "C7H8", "reactant_two_name": "O2" },
#     { "name": "CO2 + H2O", "element": "Fotosyntéza", "state": "KVAPALINA", "desc": "Tvorba glukózy a kyslíka", "reactant_one_name": "CO2", "reactant_two_name": "H2O" }
# ]
#
#
#
# # for chemikalia in chemikalie:
# #     time.sleep(0.5)
# #     data = requests.post(f"{base}/chemical", json=chemikalia)
# #
# #     if data.status_code == 201:
# #         print(chemikalia["name"])
#
# for reakcia in reakcie:
#     time.sleep(0.5)
#     data = requests.post(f"{base}/reaction", json=reakcia)
#
#     if data.status_code == 201:
#         print(reakcia["name"])
#
#
#


a = "dibromoiron +"
a = a.replace(" +", " ")

print(a)
