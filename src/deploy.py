from os import system
from os import path

def weby_deploy(linkId):
    system("cd predeploy && netlify login && netlify link " + linkId + " && netlify deploy --dir=" + path.join(".") + " --prod --alias=WEBLYAI_WEBSITE")