import os
import json


def streamRedirectGenerate(redirectTemplate):
    i = 1
    streamGenerating = True
    while streamGenerating:
        streamFileName = f'../video-archive/json/streams/{i:04}.json'
        if os.path.isfile(streamFileName):
            with open(streamFileName, 'r', encoding="UTF-8", newline="\n") as streamFile:
                streamJsonString = streamFile.read()
                streamJsonObject = json.loads(streamJsonString)
                streamOutputHTML = redirectTemplate.format(url=f'https://www.youtube.com/playlist?list={streamJsonObject["playlist"]}')
                streamOutputHTMLFilename = f'playlist/stream/{i}/index.html'
                os.makedirs(os.path.dirname(streamOutputHTMLFilename), exist_ok=True)
                with open(streamOutputHTMLFilename, 'w', encoding="UTF-8", newline="\n") as streamOutputHTMLFile:
                    streamOutputHTMLFile.write(streamOutputHTML)
        else:
            streamGenerating = False

        i += 1
    pass


def gameRedirectGenerate(redirectTemplate):
    gameBaseDir = '../video-archive/json/games'
    gameDirs = os.listdir(gameBaseDir)
    for gameDir in gameDirs:
        categoryDirs = os.listdir(f'{gameBaseDir}/{gameDir}')
        for categoryDir in categoryDirs:
            if(os.path.isdir(f'{gameBaseDir}/{gameDir}/{categoryDir}')):
                with open(f'{gameBaseDir}/{gameDir}/{categoryDir}/_subID.json', 'r', encoding="UTF-8", newline="\n") as gameFile:
                    gameJsonString = gameFile.read()
                    gameJsonObject = json.loads(gameJsonString)
                    gameOutputHTML = redirectTemplate.format(url=f'https://www.youtube.com/playlist?list={gameJsonObject["playlist"]}')
                    gameOutputHTMLFilename = f'playlist/game/{gameDir}/{categoryDir}/index.html'
                    os.makedirs(os.path.dirname(gameOutputHTMLFilename), exist_ok=True)
                    with open(gameOutputHTMLFilename, 'w', encoding="UTF-8", newline="\n") as gameOutputHTMLFile:
                        gameOutputHTMLFile.write(gameOutputHTML)
    pass


if __name__ == '__main__':
    redirectTemplate = ""
    with open('redirect_template.html', 'r', encoding="UTF-8", newline="\n") as templateFile:
        redirectTemplate = templateFile.read()

    streamRedirectGenerate(redirectTemplate)
    gameRedirectGenerate(redirectTemplate)

    pass
