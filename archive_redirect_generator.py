import os
import json


def streamRedirectGenerate(redirectTemplate):
    i = 1
    streamGenerating = True
    while streamGenerating:
        streamFileName = f'../video-archive/archive/stream/{i:04}.json'
        if os.path.isfile(streamFileName):
            with open(streamFileName, 'r', encoding="UTF-8", newline="\n") as streamFile:
                streamJsonString = streamFile.read()
                streamJsonObject = json.loads(streamJsonString)
                streamOutputHTML = redirectTemplate.format(url=f'https://www.youtube.com/playlist?list={streamJsonObject["playlistID"]}')
                streamOutputHTMLFilename = f'playlist/stream/{i}/index.html'
                os.makedirs(os.path.dirname(streamOutputHTMLFilename), exist_ok=True)
                with open(streamOutputHTMLFilename, 'w', encoding="UTF-8", newline="\n") as streamOutputHTMLFile:
                    streamOutputHTMLFile.write(streamOutputHTML)
        else:
            streamGenerating = False

        i += 1
    pass


def categoryRedirectGenerate(redirectTemplate):
    categoryBaseDir = '../video-archive/archive/category'
    categoryDirs = os.listdir(categoryBaseDir)
    for categoryDir in categoryDirs:
        subCategoryFiles = os.listdir(f'{categoryBaseDir}/{categoryDir}')
        for subCategoryFile in subCategoryFiles:
            if(os.path.isfile(f'{categoryBaseDir}/{categoryDir}/{subCategoryFile}') and subCategoryFile != "_category.json" and subCategoryFile.endswith(".json")):
                subCategoryFile = subCategoryFile.replace(".json", "")
                with open(f'{categoryBaseDir}/{categoryDir}/{subCategoryFile}.json', 'r', encoding="UTF-8", newline="\n") as gameFile:
                    categoryJsonString = gameFile.read()
                    categoryJsonObject = json.loads(categoryJsonString)
                    categoryOutputHTML = redirectTemplate.format(url=f'https://www.youtube.com/playlist?list={categoryJsonObject["playlistID"]}')
                    categoryOutputHTMLFilename = f'playlist/category/{categoryDir}/{subCategoryFile}/index.html'
                    os.makedirs(os.path.dirname(categoryOutputHTMLFilename), exist_ok=True)
                    with open(categoryOutputHTMLFilename, 'w', encoding="UTF-8", newline="\n") as categoryOutputHTMLFile:
                        categoryOutputHTMLFile.write(categoryOutputHTML)
    pass


if __name__ == '__main__':
    redirectTemplate = ""
    with open('redirect_template.html', 'r', encoding="UTF-8", newline="\n") as templateFile:
        redirectTemplate = templateFile.read()

    streamRedirectGenerate(redirectTemplate)
    categoryRedirectGenerate(redirectTemplate)

    pass
