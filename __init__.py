import agent
import time
import environment
import nodriver as uc

if __name__ == "__main__":
    e = environment.Environment()
    e.start_browser()
    a = agent.Agent()
    r = e.response("*") # Esto es un array de pixeles
    while True:
        v = a.compute(r) # Por el momento esto sólo está retornando "*"
        if v == "^":
            break
        start = time.time()
        r = e.response(v)
        # Aqui tenemos que hacer 2 clicks para empezar el juego
        # El primero es encima cuando ya cargó la página (revisar cuando hay amarillo en la pantalla)
        # El segundo es cuando ya cargó el juego y en ese punto ya hay que darle a empezar
        print(r[950][540])
        elapsed = time.time() - start
        time.sleep(max(0,1-elapsed))