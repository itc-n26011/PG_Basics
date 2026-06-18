text = "aldous Huxley was born in 1894."
ls = text.split(" ")
print(ls[0].capitalize() + " " + " ".join([word for word in ls[1:]]))
