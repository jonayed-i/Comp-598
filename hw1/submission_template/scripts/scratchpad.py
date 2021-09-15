import re



def isQuestion(content):
    if re.search(r"\?",content):
        return True
    else:
        return False

print(isQuestion("daddygang"))

print(re.search("\?","bryg?"))