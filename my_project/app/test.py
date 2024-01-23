AN = 3
def filter(*args, **kwargs):
    print(args)
    print(kwargs)
    if 'an__lt' in kwargs:
        print("mai mic")
        return AN < kwargs['an__lt']
    if 'an__gt' in kwargs:
        print("mai mare")
        return AN > kwargs['an__gt']


print(filter(an__lt=2))