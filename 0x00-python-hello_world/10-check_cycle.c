#include "lists.h"

/**
 * check_cycle - A function in C that checks if a singly
 * linked list has a cycle in it
 * @list: A pointer to the head node of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *curr = NULL, *nxt = NULL;

	curr = list;
	nxt = list;

	while (list != NULL && curr != NULL && nxt != NULL && curr->next != NULL && nxt->next != NULL)
	{
		curr = curr->next;
		nxt = nxt->next->next;

		if (curr == NULL || nxt == NULL)
			return (0);
		if (nxt == curr)
			return (1);
	}
	return (0);
}
