#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(int argc, char *argv[]) {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python list for testing
    PyObject *list = PyList_New(0);
    PyList_Append(list, PyUnicode_DecodeUTF8("Hello", 5, "strict"));
    PyList_Append(list, PyLong_FromLong(42));
    PyList_Append(list, PyFloat_FromDouble(3.14));

    // Call the function to print list info
    print_python_list_info(list);

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
