import agent
import time
import environment

if __name__ == "__main__":

    e = environment.Environment()
    e.start_browser()
    a = agent.Agent()
    game_started = False
    while not game_started:
        captura = e.screenshot()
        game_started = e.start_game(captura)
        time.sleep(0.5)
#     time.sleep(5)
    a.compute(e)