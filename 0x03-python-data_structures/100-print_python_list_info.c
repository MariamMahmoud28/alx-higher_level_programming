#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, alloc;
    PyObject *item;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (Py_ssize_t i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(int argc, char *argv[]) {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python list and call the function
    PyObject *list = Py_BuildValue("[s, i, i, s]", "Hello", 42, 10, "World");
    print_python_list_info(list);

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
