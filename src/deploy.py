from os import sys

def weby_deploy(key):
    sys("cd predeploy && netlify deploy --prod --alias=WEBLYAI_WEBSITE --identity=" + key)