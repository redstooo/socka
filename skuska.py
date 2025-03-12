import requests
#
# root_url = "http://127.0.0.1:5000/"
#
# def get_something(name):
#     url = f"{root_url}{name}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         something_data = response.json()
#         return something_data
#     else:
#         print(f"something went wrong... {response.status_code}")
#
#
#
# something_name = "chemical"
# something_info = get_something(something_name)
# id = 1
#
# if something_info:
#     print(something_info["Chemicals..."][id - 1]["name"])



# PRE JEDNU CHEMIKALIU VSETKY REAKCIE(TREBA ESTE PRIDAT FOR LOOP ABY SA X(CHEMIKALIE) MENILI
# (MOZU BYT AJ DUPLIKATY BO NEDA IBA TU CHEMIKALIU ALE ZLUCENINY KDE SA NACHADZA TA CHEMIKALIA))

#
# for x in range(1, 35):
#     y = 0
#     print("-"*40)
#     while True:
#         response = requests.get(f"https://chemequations.com/api/search-reactions-by-compound-ids?reactantIds={x}&productIds=&offset={y}")
#         data = response.json()
#         if data["resultCount"] < y:
#             break
#         for chemikalia in data["searchResults"]:
#             nieco = chemikalia["equationStr"]
#             chemikalie, reakcie = nieco.split("=")
#             if chemikalie.count("+") == 1:
#                 prva, druha = chemikalie.split("+")
#                 print(f"1. chemikalia {prva} | 2. chemikalia {druha} | reackia {reakcie}")
#         y += 10

#
#
# def post_req(name):
#     data = requests.post("http://127.0.0.1:5000/chemical", json={
#         "name": name.strip()
#     })
#     if data.status_code == 201:
#         print(f"{name} pridané")
#     else:
#         print(data.status_code)
#
# def post_req_reakcie(name, one, two):
#     data = requests.post("http://127.0.0.1:5000/reaction", json={
#         "name": name.strip(),
#         "reactant_one_name": one.strip(),
#         "reactant_two_name": two.strip()
#     })
#
#     if data.status_code == 201:
#         print(f"{name} pridané")
#     else:
#         print(data.status_code)
#
# def pridavanie(vec, rozsah1, rozshah2):
#     for x in range(rozsah1, rozshah2):
#         y = 0
#         print("-"*40)
#         response = requests.get(f"https://chemequations.com/api/search-reactions-by-compound-ids?reactantIds={x}&productIds=&offset={y}")
#         data = response.json()
#         for chemikalia in data["searchResults"]:
#             nieco = chemikalia["equationStr"]
#             chemikalie, reakcie = nieco.split("=")
#             if chemikalie.count("+") == 1:
#                 prva, druha = chemikalie.split("+")
#                 if vec == "chemikalia":
#                     post_req(prva)
#                     post_req(druha)
#                 elif vec == "reakcia":
#                     post_req_reakcie(reakcie, prva, druha)
#
# pridavanie("chemikalia", 21, 40)

url = "http://127.0.0.1:5000/reaction"

reakcie = [
    {
        "name": "CO2 + H2O",
        "reactant_one_name": "CO2",
        "reactant_two_name": "H2O"
    },
    {
        "name": "CH4 + O2",
        "reactant_one_name": "CH4",
        "reactant_two_name": "O2"
    },
    {
        "name": "H2 + O2",
        "reactant_one_name": "H2",
        "reactant_two_name": "O2"
    },
    {
        "name": "HCl + NaOH",
        "reactant_one_name": "HCl",
        "reactant_two_name": "NaOH"
    },
    {
        "name": "C2H5OH + O2",
        "reactant_one_name": "C2H5OH",
        "reactant_two_name": "O2"
    },
    {
        "name": "H2O2 + O2",
        "reactant_one_name": "H2O2",
        "reactant_two_name": "O2"
    },
    {
        "name": "NH3 + HCl",
        "reactant_one_name": "NH3",
        "reactant_two_name": "HCl"
    },
    {
        "name": "CaO + CO2",
        "reactant_one_name": "CaO",
        "reactant_two_name": "CO2"
    },
    {
        "name": "Na + H2O",
        "reactant_one_name": "Na",
        "reactant_two_name": "H2O"
    },
    {
        "name": "C6H6 + O2",
        "reactant_one_name": "C6H6",
        "reactant_two_name": "O2"
    },
    {
        "name": "SO3 + H2O",
        "reactant_one_name": "SO3",
        "reactant_two_name": "H2O"
    },
    {
        "name": "CaCO3 + Heat",
        "reactant_one_name": "CaCO3",
        "reactant_two_name": "Heat"
    },
    {
        "name": "H3PO4 + NaOH",
        "reactant_one_name": "H3PO4",
        "reactant_two_name": "NaOH"
    },
    {
        "name": "CHCl3 + NaOH",
        "reactant_one_name": "CHCl3",
        "reactant_two_name": "NaOH"
    },
    {
        "name": "CH2O + O2",
        "reactant_one_name": "CH2O",
        "reactant_two_name": "O2"
    },
    {
        "name": "Na + Cl2",
        "reactant_one_name": "Na",
        "reactant_two_name": "Cl2"
    },
    {
        "name": "C6H6 + CH3Cl",
        "reactant_one_name": "C6H6",
        "reactant_two_name": "CH3Cl"
    },
    {
        "name": "HNO3 + NaOH",
        "reactant_one_name": "HNO3",
        "reactant_two_name": "NaOH"
    },
    {
        "name": "C3H6O + O2",
        "reactant_one_name": "C3H6O",
        "reactant_two_name": "O2"
    },
    {
        "name": "C7H8 + O2",
        "reactant_one_name": "C7H8",
        "reactant_two_name": "O2"
    }
]

for reakcia in reakcie:
    print(reakcia)
    data = requests.post(url, json=reakcia)

    if data.status_code == 201:
        print(reakcia['name'])



