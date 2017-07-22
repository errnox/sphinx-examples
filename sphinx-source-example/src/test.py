class Test(object):
    def __init__(self):
        pass

    def do_nothing(self):
        """Does nothing.

        Does nothing, successfully.

        Args:
            none

        Returns:
            True
        """
        print "Doing nothing..."
        return True


    def do_something(self, task):
        """Does something.

        Takes a task and executes it.
        """
        print 'Doing ' + str(task) + '...'
        return True

    def be_lazy(person):
        """Lets a person be lazy

        Takes a person an lets him/her be lazy.
        It reports the person's new status.

        :param person: Person who is going to be lazy
        :type param: str
        :returns: True
        :rtype: boolean
        """
        print str(person) + " is lazy."
        return True

if __name__ == '__main__':
    test = Test()
    test.do_nothing()

