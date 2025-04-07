import urllib.request

def pridavanie_obrazku(meno):
    if meno == "" or meno == " ":
        print("nenašiel sa obrázok")
    else:
        full_path = f"smiles/{meno}.jpg"
        urllib.request.urlretrieve(f"http://hulab.rxnfinder.org/smi2img/{meno}/", full_path)
        print(f"pridané {meno}")
