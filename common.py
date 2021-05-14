import time

def scrollDownToBottom(browser, elem, window=True):
    last_height = browser.execute_script(
        "return "+elem+".scrollHeight")  # Get first scroll height
    browser.execute_script(elem+".scrollTo(0,"+str(last_height)+");")
    while True:
        # Scroll down to bottom
        if window:
            browser.execute_script("window.scrollTo(0,"+str(last_height)+");")
        else:
            browser.execute_script(elem+".scrollTo(0,"+str(last_height)+");")

        # Wait to load
        time.sleep(1.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return "+elem+".scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
