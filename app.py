import json
import logger
import traceback
import nmbot


if __name__ == "__main__":
    with open('headers.json', 'r') as file:
        headers = json.load(file)

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    stats = {
        'loop_count': 0,
        'arena_battles': 0,
        'world_successes': 0,
        'world_losses': 0,
        'item_successes': 0
    }

    logger = logger.Logger()
    manager = nmbot.NMBot(headers, cookies, stats, logger)

    try:
        manager.execute()
    except nmbot.NoSuchWindowException:
        logger.log('\n\n\n\n\n\n')
        logger.log('program exited due to window being closed')
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