#include "lists.h"
/**
 * is_palindrome - Function to check if a singly list is a palindrome
 * @head: Head of the list
 * Return: 0 if it is not a palindrom otherwise return 1
*/
int is_palindrome(listint_t **head)
{
	int i, first_sum = 0, second_sum = 0;
	int length = 0;
	listint_t *current = *head;
	listint_t *current_list = *head;

	if (*head == NULL || head == NULL)
	{
		return (0);
	}
	while (current != NULL)
	{
		current = current->next;
		length++;
	}
	for (i = 0; i < length; i++)
	{
		if (i < length / 2)
		{
			first_sum += current_list->n;
		}
		else
		{
			second_sum += current_list->n;
		}
	}
	if (first_sum == second_sum)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}

