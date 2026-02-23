import sys
import agent
import time
import environment

if __name__ == "__main__":
    mode = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    e = environment.Environment()
    a = agent.Agent()

    if mode == 1:
        e.start_browser()
        game_started = False
        while not game_started:
            captura = e.screenshot()
            game_started = e.start_game(captura)
            time.sleep(0.5)
        a.compute(e)
    elif mode == 0:
        time.sleep(5)
        a.compute(e)
