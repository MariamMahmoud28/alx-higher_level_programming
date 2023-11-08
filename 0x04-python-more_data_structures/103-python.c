#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: A PyObject pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: A PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    str = PyBytes_AS_STRING(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    if (size < 10)
        printf("  first %ld bytes: ", size);
    else
        printf("  first 10 bytes: ");

    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%c", str[i], i < size - 1 ? ' ' : '\n');
}
