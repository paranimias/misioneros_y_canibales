import agent
import Enviroment


if __name__ == "__main__":
    e = Enviroment()
    a = Agent()
    r = e.response("*")
    while True:
        v = a.compute(r)
        if v == "^"
            break
        r = e.response(v)
