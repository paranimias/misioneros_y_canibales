import agent
import time
import environment

if __name__ == "__main__":
    e = environment.Environment()
    e.start_browser()
    a = agent.Agent()
    game_started = False
    while not game_started:
        game_started = e.start_game()
        start = time.time()
        time.sleep(2)
        elapsed = time.time() - start
        time.sleep(max(0, 1 - elapsed))
    time.sleep(2)
    r = e.response("*")  # Esto es un array de pixeles
    print(r)
    # while r:
    #     v = a.compute(r)  # Por el momento esto sólo está retornando "*"
    #     r = e.response(v)

