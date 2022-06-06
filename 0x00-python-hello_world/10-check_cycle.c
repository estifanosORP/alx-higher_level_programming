#include "lists.h"
/**
 * check_cycle - checks if a linked list is cyclic
 * @list: pointer to the head of a list
 * Return: 1, if the linkedlist is cyclic
 *         0, otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
	{
		return (0);
	}

	fast = list;
	slow = list;

	do {
		if (slow == NULL || fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	} while (fast != slow);

	return (1);
}
