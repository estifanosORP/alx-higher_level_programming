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

	fast = malloc(sizeof(listint_t *));
	slow = malloc(sizeof(listint_t *));

	if (list == NULL)
	{
		/*
		* free(fast);
		* free(slow);
		*/
		return (0);
	}

	fast = list;
	slow = list;

	do {
		slow = slow->next;
		if (slow == NULL || fast == NULL)
		{
			/*
			* free(fast);
			* free(slow);
			*/
			return (0);
		}
		fast = fast->next->next;
	} while (fast != slow);

	/*
	* free(fast);
	* free(slow);
	*/
	return (1);
}
