#include "lists.h"
/**
 * insert_node - inserts node for a sorted linked list
 * @head: head of of the linked list
 * @number: number for the new node to be added
 * Return: address of the new node if the node is added
 *         NULL, if the new node is not successfuly added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *temp = malloc(sizeof(listint_t *));
	listint_t *additional = malloc(sizeof(listint_t *));

	if (additional == NULL)
	{
		return (NULL);
	}
	additional->n = number;

	if (current == NULL)
	{
		*head = additional;
		additional->next = NULL;
		return (*head);
	}

	while (current != NULL)
	{
		if (number <= current->next->n && current->next != NULL)
		{
			temp = current->next;
			current->next = additional;
			additional->next = temp;
			return (additional);
		}

		current = current->next;
	}
	current->next = additional;
	additional->next = NULL;
	return (additional);
}
