from packaging import version

def test_numpy():
    import numpy
    print(numpy.__version__)

    
def test_scipy():
    import scipy
    print(scipy.__version__)
    ## on 10/28/2020 Devin discovered that CMSE201 needs version 1.5 or grater
    assert(version.parse("1.5.2") > version.parse(scipy.__version__))

def test_matplotlib():
    import matplotlib
    print(matplotlib.__version__)

def test_sympy():
    import sympy
    print(sympy.__version__)

def test_skimage():
    import skimage 
    print(skimage.__version__)

# def test_scikit-learn:
#     import scikit-learn
#     print(sscikit.__version__)
