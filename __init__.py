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
        start = time.time()
        time.sleep(2)
        elapsed = time.time() - start
        time.sleep(max(0, 1 - elapsed))
    print("El juego empezó")
    time.sleep(1)
    r = e.response("*")  # Esto es un array de pixeles
    while r is not False:
        v = a.compute(r)  # Por el momento esto sólo está retornando "*"
        r = e.response(v)