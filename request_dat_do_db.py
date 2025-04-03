import requests
import time

def udaje_pubchem(reaction):
    prvky = reaction.split(" + ")
    names = []
    smiles = []
    desc = []
    for prvok in prvky:
        try:
            response = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{prvok}/JSON")
            data = response.json()
            for vec in data["PC_Compounds"]:
                for nieco in vec["props"]:
                    if nieco["urn"]["label"] == "IUPAC Name":
                        names.append(nieco["value"]["sval"])
                        break
                for nieco in vec["props"]:
                    if nieco["urn"]["label"] == "SMILES":
                        smiles.append(nieco["value"]["sval"])
                        break
                for niecoo in vec["id"]["id"]:
                    idcko = vec["id"]["id"][niecoo]
                    break
                response2 = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{idcko}/description/JSON")
                data2 = response2.json()
                desc.append(data2["InformationList"]["Information"][1]["Description"])



        except (KeyError, IndexError):
            names.append(" ")
            smiles.append(" ")
            desc.append(" ")
    reactions = [names, smiles, desc]
    return reactions




def pridavanie(rozsah1, rozshah2):
    for x in range(rozsah1, rozshah2):
        response = requests.get(f"https://chemequations.com/api/search-reactions-by-compound-ids?reactantIds={x}&productIds=&offset=0")
        data = response.json()
        for chemikalia in data["searchResults"]:
            nieco = chemikalia["equationStr"]
            chemikalie, reakcie = nieco.split("=")
            if chemikalie.count("+") == 1:
                prva, druha = chemikalie.split("+")
                meno = ""
                smiles = ""
                desc = ""
                udaje = udaje_pubchem(reakcie)
                for asd in udaje[0]:
                    meno += f"{asd}+"

                for asd in udaje[1]:
                    smiles += f"{asd}+"

                for asd in udaje[2]:
                    desc += f"{asd}, "
                meno = meno.replace(" +", "")
                smiles = smiles.replace(" +", "")
                meno.strip()
                smiles.strip()
                meno = meno[:-1]
                smiles = smiles[:-1]
                rea = {
                    "name": meno,
                    "formula": reakcie,
                    "smiles": smiles,
                    "desc": desc,
                    "reactant_one_name": prva.strip(),
                    "reactant_two_name": druha.strip(),
                }

                data = requests.post("http://127.0.0.1:5000/reaction", json=rea)
                if data.status_code == 201:
                    print(f"{meno} pridané")
                else:
                    print(data.status_code)
                # data = requests.post("http://127.0.0.1:5000/chemical", json={"name": prva.strip()})
                # data2 = requests.post("http://127.0.0.1:5000/chemical", json={"name": druha.strip()})
                # if data.status_code == 201:
                #     print(prva)
                # elif data2.status_code == 201:
                #     print(druha)
                # else:
                #     print(data.status_code, data2.status_code)

pridavanie( 1, 30)
