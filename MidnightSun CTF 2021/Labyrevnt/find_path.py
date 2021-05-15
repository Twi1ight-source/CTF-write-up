end_path = []
visited_funcs = set ()
def find_end_function(func):
    funcName = func.getName ()

    if funcName in visited_funcs:
        return 0
    else:
        visited_funcs.add (funcName)

    end_path.append (funcName)

    if func.getName () == u'walk_end':
        print ("yes")
        return 1

    calledFuncs = func.getCalledFunctions (monitor)
    calledFuncs.remove (getFunction ("get_input"))

    #  print (len (calledFuncs))

    if len (calledFuncs) == 0:
        end_path.pop ()
        return 0

    for i in calledFuncs:
        if find_end_function (i) == 1:
            return 1

    end_path.pop ()
    visited_funcs.remove (funcName)

    return 0

startFunc = getFunction ("walk_start")
find_end_function (startFunc)
print (end_path)

#  end_path_entries = []
#  for i in end_path:
    #  end_path_entries.append (i.getEntryPoint ())

#  print (end_path_entries)
print (len (end_path))