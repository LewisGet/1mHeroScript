def openBox ():
    if exists("findBoxs.png"):
        boxs = findAll("findBoxs.png")
        
        for box in boxs:
            click(box)


def doneBoxScene():
    click("ok.png")

def checkElseDoneScene():
    if exists("elseDone.png"):
        click("elseDoneOk-1.png")
        sleep(1)
        checkElseDoneScene()

def sellItems():
    click("boxFullYes.png")
    
    if exists("sellItem1.png"):
        items = findAll("sellItem1.png")

        for item in items:
            click(item)

    if exists("sellItem2.png"):
        items = findAll("sellItem2-1.png")

        for item in items:
            click(item)

    #網路延遲準備時間
    sleep(5) 
    click("sellItemsButton.png") 
    sleep(2)
    click("doneSell.png")

    sleep(5)
    #backToReplay
    click(Pattern("backReplay.png").targetOffset(-55,-2))
    sleep(5)
    replayGame()

def replayGame():
    if exists("levelup.png"):
        click("levelup.png")
    
    click("replayGame.png")
    # check box full
    sleep(2)
    if exists("boxFull-1.png"):
        sellItems()
    
    # no life and sleep


def startGame():
    click("startGame.png")
    #sleep(3 * 60 * 5)
    sleep(60)

while 1:
    startGame()
    sleep(5)
    openBox()
    sleep(5)
    doneBoxScene()
    sleep(5)
    checkElseDoneScene()
    sleep(5)
    replayGame()
    sleep(5)