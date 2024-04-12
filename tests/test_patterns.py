from vim_matlab import python_vim_utils


def strip_comments(line):
    pattern = python_vim_utils.PythonVimUtils.comment_pattern
    return pattern.sub(r"\1", line).strip()

def test_printout():
    print("test_comment_patterns")
    # print("test escape formatting \"%s\"")
    # print("python formatting escapes {}%{}".format(1,2))
    print("print strip_comments")
    print("hello" + ": " + strip_comments("hello"))
    print("hello %" + ": " + strip_comments("hello %"))
    print("hello %%" + ": " + strip_comments("hello %%"))
    print("disp('%')" + ": " + strip_comments("disp('%') % "))
    print("disp(\"%\")" + ": " + strip_comments("disp(\"%\") % "))
    print("disp('')" + ": " + strip_comments("disp('')% "))
    print("disp('')" + ": " + strip_comments("disp('') % "))
    print("disp('')" + ": " + strip_comments("disp('') %%"))
    print("disp('%');disp('%')" + ": " +
          strip_comments("disp('%');disp('%')%disp('')"))
    print("end of printout debug")

def test_regex_pattern():
    print("print regex pattern")
    pattern = python_vim_utils.PythonVimUtils.comment_pattern
    #return pattern.sub(r"\1", line).strip()
    print(pattern)


# @hey, a bug with escaping \ and "
def test_comment_pattern():
    # bunch of asserts - these should all pass!
    assert "hello" == strip_comments("hello")
    assert "hello" == strip_comments("hello %")
    assert "hello" == strip_comments("hello %%")
    assert "disp('%')" == strip_comments("disp('%') % ")
    assert "disp('')" == strip_comments("disp('')")
    assert "disp('%')" == strip_comments("disp('%')")
    assert "disp(\"%\")" == strip_comments("disp(\"%\")")
    assert "disp('')" == strip_comments("disp('')% ")
    assert "disp('')" == strip_comments("disp('') % ")
    assert "disp('')" == strip_comments("disp('') %%")
    assert "disp('%');disp('%')" == strip_comments(
        "disp('%');disp('%')%disp('')")
    assert "A = sqrtm(B) \\ C.';" == strip_comments(
        "A = sqrtm(B) \\ C.'; % foo")
    assert "disp('100%');A = sqrtm(B) \\ C.';" == strip_comments(
        "disp('100%');A = sqrtm(B) \\ C.';% foo")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% '")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% ''")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% '''")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% '.''")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% ' '")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% ' ' %")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% ' %' ")
    assert "disp('%');C.'" == strip_comments("disp('%');C.'% ' %' %")
    assert "disp('% ''');C.';" == strip_comments("disp('% ''');C.'; % ' %' %")
    assert "disp('% .''');C.';" == strip_comments(
        "disp('% .''');C.'; % ' %' %")
    # assert "fprintf("%s\\n\","test parse");" == strip_comments("disp('% .''');C.'; % ' %' %")
