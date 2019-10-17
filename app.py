import json
import logger
import keyboard
import threading




if __name__ == "__main__":
    with open('headers.json', 'r') as file:
        headers = json.load(file)

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    logger = logger.Logger()
    manager = NMBot(headers, cookies, logger)

    keyboard.add_hotkey('delete', manager.kill)

    kill_thread = threading.Thread(target=keyboard.wait)
    kill_thread.daemon = True
    kill_thread.start()

    try:
        manager.execute()
    except Exception as e:
        logger.log('\n\n\n\n\n\n')
        logger.log('%s' % e)
        logger.log(traceback.format_exc())

    logger.close()