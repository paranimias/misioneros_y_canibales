if __name__ == "__main__":
    # a = Agent()
    # e = Environment(a)
    #
    imagen_transformada = e.send(e.screenshot())
    # print(type(imagen_transformada[1079][950]))
    e.show_picture(imagen_transformada)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()