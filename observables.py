from reactivex import of, operators as op

of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
).subscribe(lambda value: print("Received {0}".format(value)))