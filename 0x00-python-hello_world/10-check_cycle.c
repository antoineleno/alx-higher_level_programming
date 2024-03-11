#include "lists.h"
/**
 * check_cycle - Function to check if a list is a cycle or not
 * @list: Head of the node
 * Return: 0 is not a cycle otherwise 1
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
