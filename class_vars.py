# iterating through class variables stolen and modified from https://stackoverflow.com/a/1939279

# NOTE: While it does look like StringVars don't work as they don't display themselves properly, they are completely functional.
# NOTE: If you cast them to a string before they get appended to a list, they show up fine. Problem is you won't be able to call .get()
# NOTE: to retrieve the value. Don't ask me why.
def get_class_vars(obj: object):

    members = [attr for attr in dir(obj())
               if not callable(getattr(obj(), attr)) and not attr.startswith("__")]


    class_variables = []
    for member in members:
        # This works with multiple value types because a list is basically an array of pointers.
        class_variables.append(getattr(obj(), member))


    return class_variables