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

    stats = {
        'loop_count': 0,
        'arena_battles': 0,
        'world_successes': 0,
        'world_losses': 0,
        'item_successes': 0
    }

    manager = NMBot(headers, cookies, stats, logger)

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

    with open('summary.txt', 'w+') as file:
        file.write('Total Loops:   ' + str(stats['loop_count']) +
                 '\nArena Battles: ' + str(stats['arena_battles']) +
                 '\nWorld Wins:    ' + str(stats['world_successes']) +
                 '\nWorld Losses:  ' + str(stats['world_losses']) +
                 '\nItems Gained:  ' + str(stats['item_successes']))
    logger.close()