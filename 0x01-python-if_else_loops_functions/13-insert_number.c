#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - A function in C that inserts a number
 * into a sorted singly linked list
 * @head: A pointer to the first node of the list
 * @number: The number to be inserted
 * Return: Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = NULL, *temp = NULL;
	
	if (!head)
		return NULL;
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
	{
		free(temp);
		return NULL;
	}
	temp->n = number;
	temp->next = NULL;
	if (!*head)
	{
		*head = temp;
		return (temp);
	}
	curr = *head;
	while (curr)
	{
		if (curr->n <= number)
		{
			if (curr->next == NULL || curr->next->n >= number)
			{
				temp->next = curr->next;
				curr->next = temp;
				break;
			}
		}
		else if (curr->n >= number)
		{
			temp->next = *head;
			*head = temp;
			break;
		}

		curr = curr->next;
	}
	return (temp);
}
