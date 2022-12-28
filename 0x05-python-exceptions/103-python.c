#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	int size;

	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (int i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	int size;

	if (!PyBytes_Check(p))
	{
		printf("Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %d bytes: ", (size > 10) ? 10 : size);
	for (int i = 0; i < ((size > 10) ? 10 : size); i++)
	{
		printf("%02hhx%c", ((unsigned char *)PyBytes_AsString(p))[i], (i + 1 == size || i + 1 == 10) ? '\n' : ' ');
	}
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");
	printf("  value: %.16g\n", PyFloat_AsDouble(p));
}

