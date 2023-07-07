file_to_scrap = ""
f = ""


def extracter(type)->str:
    start = f.find("```" + type) + len(type) + 3
    end = f.find("```", start) - 1
    code = f[start:end]
    return code