

## two types of arguements , keyword and non-keyword

## keyword refers to **kwargs


def identity(**container):
    for key,value in container.items():
        print(f"{key} : {value}")



identity(name="amit",age=21,city="mumbai")

## **kwargs allows us to add any number of arguements and values

## allows to provide variable name along with its value as we pass it in function

## args packs positional arguements into a tuple

## kwargs packs keywords agruments into a dictionary

