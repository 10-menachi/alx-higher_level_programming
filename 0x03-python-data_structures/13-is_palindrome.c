#include "lists.h"

/**
 * is_palindrome - checks if a singly
 * linked list is a palindrome
 *
 * @head: head of yhe list
 *
 * Return: 0 if not palindrome,
 * 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0;
	int values[1024];

	while (current != NULL)
	{
		values[count] = current->n;
		current = current->next;
		count++;
	}

	for (int i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - i - 1])
			return (0);
	}
	return (1);
}
