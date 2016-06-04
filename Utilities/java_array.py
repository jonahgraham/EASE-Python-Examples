from py4j.java_gateway import JavaClass


def java_array(l, java_type=None, fqn=None):
    '''
    Convert list l to a Java array of element_type.

    By default Py4J creates java ArrayList out of a Python list
    when calling Java. By wrapping a Python list in java_array()
    it "casts" it to being a Java native array with the element
    type as defined by java_type or fqn:

    - if java_type and fqn are None, java.lang.Object is used.
    - if java_type is not None, it should be a py4j.java_gateway.JavaClass
      of the instance type desired
    - if java_type is None, fqn is the Fully Qualified Name for the Java
      class to use as the instance type. For primitives, use the
      primitive name (e.g. "double")
    '''
    # # TODO type inference?
    if java_type is None:
        if fqn is None:
            java_type = java.lang.Object
        else:
            java_type = JavaClass(fqn, gateway)
    new_array = gateway.new_array(java_type, len(l))
    for i, entry in enumerate(l):
        new_array[i] = entry
    return new_array
