"""
parsing a name with this structure

First [Middle] Last [,Jr.]

Possible names:

"Roy Wood "

"Roy Wood, Jr."

"Roy Wood,Jr."

"Roy  H. Wood "

" Roy Herbert Wood, Jr"
"""




def parse_name(full_name):
    most = full_name.split(",")

    try:
        jr = most[1].strip()
        jr = jr.rstrip(".")
    except IndexError:
        jr = ""
    most = most[0].split()
    print(most)
    if len(most) == 3:
        first, middle, last = most
        middle = middle.rstrip(".")
    else:
        first, last = most
        middle = ""
    first, middle, last, jr = (s.capitalize() for s in (first, middle, last, jr))
    return first, middle, last, jr


def test_full():
    assert ( parse_name(" Roy Herbert Wood, Jr") ==
             ("Roy", "Herbert", "Wood", "Jr"))

def test_first_last():
    assert ( parse_name(" Roy Wood") ==
             ("Roy", "", "Wood", ""))

def test_last_middle():
    assert ( parse_name(" Roy Herbert Wood") ==
             ("Roy", "Herbert", "Wood", ""))

def test_first_last_mi():
    assert ( parse_name(" Roy H. Wood") ==
             ("Roy", "H", "Wood", ""))

def test_first_last_jr():
    assert ( parse_name("Roy Wood,Jr.") ==
             ("Roy", "", "Wood", "Jr"))

def test_first_last_jr2():
    assert ( parse_name("Roy Wood, Jr.") ==
             ("Roy", "", "Wood", "Jr"))

def test_caps():
    assert ( parse_name("ROy wood, Jr.") ==
             ("Roy", "", "Wood", "Jr"))
