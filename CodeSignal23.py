def variableName(name):
    print(name[0])
    if sum([0 if str(x).isalnum() or str(x) == '_' else 1 for x in list(str(name))])==0 and not name[0].isdigit():
        return True
    return False


"""
Correct variable names consist only of English letters, digits 
and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

    For name = "var_1__Int", the output should be
    variableName(name) = true;
    For name = "qq-q", the output should be
    variableName(name) = false;
    For name = "2w2", the output should be
    variableName(name) = false.

"""

name = "2w2"
if __name__ == '__main__':
    print(variableName(name))
