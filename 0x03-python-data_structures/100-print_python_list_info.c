#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about
 * python lists
 *
 * @p: pyobject
 */


void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated;
	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	const char *type;
	
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

