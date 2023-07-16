#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints python strings
 * @p: given string
 *
 */

void print_python_string(PyObject *p)
{
	PyUnicodeObject *unicode;
	PyASCIIObject *ascii;
	Py_ssize_t length;
	const char *value;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	unicode = (PyUnicodeObject *)p;
	ascii = (PyASCIIObject *)p;
	length = PyUnicode_GET_LENGTH(unicode);
	value = PyUnicode_AsUTF8AndSize(p, NULL);
	printf("  type: %s\n", (ascii->state.ascii ? "compact ascii" :
				"compact unicode object"));
	printf("  length: %ld\n", length);
	printf("  value: %s\n", value);
}
