from os import system

def weby_deploy(key):
    system("cd predeploy && netlify deploy --prod --alias=WEBLYAI_WEBSITE --identity=" + key)